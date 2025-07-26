from facetraits import FaceAnalyzer
from . import assets
import cv2

def test_face_analyzer_creating():
    for asset in assets:
        FaceAnalyzer(asset)
        img = cv2.imread(asset)
        FaceAnalyzer.from_array(img)