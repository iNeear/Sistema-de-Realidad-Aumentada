import numpy as np
import cv2
import os
import glob

# Criterio de terminación para la detección de esquinas
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Preparar puntos del objeto, como (0,0,0), (1,0,0), (2,0,0), ..., (5,3,0)
objp = np.zeros((6 * 4, 3), np.float32)
objp[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)

# Arreglos para almacenar puntos del objeto y puntos de la imagen de todas las imágenes
objpoints = []  # Puntos 3D en el espacio del mundo real
imgpoints = []  # Puntos 2D en el plano de la imagen

# Carpeta para almacenar las imágenes capturadas y los parámetros de la cámara
captured_images_folder = 'C:/Users/LENOVO/Desktop/IMG_Calibration/'

# Crear la carpeta si no existe
os.makedirs(captured_images_folder, exist_ok=True)

# Número máximo de capturas deseadas
max_captures = 10

# Inicializar el índice de las imágenes capturadas
image_index = 0

# Inicializar la cámara para la calibración
cap_calibration = cv2.VideoCapture(0)
if not cap_calibration.isOpened():
    print("Error al abrir la cámara para calibración")
    exit()

while image_index < max_captures:
    # Capturar un frame de la cámara
    ret, frame = cap_calibration.read()
    if not ret:
        print("Error al capturar el frame")
        break

    # Mostrar la imagen actual
    cv2.imshow('Captura Actual', frame)

    # Esperar a que el usuario presione una tecla
    key = cv2.waitKey(1)

    # Si la tecla es 'c', capturar la imagen y guardarla
    if key == ord('c'):
        print(f"Capturando imagen {image_index + 1} de {max_captures}...")

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Encontrar las esquinas del tablero de ajedrez en la imagen en escala de grises
        ret, corners = cv2.findChessboardCorners(gray, (6, 4), None)

        # Si se encuentran esquinas del tablero de ajedrez, agregar puntos del objeto y puntos de la imagen (después de refinarlos)
        if ret:
            objpoints.append(objp)  # Almacenar las coordenadas 3D de las esquinas del tablero de ajedrez
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)  # Almacenar las coordenadas 2D de las esquinas del tablero de ajedrez

            # Dibujar y mostrar las esquinas en la imagen
            frame = cv2.drawChessboardCorners(frame, (6, 4), corners2, ret)
            cv2.imshow('Captura Actual', frame)
            cv2.waitKey(500)  # Esperar medio segundo entre imágenes
            image_index += 1

    elif key == ord('q') or (key == 27):  # Tecla 'q' o 'Esc' para salir
        print("Saliendo...")
        break

# Liberar la cámara de calibración y las ventanas
cap_calibration.release()
cv2.destroyAllWindows()

# Calibración utilizando las imágenes capturadas
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print('\nMatriz de la cámara (mtx):')
print(mtx)  # Parámetros intrínsecos de la cámara
print('\nParámetros de distorsión (dist):')
print(dist)  # Coeficientes de distorsión

calibration_file_path = f"{captured_images_folder}calibration_params.npz"
np.savez(calibration_file_path, mtx=mtx, dist=dist)

# Continuación del código para generar el cubo 3D
# Preparar puntos del objeto, como (0,0,0), (1,0,0), (2,0,0), ..., (7,5,0)
#cube = np.array([[1, 1, 0], [1, -1, 0], [-1, -1, 0], [-1, 1, 0], [1, 1, 2], [1, -1, 2], [-1, -1, 2], [-1, 1, 2]])

# Inicializar la cámara para ARuco
cap_aruco = cv2.VideoCapture(0)  # Puedes cambiar el número de la cámara si tienes más de una

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_100)
parameters = cv2.aruco.DetectorParameters()

while True:
    # Leer el frame actual desde la cámara de ARuco
    ret, frame = cap_aruco.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los marcadores ArUco
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if np.all(ids is not None):
        for i in range(0, len(ids)):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.05, mtx, dist)
            (rvec - tvec).any()  # Para suprimir la salida

            # Dibujar los marcadores detectados
            cv2.aruco.drawDetectedMarkers(frame, corners)

            # Dibujar ejes
            cv2.aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.1)


            # Dibujar cubo
            # Cara inferior
            v1, v2 = corners[i][0][0][0], corners[i][0][0][1]
            v3, v4 = corners[i][0][1][0], corners[i][0][1][1]
            v5, v6 = corners[i][0][2][0], corners[i][0][2][1]
            v7, v8 = corners[i][0][3][0], corners[i][0][3][1]

            cv2.line(frame, (int(v1), int(v2)), (int(v3), int(v4)), (255, 255, 0), 3)
            cv2.line(frame, (int(v5), int(v6)), (int(v7), int(v8)), (255, 255, 0), 3)
            cv2.line(frame, (int(v1), int(v2)), (int(v7), int(v8)), (255, 255, 0), 3)
            cv2.line(frame, (int(v3), int(v4)), (int(v5), int(v6)), (255, 255, 0), 3)

            # Cara superior
            cv2.line(frame, (int(v1), int(v2 - 200)), (int(v3), int(v4 - 200)), (255, 255, 0), 3)
            cv2.line(frame, (int(v5), int(v6 - 200)), (int(v7), int(v8 - 200)), (255, 255, 0), 3)
            cv2.line(frame, (int(v1), int(v2 - 200)), (int(v7), int(v8 - 200)), (255, 255, 0), 3)
            cv2.line(frame, (int(v3), int(v4 - 200)), (int(v5), int(v6 - 200)), (255, 255, 0), 3)

            # Caras laterales
            cv2.line(frame, (int(v1), int(v2 - 200)), (int(v1), int(v2)), (255, 255, 0), 3)
            cv2.line(frame, (int(v3), int(v4 - 200)), (int(v3), int(v4)), (255, 255, 0), 3)
            cv2.line(frame, (int(v5), int(v6 - 200)), (int(v5), int(v6)), (255, 255, 0), 3)
            cv2.line(frame, (int(v7), int(v8 - 200)), (int(v7), int(v8)), (255, 255, 0), 3)

    # Mostrar el frame
    cv2.imshow('frame', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara de ARuco y las ventanas
cap_aruco.release()
cv2.destroyAllWindows()
