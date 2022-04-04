def calculate_surface_area(a, b, c):
    return 2 * (a * b + a * c + b * c)


def calculate_volume(a, b, c):
    return a * b * c


def main():
    a = float(input("Unesite velicinu stranice a kvadra:"))
    b = float(input("Unesite velicinu stranice b kvadra:"))
    c = float(input("Unesite velicinu stranice c kvadra:"))
    assert calculate_surface_area(3, 4, 5) == 94.0
    assert calculate_volume(3, 4, 5) == 60.0
    print(f"Povrsina kvadra je: {calculate_surface_area(a, b, c)}")
    print(f"Zapremina kvadra je: {calculate_volume(a, b, c)}")


if __name__ == "__main__":
    main()
