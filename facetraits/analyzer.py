from dataclasses import dataclass
import cv2
from facetraits.traits import Chin, Forehead, Jawline, Symmetry
from facetraits.traits.brow_ridges import BrowRidges, calculate_brow_eye_drop_percentage
from facetraits.utils import get_point
import numpy as np
import mediapipe as mp
from facetraits.utils import *

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

    def analyze(self, visualize: bool = False):
        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

        rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_image)

        w, h = rgb_image.shape[1], rgb_image.shape[0]
        landmarks = results.multi_face_landmarks[0].landmark

        brow = calculate_brow_eye_drop_percentage(landmarks)
        print(f"Brow: {brow}")

        if visualize:
            mp_drawing = mp.solutions.drawing_utils
            drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))

            newimage = self.image.copy()

            # Обработка изображения
            with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True) as face_mesh:
                results = face_mesh.process(rgb_image)

                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        # Рисуем точки и линии
                        mp_drawing.draw_landmarks(
                            image=newimage,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_TESSELATION,
                            landmark_drawing_spec=drawing_spec,
                            connection_drawing_spec=drawing_spec
                        )
            for idx in [
                LEFT_EYE_CENTER, RIGHT_EYE_CENTER,
                LEFT_BROW, RIGHT_BROW,
                TOP_FOREHEAD, CHIN
            ]:
                point = get_point(landmarks, w, h, idx).astype(int)
                cv2.circle(newimage, tuple(point), 3, (255, 0, 0), -1)
            cv2.imshow("Face Mesh", newimage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        return AnalysisReport(
            symmetry=None,
            chin=None,
            jawline=None,
            forehead=None,
            brow_ridges=brow,
        )

@dataclass
class AnalysisReport:
    symmetry: Symmetry
    chin: Chin
    jawline: Jawline
    forehead: Forehead
    brow_ridges: BrowRidges