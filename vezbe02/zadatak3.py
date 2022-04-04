def generate_1d_matrix(n):
    result = []
    adder = 1
    for i in range(n):
        result.append(adder)
        adder += 10
    return result


def main():
    number = int(input("Enter number:"))
    print(generate_1d_matrix(number))


if __name__ == "__main__":
    main()
