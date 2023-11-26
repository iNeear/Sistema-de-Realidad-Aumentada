import cv2
import numpy as np

# Definir un diccionario de opciones
opciones = {
    "1": "cv2.aruco.DICT_4X4_50",
    "2": "cv2.aruco.DICT_4X4_100",
    "3": "cv2.aruco.DICT_4X4_250",
    "4": "cv2.aruco.DICT_5X5_50",
    "5": "cv2.aruco.DICT_5X5_100",
    "6": "cv2.aruco.DICT_5X5_250",
    "7": "cv2.aruco.DICT_6X6_50",
    "8": "cv2.aruco.DICT_6X6_100",
    "9": "cv2.aruco.DICT_6X6_250",
    "10": "cv2.aruco.DICT_7X7_50",
    "11": "cv2.aruco.DICT_7X7_100",
    "12": "cv2.aruco.DICT_7X7_250",
    "13": "cv2.aruco.DICT_ARUCO_ORIGINAL",
    "14": "cv2.aruco.DICT_APRILTAG_16h5",
    "15": "cv2.aruco.DICT_APRILTAG_25h9",
    "16": "cv2.aruco.DICT_APRILTAG_36h11"
}

# Mostrar las opciones al usuario
print("Seleccione una opción:")
print()

# Iterar sobre la lista y mostrar las opciones numeradas
for clave, opcion in opciones.items():
    print(f"{clave}: {opcion}")

# Solicitar al usuario que elija una opción
while True:
    print()
    seleccion = input("Elija el número de la opción: ")
    if seleccion in opciones:
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Obtener la opción seleccionada por el usuario
opcion_seleccionada_str = opciones[seleccion]

# Mostrar la opción seleccionada
print(f"Ha seleccionado: {opcion_seleccionada_str}")

# Convertir la cadena de texto en un objeto real
opcion_seleccionada = eval(opcion_seleccionada_str)
print()

# Solicitar al usuario que ingrese el ID del marcador
while True:
    id = int(input("Ingrese el ID del marcador (0-999): "))
    if 0 <= id <= 999:
        break
    else:
        print("ID no válido. Inténtelo de nuevo.")

# Solicitar al usuario que ingrese el tamaño deseado (img_size)
while True:
    img_size = int(input("Ingrese el tamaño deseado (10-700): "))
    if 10 <= img_size <= 700:
        break
    else:
        print("Tamaño no válido. Inténtelo de nuevo.")
print()

# Definir el diccionario ArUco y el ID del marcador
aruco_dict = cv2.aruco.getPredefinedDictionary(opcion_seleccionada)

# Generar y guardar el marcador ArUco
marker_img = cv2.aruco.generateImageMarker(aruco_dict, id, img_size)
cv2.imwrite(f"aruco_{opcion_seleccionada_str}_ID{str(id)}_Size{str(img_size)}.png", marker_img)

print(f"Se ha generado y guardado el marcador con ID {id} y tamaño {img_size}.")

# Cargar la imagen que se superpondrá
try:
    overlay_image = cv2.imread("D:/5. PROYECTOS PY/Compute Vision/Proyecto/Spiderman.png")
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit()

# Inicializar la cámara
try:
    cap = cv2.VideoCapture(1)  # Puedes cambiar el número de la cámara si tienes más de una
except Exception as e:
    print(f"Error al inicializar la cámara: {e}")
    exit()

while True:
    ret, frame = cap.read()
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar los marcadores ArUco
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
    
    # Dibujar los marcadores ArUco y superponer la imagen
    if ids is not None and id in ids:
        index = np.where(ids == id)[0][0]
        corner = corners[index].astype(int)
        
        # Obtener las esquinas del marcador ArUco
        c1 = tuple(corner[0][0])
        c2 = tuple(corner[0][1])
        c3 = tuple(corner[0][2])
        c4 = tuple(corner[0][3])
        
        # Definir las coordenadas de la imagen para la transformación de perspectiva
        pts_image = np.array([[0, 0], [overlay_image.shape[1] - 1, 0], 
                              [overlay_image.shape[1] - 1, overlay_image.shape[0] - 1], 
                              [0, overlay_image.shape[0] - 1]], dtype=np.float32)
        pts_aruco = np.array([c1, c2, c3, c4], dtype=np.float32)
        
        # Calcular la matriz de transformación de perspectiva
        matrix = cv2.getPerspectiveTransform(pts_image, pts_aruco)
        
        # Aplicar la transformación de perspectiva
        overlay = cv2.warpPerspective(overlay_image, matrix, (frame.shape[1], frame.shape[0]))
        
        # Crear una máscara del mismo tamaño que el frame
        mask = np.ones(frame.shape, dtype=np.uint8)*255

        # Rellenar un polígono negro en la máscara en la ubicación del marcador ArUco
        cv2.fillConvexPoly(mask, np.int32([pts_aruco]), (0, 0, 0))

        # Aplicar la máscara al frame
        frame_masked = cv2.bitwise_and(frame, mask)

        # Superponer la imagen en el frame enmascarado
        frame_with_overlay = cv2.addWeighted(frame_masked, 1, overlay, 0.7, 0)
        cv2.imshow("AR with ArUco", frame_with_overlay)
    else:
        cv2.imshow("AR with ArUco", frame)
    
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
