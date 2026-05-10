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
        return (2 * self.width) + (2 * self.height)
    
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

    def get_area(self):
        return super().get_area()
    
    def get_perimeter(self):
        return super().get_perimeter()
    
    def get_diagonal(self):
        return super().get_diagonal()
    
    def get_picture(self):
        return super().get_picture()
    
    def __str__(self):
        result = f"{self.__class__.__name__}(side={self.width})"
        return result

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture()) 

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
# print(rect.get_amount_inside(sq))

