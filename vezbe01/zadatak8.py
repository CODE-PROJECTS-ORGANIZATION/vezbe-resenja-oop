import math


def quadratic_equation(a, b, c):
    determinant = math.pow(b, 2) - 4 * a * c
    if determinant < 0:
        return "Quadratic function does not have real solutions"
    elif determinant == 0:
        return f"Quadratic function has one unique real solutions: {-b / (2 * a)}"
    else:
        x1 = (-b + math.sqrt(determinant)) / (2 * a)
        x2 = (-b - math.sqrt(determinant)) / (2 * a)
        return f"Quadratic function has two real solutions: x1 = {x1} and x2 = {x2}"


def main():
    no_real_solutions = "Quadratic function does not have real solutions"
    assert no_real_solutions == quadratic_equation(1, 2, 3)
    one_real_solution = "Quadratic function has one unique real solutions: -1.0"
    assert one_real_solution == quadratic_equation(1, 2, 1)
    two_real_solutions = "Quadratic function has two real solutions: x1 = -0.8541019662496847 and x2 = 5.854101966249685"
    assert two_real_solutions == quadratic_equation(-1, 5, 5)
    a = float(input("Enter parameter a:"))
    b = float(input("Enter parameter b:"))
    c = float(input("Enter parameter c:"))
    print(quadratic_equation(a, b, c))


if __name__ == "__main__":
    main()
