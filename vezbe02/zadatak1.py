def count_down_horizontally(n):
    for i in range(n, 0, -1):
        print(i, end=" ")


def count_down_vertically(n):
    for i in range(n, 0, -1):
        print(i)


def count_down_reversed(n):
    for i in reversed(range(1, n + 1, 1)):
        print(i, end=" ")


def count_down_while(n):
    while n > 0:
        print(n, end=" ")
        n -= 1


def main():
    number = int(input("Enter number:"))
    print("\nHorizontally print:")
    count_down_horizontally(number)
    print("\nVertically print:")
    count_down_vertically(number)
    print("\nReversed print:")
    count_down_reversed(number)
    print("\nWhile print:")
    count_down_while(number)


if __name__ == "__main__":
    main()
