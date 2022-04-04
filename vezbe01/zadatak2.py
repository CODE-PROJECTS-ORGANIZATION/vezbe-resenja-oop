import math


def calculate_side_of_the_square(area):
    return math.sqrt(area)


def calculate_side_of_the_square1(area):
    diagonal = math.sqrt(2 * area)
    a = diagonal / math.sqrt(2)
    return a


def calculate_area_of_the_isosceles_triangle(a_side, b_side):
    a_height = math.sqrt(math.pow(b_side, 2) - math.pow(a_side / 2, 2))
    return a_side * a_height / 2


def calculate_area_of_the_isosceles_triangle1(a_side, b_side):
    # Using Heron's formula
    o = (a_side + 2 * b_side) / 2
    return math.sqrt(o * (o - a_side) * (o - b_side) * (o - b_side))


def main():
    area_of_square = 16
    assert calculate_side_of_the_square(area_of_square) == calculate_side_of_the_square1(area_of_square)
    print(f"Side of square is equal to: {calculate_side_of_the_square(area_of_square)}")
    a_side = 4
    b_side = 6
    assert calculate_area_of_the_isosceles_triangle(a_side,b_side) ==calculate_area_of_the_isosceles_triangle1(a_side,b_side)
    print(f"Area of isosceles triangle is: {calculate_area_of_the_isosceles_triangle(a_side,b_side)}")



if __name__ == "__main__":
    main()
