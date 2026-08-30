"""Funciones de apoyo para las transformaciones de intensidad del taller."""
import numpy as np


def to_uint8(img):
    """Escala y convierte a uint8 (rango 0-255)."""
    img = img.astype(np.float64)
    img -= img.min()
    if img.max() > 0:
        img *= 255.0 / img.max()
    return img.astype(np.uint8)


def gamma_transform(gray, gamma, c=None):
    """s = c * r^gamma, con r normalizado a [0,1]."""
    r = gray.astype(np.float64) / 255.0
    if c is None:
        c = 1.0
    s = c * np.power(r, gamma)
    return to_uint8(s)


def log_transform(gray, c=None):
    """s = c * log(1 + r)."""
    r = gray.astype(np.float64)
    if c is None:
        c = 255.0 / np.log(1 + r.max())
    s = c * np.log(1 + r)
    return np.clip(s, 0, 255).astype(np.uint8)


def piecewise_linear(gray, r1, s1, r2, s2):
    """Transformación lineal a trozos (contrast stretching) definida por
    los puntos (0,0) -> (r1,s1) -> (r2,s2) -> (255,255)."""
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
    """Realza el rango [A,B] llevándolo a 255, el resto a 0
    (o al valor original si preserve_background=True)."""
    gray = gray.astype(np.uint8)
    mask = (gray >= A) & (gray <= B)
    if preserve_background:
        out = gray.copy()
        out[mask] = 255
    else:
        out = np.zeros_like(gray)
        out[mask] = 255
    return out
