from facetraits import FaceAnalyzer
from . import assets
import cv2

def test_vizualize():
    print(FaceAnalyzer(assets[8]).analyze())
    FaceAnalyzer(assets[8]).analyze(visualize=True)