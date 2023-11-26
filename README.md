# Sistema de Realidad Aumentada
#### Integrantes: *Jesus Andres Coneo Paredes* - *Alvaro Andres Salgado Martinez*

Este proyecto se centra en el desarrollo de un sistema de Realidad Aumentada (RA) con la capacidad de proyectar elementos 2D y 3D sobre objetos de referencia. La RA, una tecnología emergente, promete aplicaciones innovadoras en diversos campos. No obstante, su adopción en contextos más allá del entretenimiento se enfrenta a desafíos técnicos y de implementación.

# Video de muestra de ArUco_2D

https://github.com/iNeear/Sistema-de-Realidad-Aumentada/assets/131725786/ae3f1cd1-24b4-46c9-aba0-85439ee49771

## Explicación del Código 2D
1. Inicializar el diccionario ArUco y cargar la imagen que se va a superponer
  - Seleccionar el diccionario ArUco y cargar la imagen (Spiderman.png).

2. Inicializar la cámara
  - Iniciar la cámara para la captura en tiempo real.

3. Mientras la cámara esté abierta:
   - Leer un frame de la cámara
     - Capturar un frame de la cámara.
   - Convertir el frame a escala de grises
     - Convertir el frame a escala de grises para facilitar el procesamiento.
   - Detectar los marcadores ArUco en el frame
     - Utilizar el diccionario ArUco para detectar marcadores en el frame.
   - Si se detecta el marcador ArUco:
     1. Obtener las esquinas del marcador
        - Extraer las coordenadas de las esquinas del marcador ArUco.
     2. Calcular la matriz de transformación de perspectiva
        - Calcular la matriz que mapea el marcador al tamaño de la imagen.
     3. Aplicar la transformación de perspectiva a la imagen
        - Transformar la imagen para que coincida con la perspectiva del marcador.
    - Superponer la imagen transformada en el frame
        - Combinar la imagen transformada con el frame original.
    - Mostrar el frame (con o sin la imagen superpuesta)
     - Mostrar el frame resultante, ya sea con o sin la imagen superpuesta.
    - Si se presiona la tecla 'q', cerrar la cámara y salir del bucle
     - Finalizar el bucle si el usuario presiona la tecla 'q'.
5. Cerrar todas las ventanas abiertas
  - Liberar recursos y cerrar ventanas después de la captura.

# Video de muestra de ArUco_3D

La calibración de la cámara es un paso crucial en la visión por computadora. Implica capturar imágenes de un objeto conocido (como un tablero de ajedrez) desde diferentes ángulos para estimar los parámetros de la cámara. Estos parámetros, que incluyen la distancia focal y el punto principal, son esenciales para convertir las coordenadas de los puntos en el mundo 3D a sus correspondientes coordenadas en la imagen 2D. Una vez calibrada, la cámara puede corregir la distorsión de la lente, mejorar la precisión de la detección de objetos y permitir la representación precisa de objetos 3D en la imagen 2D.

https://github.com/iNeear/Sistema-de-Realidad-Aumentada/assets/131725786/f05b4de3-0e64-4bca-904f-820f1a5ce136

Una vez obtenidos los parámetros de la cámara, se procedió a la detección del marcador ArUco. Sin embargo, al detectar el ArUco, la pantalla se congeló debido a un error. Este error, AttributeError: module 'cv2.aruco' has no attribute 'drawAxis', indica que Python no pudo encontrar la función drawAxis en el módulo cv2.aruco. A pesar de varios intentos de solución, incluyendo la verificación de la versión de OpenCV, la desinstalación y reinstalación de OpenCV, y la creación de un nuevo entorno virtual, el problema persistió. 

![Error](https://github.com/iNeear/Sistema-de-Realidad-Aumentada/assets/131725786/b1e587ce-e209-4415-b432-c0ce06e8eb15)

https://github.com/iNeear/Sistema-de-Realidad-Aumentada/assets/131725786/7adc1b5c-5ae4-493c-a1e6-40fc56d89844

## Explicación del Código 3D

1. Preparación y Configuración:
  - Importar bibliotecas necesarias: NumPy, OpenCV y OS.
2. Configuración de la Calibración:
  - Establecer criterio de terminación y definir puntos del objeto (esquinas del tablero de ajedrez).
3. Captura de Imágenes para Calibración:
  - Iniciar la cámara y capturar imágenes del tablero de ajedrez al presionar 'c'.
4. Calibración de la Cámara:
  - Calibrar la cámara utilizando las imágenes capturadas.
5. Guardado de Parámetros de Calibración:
  - Guardar los parámetros de calibración en un archivo.
6. Realidad Aumentada con ARuco:
- Utilizar ARuco para detectar marcadores y superponer un cubo virtual.
7. Dibujo de Marcadores y Cubo:
  - Dibujar marcadores ARuco, ejes y un cubo virtual en el feed de la cámara.
8. Visualización y Salida:
  - Mostrar el feed de la cámara y salir si se presiona 'q'.
9. Liberación de Recursos:
- Liberar recursos de la cámara y cerrar ventanas.










