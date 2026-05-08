import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self):
        return self.width
    
    def set_height(self):
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)
    
