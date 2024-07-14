import area
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius

circle1 = Circle(5)

area = circle1.calculate_area()
print("Area of the circle:",area)
