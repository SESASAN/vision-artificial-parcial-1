# Momento Evaluativo 2 — Visión Artificial

Taller de histogramas, filtrado espacial y detección/realce de bordes,
graded en dos componentes: "Hacer" (40%, construcción de los algoritmos) y
"Analizar" (60%, sustentación en video).

## Puntos del taller

1. **(1.2)** Histograma y ecualización de histograma sobre la imagen propia
   en escala de grises: histograma original, ecualización, histograma
   ecualizado, nivel de intensidad más probable (original y ecualizada), y
   probabilidad de intensidad=176 en la ecualizada.
2. **(0.6)** Especificación de histograma usando `images/Referencia.tif`
   (500x500, escala de grises) como imagen objetivo.
3. **(2.0)** Ruido (uniforme, gaussiano, sal y pimienta) sobre la imagen
   original en gris, y 9 filtros por cada imagen con ruido (uniforme 3x3/5x5/7x7,
   gaussiano σ=0.5 y σ=1.9 en 3x3/5x5/7x7) — 27 imágenes filtradas en total.
   Evaluación con SSIM contra la imagen original sin ruido para identificar
   el mejor filtro por cada tipo de ruido.
4. **(0.6)** Detección de bordes con Sobel (horizontal/vertical, por
   convolución) y Laplaciano de 8 vecinos; magnitud del gradiente por suma de
   valores absolutos.
5. **(0.6)** Realce de bordes con Laplaciano de 4 y de 8 vecinos (distinto a
   detección de bordes del punto 4).

## Estructura

- `images/` — `Referencia.tif` (imagen objetivo del punto 2) y la imagen
  propia que se genere para el taller (guardarla como `mi_imagen.png`, ver
  `00_preparacion`).
- `notebooks/` — un notebook por punto (`00_preparacion.ipynb` +
  `0X_puntoX.ipynb`), con el enunciado en celdas de markdown y el código
  pendiente marcado con `# TODO`.
- `codigo/` — el mismo código exportado a scripts `.py` planos, uno por
  punto (sin las celdas markdown).
- `results/` — imágenes resultado generadas al resolver cada punto.

## Entorno

Ver el README en la raíz del repositorio para crear y activar el entorno
virtual compartido (`../requirements.txt`).

## Ejecutar

Con el entorno activado:

```bash
jupyter notebook "parcial 2/notebooks/"
```

o, desde `parcial 2/codigo/`, cada script por separado (`python 0X_puntoX.py`),
en orden, empezando por `00_preparacion.py`.

## Contenido de cada notebook/script

| Archivo | Punto | Qué contiene |
|---|---|---|
| `00_preparacion` | — | Carga de la imagen generada con IA |
| `01_punto1` | 1 | Histograma, ecualización, niveles más probables |
| `02_punto2` | 2 | Especificación de histograma contra `Referencia.tif` |
| `03_punto3` | 3 | Ruido (uniforme/gaussiano/sal y pimienta) + 9 filtros + tabla SSIM |
| `04_punto4` | 4 | Detección de bordes: Sobel (kernels dados) y Laplaciano de 8 vecinos |
| `05_punto5` | 5 | Realce de bordes: Laplaciano de 4 y 8 vecinos |
