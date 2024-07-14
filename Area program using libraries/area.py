import math

def calculate_circle_area(radius):
  if radius < 0:
    return "Radius cannot be negative"
  else:
    return math.pi*pow(radius,2)


def calculate_rectangle_area(length,width):
  if length < 0 or width < 0:
    return "Invalid input, length or width cannot be negative"
  else:
    return length*width
    

def calculate_triangle_area(base,height):
  if base < 0 or height < 0:
    return "Invalid input, base or height cannot be negative"
  else:
    return 0.5*base*height
