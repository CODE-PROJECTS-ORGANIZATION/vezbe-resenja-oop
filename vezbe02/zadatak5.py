def calculate_product():
    product = 1
    for i in range(10, 21):
        if i % 2 == 0:
            product *= i
    return product


def main():
    assert 10*12*14*16*18*20 == calculate_product()
    print(calculate_product())


if __name__ == "__main__":
    main()
