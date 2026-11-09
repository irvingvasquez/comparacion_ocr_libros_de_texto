# Comparación OCR de libros de texto

Visor para comparar, página por página, tres transcripciones de los mismos escaneos:

- **Marker / Surya**
- **Nanonets-OCR2-3B**
- **DeepSeek-OCR**

La muestra son tres libros de texto gratuitos históricos de la CONALITEG, elegidos al azar (semilla 42). El escaneo queda a la izquierda y las tres transcripciones a la derecha.

| Año | Grado | Libro | Páginas |
| --- | --- | --- | --- |
| 1960 | 4.º | Mi libro de lengua nacional | 129 |
| 1962 | 6.º | Aritmética y geometría | 131 |
| 1988 | 4.º | Matemáticas | 259 |

## Requisitos

Python 3.9 o posterior. No hay paquetes que instalar.

## Descargar y abrir

```bash
git clone https://github.com/irvingvasquez/comparacion_ocr_libros_de_texto.git
cd comparacion_ocr_libros_de_texto
python3 servir.py
```

Eso sirve el visor en http://127.0.0.1:8765/review.html y abre el navegador. Para detenerlo, pulsa Ctrl+C.

Si el puerto 8765 está ocupado:

```bash
python3 servir.py --port 8766
```

Para servir sin abrir el navegador:

```bash
python3 servir.py --no-browser
```

El mismo resultado, sin el script:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

y abre http://127.0.0.1:8765/review.html.

Conviene usar el servidor local. Si se abre `review.html` directamente como archivo, algunos navegadores no cargan los escaneos.

## Cómo usarlo

- El menú **Libro** cambia de volumen.
- **Página anterior** y **Página siguiente**, o las flechas izquierda y derecha, cambian de página.
- Las flechas arriba y abajo cambian de libro.

## De dónde salen los textos

Los PDF originales están en [libros_de_texto_gratuitos](https://github.com/irvingvasquez/libros_de_texto_gratuitos), tomados del histórico de la CONALITEG: https://historico.conaliteg.gob.mx/

`sample.json` guarda la semilla, las rutas dentro de ese corpus y el tiempo de cada motor. Las imágenes de esta carpeta son las páginas rasterizadas a 200 dpi. El texto de cada motor ya va dentro de `review.html`.

## Licencia

Los libros pertenecen a la SEP/CONALITEG. El corpus de origen se comparte bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Este visor, al ser un derivado de ese material, se comparte con la misma licencia. El uso es académico.
