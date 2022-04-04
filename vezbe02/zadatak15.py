def square_pattern(n):
    print("Square pattern:")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def reverse_left_triangle_pattern(n):
    print("Reverse left triangle pattern:")
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def right_triangle_pattern(n):
    print("Right triangle pattern:")
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def left_triangle_pattern(n):
    print("Left triangle pattern:")
    for i in range(n):
        for j in range(n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def reverse_right_triangle_pattern(n):
    print("Reverse right triangle pattern:")
    for i in range(n):
        for j in range(n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def hill_pattern(n):
    print("Hill pattern:")
    for i in range(n):
        # Left triangle pattern
        for j in range(n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Right triangle pattern
        # range(1,n) eliminates column duplicates repetition
        for j in range(1, n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def reverse_hill_pattern(n):
    print("Reverse hill pattern:")
    for i in range(n):
        # Reverse left triangle pattern
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Reverse right triangle pattern
        # range(1,n) eliminates column duplicates repetition
        for j in range(1, n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def diamond_pattern(n):
    print("Diamond pattern:")
    # Hill pattern
    for i in range(n):
        for j in range(n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # range(1,n) eliminates column duplicates repetition
        for j in range(1, n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    # Reverse hill pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # range(1,n) eliminates column duplicates repetition
        for j in range(1, n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def diamond_separator_pattern(n, separator):
    print("Diamond pattern:")
    # Hill pattern
    for i in range(n):
        for j in range(n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(separator, end=" ")
        for j in range(1, n):
            if i >= j:
                print("*", end=" ")
            else:
                print(separator, end=" ")
        print()
    # Reverse hill pattern
    for i in range(1, n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(separator, end=" ")
        for j in range(1, n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(separator, end=" ")
        print()


def left_pascals_triangle_pattern(n):
    print("Left Pascal's triangle")
    # Left triangle pattern
    for i in range(n):
        for j in range(n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    # Reverse left triangle pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def right_pascals_triangle_pattern(n):
    print("Right Pascal's triangle")
    # Right triangle pattern
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    # Reverse right triangle pattern
    # range(1,n) eliminates rows duplicates repetition
    for i in range(1, n):
        for j in range(n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def butterfly_pattern(n):
    # Right triangle pattern
    print("Butterfly triangle pattern:")
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Left triangle pattern
        # range(1,n) eliminates columns duplicates repetition
        for j in range(1, n):
            if j >= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    # range(1,n) eliminates rows duplicates repetition
    # Reverse right triangle pattern
    for i in range(1, n):
        for j in range(n):
            if j <= (n - i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Reverse left triangle pattern
        # range(1,n) eliminates columns duplicates repetition
        for j in range(1, n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def pyramid_pattern(n):
    print("Pyramid pattern:")
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")


def odd_pyramid_pattern(n):
    print("Odd pyramid pattern:")
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(0, 2 * i + 1):
            print("*", end="")
        print("")


def main():
    n = 5
    square_pattern(n)
    reverse_left_triangle_pattern(n)
    right_triangle_pattern(n)
    left_triangle_pattern(n)
    reverse_right_triangle_pattern(n)
    hill_pattern(n)
    reverse_hill_pattern(n)
    diamond_pattern(n)
    diamond_separator_pattern(n, "-")
    left_pascals_triangle_pattern(n)
    right_pascals_triangle_pattern(n)
    butterfly_pattern(n)
    pyramid_pattern(n)
    odd_pyramid_pattern(n)


if __name__ == "__main__":
    main()
