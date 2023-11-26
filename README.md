# Sistema de Realidad Aumentada
Este proyecto se centra en el desarrollo de un sistema de Realidad Aumentada (RA) con la capacidad de proyectar elementos 2D y 3D sobre objetos de referencia. La RA, una tecnología emergente, promete aplicaciones innovadoras en diversos campos. No obstante, su adopción en contextos más allá del entretenimiento se enfrenta a desafíos técnicos y de implementación.

# Video de muestra de ArUco_2D

https://github.com/iNeear/Sistema-de-Realidad-Aumentada/assets/131725786/ae3f1cd1-24b4-46c9-aba0-85439ee49771

## Explicación del Código
1. Inicializar el diccionario ArUco y cargar la imagen que se va a superponer
  - Seleccionar el diccionario ArUco y cargar la imagen (Spiderman.png).

2. Inicializar la cámara
  - Iniciar la cámara para la captura en tiempo real.

3. Mientras la cámara esté abierta:
   1 Leer un frame de la cámara
     - Capturar un frame de la cámara.



   3.2 Convertir el frame a escala de grises
     - Convertir el frame a escala de grises para facilitar el procesamiento.
  3.3 Detectar los marcadores ArUco en el frame
     - Utilizar el diccionario ArUco para detectar marcadores en el frame.
  3.4 Si se detecta el marcador ArUco:
     1. Obtener las esquinas del marcador
        - Extraer las coordenadas de las esquinas del marcador ArUco.
     2. Calcular la matriz de transformación de perspectiva
        - Calcular la matriz que mapea el marcador al tamaño de la imagen.
     3. Aplicar la transformación de perspectiva a la imagen
        - Transformar la imagen para que coincida con la perspectiva del marcador.
     4. Superponer la imagen transformada en el frame
        - Combinar la imagen transformada con el frame original.
  3.5 Mostrar el frame (con o sin la imagen superpuesta)
     - Mostrar el frame resultante, ya sea con o sin la imagen superpuesta.
  3.6 Si se presiona la tecla 'q', cerrar la cámara y salir del bucle
     - Finalizar el bucle si el usuario presiona la tecla 'q'.

5. Cerrar todas las ventanas abiertas
  - Liberar recursos y cerrar ventanas después de la captura.
