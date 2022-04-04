def generate_2d_matrix(rows, columns):
    matrix = []
    row = []
    counter = 1
    for i in range(rows):
        for j in range(columns):
            row.append(counter)
            counter += 1
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


def swap_diagonal_elements(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in range(len(matrix[i])):
            if i == j:
                """
                Prilikom zamene elemenata glavne i sporedne dijagonale red se ne menja (i = const) jedino sto se menja 
                je kolona (j). 
                """
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][rows - (i + 1)]
                matrix[i][rows - (i + 1)] = temp


def main():
    rows = 3
    columns = 3
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)
    swap_diagonal_elements(matrix)
    print_2d_matrix(matrix)
    print("=============================================")
    rows = 4
    columns = 4
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)
    swap_diagonal_elements(matrix)
    print_2d_matrix(matrix)
    print("=============================================")
    rows = 5
    columns = 5
    matrix = generate_2d_matrix(rows, columns)
    print_2d_matrix(matrix)
    swap_diagonal_elements(matrix)
    print_2d_matrix(matrix)


if __name__ == "__main__":
    main()
