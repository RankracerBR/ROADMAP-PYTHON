class Form:
    def area(self):
        pass 
class Form_2D():
    def perimeter(self):
        pass

class Triangle(Form_2D):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2
    
    def perimeter(self):
        return 3 * self.base
    
triangle = Triangle(6,4)
print(triangle.area())
print(triangle.perimeter())