def calculate_z(x, y):
    if x < y:
        return max(x, y) / (1 + abs(min(x, y)))
    else:
        return max(x, y) / (1 + min(x, y))


def main():
    x = float(input("Enter x value:"))
    y = float(input("Enter y value:"))
    print(f"Value z:{calculate_z(x, y)}")


if __name__ == "__main__":
    main()
