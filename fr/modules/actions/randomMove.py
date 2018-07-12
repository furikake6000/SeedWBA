# -*- coding: utf-8 -*-
import random
import time
import math

BASE_ACTION = {
    "armleft": 0.0,
    "armright": 0.0,
    "wheelleft": 0.0,
    "wheelright": 0.0
}

class RandomMove(object):
    def __init__(self):
        pass

    def activate(self):
        # Called when action activated
        act = BASE_ACTION
        act["armleft"] = 1.0
        act["armright"] = 1.0
        return act
    
    def __call__(self):
        # Called every frame while action is activated
        act = BASE_ACTION
        act["armleft"] = math.sin(time.time() * 2)
        act["armright"] = math.sin(time.time() * 2)
        return act

    def deactivate(self):
        # Called when action deactivated
        return BASE_ACTION
