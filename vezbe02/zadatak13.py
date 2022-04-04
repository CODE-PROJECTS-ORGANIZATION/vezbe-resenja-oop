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


def sum_of_elements_above_diagonal(matrix):
    sum_above_diagonal = 0
    rows = len(matrix)
    for i in range(rows):
        for j in range(len(matrix[i])):
            if j > i:
                sum_above_diagonal += matrix[i][j]
    return sum_above_diagonal


def main():
    rows = 7
    columns = 5
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)
    assert 50 == sum_of_elements_above_diagonal(matrix)
    print(f"Sum of elements above matrix A diagonal: {sum_of_elements_above_diagonal(matrix)}")


if __name__ == "__main__":
    main()
