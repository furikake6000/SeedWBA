# -*- coding: utf-8 -*-
import cv2
from ..submodules.facedetector import FaceDetector

class FaceXAxis(object):
    def __init__(self):
        self.fd = FaceDetector()
    
    def analyze(self, observation):
        x, _ = self.fd.biggestFaceRectPosNormalized(observation)
        return x
