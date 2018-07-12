# -*- coding: utf-8 -*-

class Action(object):
    def activate(self):
        # Called when action activated
        pass
    
    def __call__(self):
        # Called every frame while action is activated
        pass

    def deactivate(self):
        # Called when action deactivated
        pass