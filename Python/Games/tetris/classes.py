import globals
import random

class Shape:
    def __init__(self):
        self.object_list = []
        self.color = (0, 0, 0)
        self.shift = 0
        self.rotation = 0

    def get_object_list(self):
        return self.object_list

    def get_color(self):
        return self.color

    def set_object_list(self, object_list):
        self.object_list = object_list

    def set_color(self, color):
        self.color = color

    def set_shift(self, shift):
        self.shift = shift
        for index in range(len(self.object_list)): self.object_list[index][0] += shift

    def fall(self):
        for index in range(len(self.object_list)): self.object_list[index][1] += 1

    def hitTheLeftSide(self, floor):
        for point in self.object_list:
            if point[0] <= 0: return True

        # Check if its hit the shapes at the bottom of the "map"
        for shape_point in self.get_object_list():
            for floor_point in floor:
                if shape_point[1] == floor_point[1] and shape_point[0] == floor_point[0] + 1: return True


    def hitTheRightSide(self, floor):
        for point in self.object_list:
            if point[0] >= 9: return True

        # Check if its hit the shapes at the bottom of the "map"
        for shape_point in self.get_object_list():
            for floor_point in floor:
                if shape_point[1] == floor_point[1] and shape_point[0] == floor_point[0] - 1: return True

    def brokeTheLeftSide(self, floor):
        for point in self.object_list:
            if point[0] < 0: return True

        # Check if its hit the shapes at the bottom of the "map"
        for shape_point in self.get_object_list():
            for floor_point in floor:
                if shape_point[1] == floor_point[1] and shape_point[0] == floor_point[0]: return True

    def brokeTheRightSide(self, floor):
        for point in self.object_list:
            if point[0] > 9: return True

        # Check if its hit the shapes at the bottom of the "map"
        for shape_point in self.get_object_list():
            for floor_point in floor:
                if shape_point[1] == floor_point[1] and shape_point[0] == floor_point[0]: return True

    def hitTheBottom(self, floor):
        stop = False

        # Check if its hit the bottom of the "map"
        for point in self.object_list:
            if point[1] == 19: return True

        # Check if its hit the shapes at the bottom of the "map"
        for shape_point in self.get_object_list():
            for floor_point in floor:
                if shape_point[1] == floor_point[1] - 1 and shape_point[0] == floor_point[0]: return True

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, 0], [1, 0], [0, -1], [1, -1]]
        self.color = (100, 10, 100)

    def rotate(self):
        self.rotation = 0

class Line(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 2
            self.object_list[0][1] += -2
            self.object_list[1][0] += 1
            self.object_list[1][1] += -1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += -1
            self.object_list[3][1] += 1
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] -= 2
            self.object_list[0][1] -= -2
            self.object_list[1][0] -= 1
            self.object_list[1][1] -= -1
            self.object_list[2][0] -= 0
            self.object_list[2][1] -= 0
            self.object_list[3][0] -= -1
            self.object_list[3][1] -= 1
            self.rotation = 0


class L(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, 0], [0, -1], [1, -1], [2, -1]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 0
            self.object_list[0][1] += -2
            self.object_list[1][0] += 1
            self.object_list[1][1] += -1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += -1
            self.object_list[3][1] += 1
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] += 2
            self.object_list[0][1] += 0
            self.object_list[1][0] += 1
            self.object_list[1][1] += 1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += -1
            self.object_list[3][1] += -1
            self.rotation = 2
        elif self.rotation == 2:
            self.object_list[0][0] += 0
            self.object_list[0][1] += 2
            self.object_list[1][0] += -1
            self.object_list[1][1] += 1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += 1
            self.object_list[3][1] += -1
            self.rotation = 3
        elif self.rotation == 3:
            self.object_list[0][0] += -2
            self.object_list[0][1] += 0
            self.object_list[1][0] += -1
            self.object_list[1][1] += -1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += 1
            self.object_list[3][1] += 1
            self.rotation = 0

class J(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, -1], [1, -1], [2, -1], [2, 0]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 1
            self.object_list[0][1] += -1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += 1
            self.object_list[3][0] += -2
            self.object_list[3][1] += 0
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] += 1
            self.object_list[0][1] += 1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += -1
            self.object_list[3][0] += 0
            self.object_list[3][1] += -2
            self.rotation = 2
        elif self.rotation == 2:
            self.object_list[0][0] += -1
            self.object_list[0][1] += 1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += 1
            self.object_list[2][1] += -1
            self.object_list[3][0] += 2
            self.object_list[3][1] += 0
            self.rotation = 3
        elif self.rotation == 3:
            self.object_list[0][0] += -1
            self.object_list[0][1] += -1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += 1
            self.object_list[2][1] += 1
            self.object_list[3][0] += 0
            self.object_list[3][1] += 2
            self.rotation = 0

