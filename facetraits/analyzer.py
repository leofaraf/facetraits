import cv2
import numpy as np

class FaceAnalyzer:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError(f"Could not read image from: {image_path}")
    
    @classmethod
    def from_array(cls, image_array: np.ndarray):
        instance = cls.__new__(cls)  # bypass __init__
        instance.image_path = None
        instance.image = image_array
        return instance

    def analyze(self):
        # Perform analysis on self.image
        pass