def generate_2d_matrix(rows, columns):
    matrix = []
    row = []
    for i in range(rows):
        for j in range(columns):
            row.append(j + i)
        matrix.append(row)
        row = []
    return matrix


def print_2d_matrix(matrix):
    rows = len(matrix)
    print("Matrica A je oblika:")
    for i in range(rows):
        for j in range(len(matrix[i])):
            print(f"\t\t{matrix[i][j]}", end=" ", sep="\t")
        print(end="\n")


def sum_of_diagonal_elements(matrix):
    sum_diagonal = 0
    rows = len(matrix)
    for i in range(rows):
        for j in range(len(matrix[i])):
            if i == j:
                sum_diagonal += matrix[i][j]
    return sum_diagonal


def main():
    rows = 7
    columns = 5
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)
    print(f"Sum of diagonal elements of matrix A: {sum_of_diagonal_elements(matrix)}")


if __name__ == "__main__":
    main()