class S(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, 0], [1, 0], [1, -1], [2, -1]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 1
            self.object_list[0][1] += -2
            self.object_list[1][0] += 0
            self.object_list[1][1] += -1
            self.object_list[2][0] += 1
            self.object_list[2][1] += 0
            self.object_list[3][0] += 0
            self.object_list[3][1] += 1
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] += 1
            self.object_list[0][1] += 1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += 1
            self.object_list[3][0] += -2
            self.object_list[3][1] += 0
            self.rotation = 2
        elif self.rotation == 2:
            self.object_list[0][0] += 0
            self.object_list[0][1] += 1
            self.object_list[1][0] += 1
            self.object_list[1][1] += 0
            self.object_list[2][0] += 0
            self.object_list[2][1] += -1
            self.object_list[3][0] += 1
            self.object_list[3][1] += -2
            self.rotation = 3
        elif self.rotation == 3:
            self.object_list[0][0] += -2
            self.object_list[0][1] += 0
            self.object_list[1][0] += -1
            self.object_list[1][1] += 1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += 1
            self.object_list[3][1] += 1
            self.rotation = 0

class Z(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, -1], [1, -1], [1, 0], [2, 0]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 2
            self.object_list[0][1] += -1
            self.object_list[1][0] += 1
            self.object_list[1][1] += 0
            self.object_list[2][0] += 0
            self.object_list[2][1] += -1
            self.object_list[3][0] += -1
            self.object_list[3][1] += 0
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] += 0
            self.object_list[0][1] += 2
            self.object_list[1][0] += -1
            self.object_list[1][1] += 1
            self.object_list[2][0] += 0
            self.object_list[2][1] += 0
            self.object_list[3][0] += -1
            self.object_list[3][1] += -1
            self.rotation = 2
        elif self.rotation == 2:
            self.object_list[0][0] += -1
            self.object_list[0][1] += 0
            self.object_list[1][0] += 0
            self.object_list[1][1] += -1
            self.object_list[2][0] += 1
            self.object_list[2][1] += 0
            self.object_list[3][0] += 2
            self.object_list[3][1] += -1
            self.rotation = 3
        elif self.rotation == 3:
            self.object_list[0][0] += -1
            self.object_list[0][1] += -1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += 1
            self.object_list[3][0] += 0
            self.object_list[3][1] += 2
            self.rotation = 0

class T(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.object_list = [[0, -1], [1, -1], [2, -1], [1, 0]]
        self.color = (100, 10, 100)

    def rotate(self):
        if self.rotation == 0:
            self.object_list[0][0] += 1
            self.object_list[0][1] += -1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += 1
            self.object_list[3][0] += -1
            self.object_list[3][1] += -1
            self.rotation = 1
        elif self.rotation == 1:
            self.object_list[0][0] += 1
            self.object_list[0][1] += 1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += -1
            self.object_list[2][1] += -1
            self.object_list[3][0] += 1
            self.object_list[3][1] += -1
            self.rotation = 2
        elif self.rotation == 2:
            self.object_list[0][0] += -1
            self.object_list[0][1] += 1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += 1
            self.object_list[2][1] += -1
            self.object_list[3][0] += 1
            self.object_list[3][1] += 1
            self.rotation = 3
        elif self.rotation == 3:
            self.object_list[0][0] += -1
            self.object_list[0][1] += -1
            self.object_list[1][0] += 0
            self.object_list[1][1] += 0
            self.object_list[2][0] += 1
            self.object_list[2][1] += 1
            self.object_list[3][0] += -1
            self.object_list[3][1] += 1
            self.rotation = 0

def Random_New_Shape():
    type = random.randint(1, 7)
    color = (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))

    if type in [1]: shift = random.randint(0, 8)
    elif type in [3, 4, 5, 6, 7]: shift = random.randint(0, 7)
    elif type in [2]: shift = random.randint(0, 6)

    if type == 1: shape = Square()
    elif type == 2: shape = Line()
    elif type == 3: shape = L()
    elif type == 4: shape = J()
    elif type == 5: shape = S()
    elif type == 6: shape = Z()
    elif type == 7: shape = T()

    shape.set_shift(shift)
    shape.set_color(color)
    return shape