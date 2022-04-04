import math


def calculate_cone_surface_area(radius, height):
    # Pi * r * (r + sqrt(r^2 + h^2))
    return math.pi * radius * (radius + math.sqrt(math.pow(radius, 2) + math.pow(height, 2)))


def main():
    radius = float(input("Enter radius of cone:"))
    height = float(input("Enter height of cone:"))
    print(f"Surface area of cone is: {calculate_cone_surface_area(radius, height)}")


if __name__ == "__main__":
    main()
