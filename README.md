# Momento Evaluativo 1 — Visión Artificial

Solución de los 6 puntos del taller usando indexación de matrices y
transformaciones de intensidad (numpy, OpenCV y scikit-image).

## Requisitos

- Python 3
- Las dependencias listadas en `requirements.txt` (numpy, opencv-contrib-python,
  scikit-image, matplotlib, pillow, jupyter)

## Instalación

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

## Ejecutar solo desde `codigo/`

Cada punto tiene su propio script `.py` en `codigo/`, en el mismo orden que
el enunciado. Los scripts usan rutas relativas (`../images`, `../results`),
así que hay que ejecutarlos **desde dentro de la carpeta `codigo/`**:

```bash
cd codigo
../.venv/bin/python3 00_preparacion.py
../.venv/bin/python3 01_punto1.py
../.venv/bin/python3 02_punto2.py
../.venv/bin/python3 03_punto3.py
../.venv/bin/python3 04_punto4.py
../.venv/bin/python3 05_punto5.py
../.venv/bin/python3 06_punto6.py
```

`00_preparacion.py` debe correrse primero: redimensiona la imagen generada
con IA (`images/cinnamorroll.png`) a 1024x1024x3 y guarda
`images/cinnamorroll_1024.png`, que usan los puntos 1 a 5.

Cada script guarda sus imágenes resultado en `../results/` (es decir,
`results/` en la raíz del proyecto).

## Contenido de cada script

| Script | Punto | Qué hace |
|---|---|---|
| `00_preparacion.py` | — | Carga la imagen generada con IA y la redimensiona a 1024x1024x3 |
| `01_punto1.py` | 1 | Recorte por indexación de matrices y relación de aspecto |
| `02_punto2.py` | 2 | Reordenar canales a BGR, espejo horizontal, inversión vertical |
| `03_punto3.py` | 3 | Transformaciones gamma (γ=0.3, γ=2.3) y logarítmica |
| `04_punto4.py` | 4 | Transformación lineal a trozos con 3 pares de parámetros |
| `05_punto5.py` | 5 | Fraccionamiento de gris (gray-level slicing) con 3 rangos [A,B] |
| `06_punto6.py` | 6 (el reto) | Cadena de transformaciones sobre `Input.tif` evaluada con SSIM contra `Output.tif` |

## Notebooks

El mismo código también está disponible como notebooks de Jupyter en
`notebooks/`, con el enunciado de cada punto en celdas de markdown. Para
usarlos:

```bash
./.venv/bin/jupyter notebook notebooks/
```
