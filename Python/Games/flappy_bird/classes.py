import pygame

class obstacle:
    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2

    def get_x(self):
        return self.x
    def get_y1(self):
        return self.y1
    def get_y2(self):
        return self.y2

    def set_x(self,x):
        self.x = x
    def set_y1(self, y):
        self.y1 = y
    def set_y2(self, y):
        self.y2 = y
