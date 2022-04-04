def convert(length):
    m = length // 100
    dm = (length % 100) / 10
    return m, dm


def main():
    length = float(input("Unesite duzinu u cm:"))
    print(f"Uneta duzina iznosi: {convert(length)[0]} m i {convert(length)[1]} dm")
    assert (3, 2.4) == convert(324)


if __name__ == "__main__":
    main()
