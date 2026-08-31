"""Funciones de apoyo para las transformaciones de intensidad del taller.

Toda la lógica está hecha con numpy: cada imagen en escala de grises se
maneja como una matriz 2D de enteros (0-255), y las transformaciones se
aplican con operaciones vectorizadas (sobre toda la matriz a la vez) en
lugar de recorrer pixel por pixel con loops de Python.
"""
import numpy as np


def to_uint8(img):
    """Escala linealmente los valores de `img` a [0,255] y castea a uint8.

    Se usa al final de las transformaciones cuyo resultado puede salirse
    del rango 0-255 (como gamma_transform), para cumplir con el requisito
    del enunciado de entregar siempre imágenes uint8.
    """
    img = img.astype(np.float64)
    img -= img.min()
    if img.max() > 0:
        img *= 255.0 / img.max()
    return img.astype(np.uint8)


def gamma_transform(gray, gamma, c=None):
    """Transformación gamma (potencia): s = c * r^gamma.

    `gray` es la imagen en escala de grises (matriz numpy uint8), `r` es
    esa imagen normalizada a [0,1] (gray/255) y `np.power` aplica el
    exponente a cada pixel a la vez. gamma<1 aclara la imagen (expande
    sombras), gamma>1 la oscurece (expande luces).
    """
    r = gray.astype(np.float64) / 255.0
    if c is None:
        c = 1.0
    s = c * np.power(r, gamma)
    return to_uint8(s)


def log_transform(gray, c=None):
    """Transformación logarítmica: s = c * log(1 + r).

    A diferencia de gamma, siempre aclara la imagen, y lo hace expandiendo
    más los tonos oscuros que los claros. `c` se calcula por defecto para
    que el pixel más brillante de la entrada quede en 255.
    """
    r = gray.astype(np.float64)
    if c is None:
        c = 255.0 / np.log(1 + r.max())
    s = c * np.log(1 + r)
    return np.clip(s, 0, 255).astype(np.uint8)


def negative_transform(gray):
    """Transformación negativa: s = 255 - r (invierte los tonos)."""
    return 255 - gray.astype(np.uint8)


def piecewise_linear(gray, r1, s1, r2, s2):
    """Transformación lineal a trozos (contrast stretching).

    Define tres rectas que unen los puntos (0,0) -> (r1,s1) -> (r2,s2) ->
    (255,255). Se usan máscaras booleanas de numpy (comparaciones sobre
    toda la matriz) para saber en qué tramo cae cada pixel, y luego se le
    aplica la recta correspondiente a cada uno de esos tramos.
    """
    gray = gray.astype(np.float64)
    out = np.zeros_like(gray)

    seg1 = gray <= r1
    seg2 = (gray > r1) & (gray <= r2)
    seg3 = gray > r2

    out[seg1] = (s1 / r1) * gray[seg1] if r1 != 0 else 0
    out[seg2] = ((s2 - s1) / (r2 - r1)) * (gray[seg2] - r1) + s1
    out[seg3] = ((255 - s2) / (255 - r2)) * (gray[seg3] - r2) + s2 if r2 != 255 else s2

    return np.clip(out, 0, 255).astype(np.uint8)


def gray_level_slicing(gray, A, B, preserve_background=False):
    """Fraccionamiento de gris: resalta el rango [A,B] llevándolo a 255.

    `mask` es una matriz booleana (True donde el pixel está entre A y B).
    Si `preserve_background` es False (comportamiento del taller), el
    resto de la imagen se lleva a 0; si es True, el fondo conserva su
    valor original en vez de volverse negro.
    """
    gray = gray.astype(np.uint8)
    mask = (gray >= A) & (gray <= B)
    if preserve_background:
        out = gray.copy()
        out[mask] = 255
    else:
        out = np.zeros_like(gray)
        out[mask] = 255
    return out
