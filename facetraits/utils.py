import numpy as np

# Индексы ключевых точек
LEFT_EYE_CENTER = 159
RIGHT_EYE_CENTER = 386
LEFT_BROW = 105
RIGHT_BROW = 334
TOP_FOREHEAD = 10
CHIN = 152

def get_point(landmarks, w, h, idx):
    lm = landmarks[idx]
    return np.array([lm.x * w, lm.y * h])

def get_point_3d(landmarks, w, h, idx):
    lm = landmarks[idx]
    return np.array([lm.x * w, lm.y * h, lm.z * w])