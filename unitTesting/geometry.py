def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be postitive numbers")
    return length*width

def square_area(length):
    if length <= 0:
        raise ValueError("Length and width must be postitive numbers")
    return length*length