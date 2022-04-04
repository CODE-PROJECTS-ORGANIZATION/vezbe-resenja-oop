"""
Most important thing for star pattern problems:
1. first diagonal condition: j = i
2. second diagonal condition: j = n - i - 1
"""


def square_pattern(n):
    print("Square pattern:")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def right_triangle_pattern(n):
    print("Right triangle pattern:")
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


def reverse_right_triangle_pattern(n):
    print("Reverse right triangle pattern:")
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()


def left_triangle_pattern(n):
    print("Left triangle pattern:")
    for i in range(n):
        for j in range(0, n - i - 1):
            print(" ", end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()


def reverse_left_triangle_pattern(n):
    print("Reverse left triangle pattern:")
    for i in range(n):
        for j in range(0, i):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()


def hill_pattern(n):
    print("Hill pattern:")
    for i in range(n):
        # Left triangle pattern
        for j in range(0, n - i - 1):
            print(" ", end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        # Right triangle pattern
        # range(1, i + 1) eliminates column duplicates repetition
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


def reverse_hill_pattern(n):
    print("Reverse hill pattern:")
    for i in range(n):
        # Reverse left triangle pattern
        for j in range(0, i):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        # Reverse right triangle pattern
        # range(1, n - i) eliminates column duplicates repetition
        for j in range(1, n - i):
            print("*", end=" ")
        print()


def diamond_pattern(n):
    print("Diamond pattern:")
    # Hill pattern
    for i in range(n):
        # Left triangle pattern
        for j in range(0, n - i - 1):
            print(" ", end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        # Right triangle pattern
        # range(1, i + 1) eliminates column duplicates repetition
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    # Reverse hill pattern
    # range(1, n) eliminates rows duplicates repetition
    for i in range(1, n):
        # Reverse left triangle pattern
        for j in range(0, i):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        # Reverse right triangle pattern
        # range(1, n - i) eliminates column duplicates repetition
        for j in range(1, n - i):
            print("*", end=" ")
        print()


def diamond_separator_pattern(n, separator):
    print("Diamond pattern with separator:")
    # Hill pattern
    for i in range(n):
        # Left triangle pattern
        for j in range(0, n - i - 1):
            print(separator, end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        # Right triangle pattern
        # range(1, i + 1) eliminates column duplicates repetition
        for j in range(1, i + 1):
            print("*", end=" ")
        # Extra added loop to print separator after right triangle pattern
        for j in range(i + 1, n):
            print(separator, end=" ")
        print()
    # Reverse hill pattern
    # range(1, n) eliminates rows duplicates repetition
    for i in range(1, n):
        # Reverse left triangle pattern
        for j in range(0, i):
            print(separator, end=" ")
        for j in range(i, n):
            print("*", end=" ")
        # Reverse right triangle pattern
        # range(1, n - i) eliminates column duplicates repetition
        for j in range(1, n - i):
            print("*", end=" ")
        for j in range(n - i, n):
            print(separator, end=" ")
        print()


def left_pascals_triangle_pattern(n):
    print("Left Pascal's triangle")
    # Left triangle pattern
    for i in range(n):
        for j in range(0, n - i - 1):
            print(" ", end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()
    # Reverse left triangle pattern
    # range(1, n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(0, i):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()


def right_pascals_triangle_pattern(n):
    print("Right Pascal's triangle")
    # Right triangle pattern
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    # Reverse right triangle pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(n - i):
            print("*", end=" ")
        print()


def butterfly_pattern(n):
    print("Butterfly triangle pattern:")
    for i in range(n):
        # Right triangle pattern
        for j in range(i + 1):
            print("*", end=" ")
        # Extra added loop to print white space after right triangle pattern
        for j in range(i + 1, n):
            print(" ", end=" ")
        # Left triangle pattern
        # range(1, n - i - 1) eliminates columns duplicates repetition
        for j in range(1, n - i - 1):
            print(" ", end=" ")
        for j in range(n - i - 1, n):
            if i == n - 1 and i == j:
                break
            print("*", end=" ")
        print()
    # range(1,n) eliminates rows duplicates repetition
    # Reverse right triangle pattern
    for i in range(1, n):
        for j in range(n - i):
            print("*", end=" ")
        # Extra added loop to print white space after reverse right triangle pattern
        for j in range(n - i, n):
            print(" ", end=" ")
        # Reverse left triangle pattern
        # range(1, i) eliminates columns duplicates repetition
        for j in range(1, i):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()


def pyramid_pattern(n):
    print("Pyramid pattern:")
    # Left triangle pattern
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()


def odd_pyramid_pattern(n):
    print("Odd pyramid pattern:")
    # Left triangle pattern
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - 2 * i - 1, n):
            print("*", end="")
        print()


def reverse_pyramid_pattern(n):
    print("Reverse pyramid pattern:")
    # Reverse left triangle pattern
    for i in range(n):
        for j in range(0, i):
            print(end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()


def diamond_pyramid_pattern(n):
    print("Diamond pyramid pattern:")
    # Pyramid pattern
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()
    # Reverse pyramid pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(0, i):
            print(end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()


def sandglass_pattern(n):
    print("Sandglass_pattern:")
    # Reverse pyramid pattern
    for i in range(1, n):
        for j in range(0, i):
            print(end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    # Pyramid pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()


def double_hill(n):
    print("Double_hill:")
    # Pyramid pattern
    for i in range(0, n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        # Extra added loop to print white space after pyramid pattern
        for j in range(i + 1, n):
            print(end=" ")
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(n - i - 1, n):
            print("*", end=" ")
        print()




def main():
    n = 5
    square_pattern(n)
    right_triangle_pattern(n)
    reverse_right_triangle_pattern(n)
    left_triangle_pattern(n)
    reverse_left_triangle_pattern(n)
    hill_pattern(n)
    reverse_hill_pattern(n)
    diamond_pattern(n)
    diamond_separator_pattern(n, "-")
    left_pascals_triangle_pattern(n)
    right_pascals_triangle_pattern(n)
    butterfly_pattern(n)
    pyramid_pattern(n)
    odd_pyramid_pattern(n)
    reverse_pyramid_pattern(n)
    diamond_pyramid_pattern(n)
    sandglass_pattern(n)
    double_hill(n)


if __name__ == "__main__":
    main()
