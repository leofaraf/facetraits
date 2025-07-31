from dataclasses import dataclass

from facetraits.utils import *

@dataclass
class BrowRidges:
    ratio: float

def calculate_brow_eye_drop_percentage(landmarks) -> float:
    """
    landmarks: список 468 нормализованных точек (x, y, z)
    возвращает средний процент "провисания бровей" (brow drop) от высоты лица
    """
    
    # Высота лица (по оси Y)
    face_height = abs(landmarks[CHIN].y - landmarks[TOP_FOREHEAD].y)

    # Расстояния от бровей до глаз (по оси Y)
    left_brow_eye = abs(landmarks[LEFT_BROW].y - landmarks[LEFT_EYE_CENTER].y)
    right_brow_eye = abs(landmarks[RIGHT_BROW].y - landmarks[RIGHT_EYE_CENTER].y)

    # Среднее расстояние между глазом и бровью
    avg_brow_eye = (left_brow_eye + right_brow_eye) / 2.0

    # Нормализуем в процентах от высоты лица
    brow_drop_percent = (avg_brow_eye / face_height) * 100

    return brow_drop_percent
