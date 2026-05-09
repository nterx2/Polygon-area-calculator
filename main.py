class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return self.width
    
    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.width)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        width_picture =  ("*" * self.width + "\n") * self.height
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return width_picture 
    
    def __str__(self):
        result = f"{self.__class__.__name__}(width={self.width}, height={self.height})"
        return result

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side

    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())    
