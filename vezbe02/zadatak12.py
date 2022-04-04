def generate_2d_matrix(rows, columns):
    matrix = []
    row = []
    counter = 1
    for i in range(rows):
        for j in range(columns):
            row.append(counter * counter)
        matrix.append(row)
        row = []
        counter += 1
    return matrix


def print_2d_matrix(matrix):
    rows = len(matrix)
    print("Matrica A je oblika:")
    for i in range(rows):
        for j in range(len(matrix[i])):
            print(f"\t\t{matrix[i][j]}", end=" ", sep="\t")
        print(end="\n")





def main():
    rows = int(input("Enter rows number:"))
    columns = int(input("Enter columns number:"))
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)


if __name__ == "__main__":
    main()
