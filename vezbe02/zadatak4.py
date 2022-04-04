def print_2d_matrix(matrix):
    rows = len(matrix)
    print("Matrica A je oblika:")
    for i in range(rows):
        for j in range(len(matrix[i])):
            print(f"\t\t{matrix[i][j]}", end=" ", sep="\t")
        print(end="\n")


def main():
    matrix = [[1, 2, 3, 4], [5, 6], [7], [8, 9, 10], [11, 12, 13, 14, 15]]
    print_2d_matrix(matrix)


if __name__ == "__main__":
    main()
