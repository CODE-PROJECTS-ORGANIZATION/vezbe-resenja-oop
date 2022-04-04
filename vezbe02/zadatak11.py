def generate_sequence(sequence_a, sequence_b):
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must be same length !!!")
    sequence_result = []
    for i in range(len(sequence_a)):
        if i % 2 == 0:
            sequence_result.append(sequence_a[i] + sequence_b[len(sequence_b) - 1 - i])
        else:
            sequence_result.append(sequence_a[i] * sequence_b[len(sequence_b) - 1 - i])
    return sequence_result


def main():
    sequence_a = [1, 2, 3, 4, 5]
    sequence_b = [10, 20, 30, 40, 50]
    assert [51, 80, 33, 80, 15] == generate_sequence(sequence_a, sequence_b)
    try:
        sequence_c = generate_sequence(sequence_a, sequence_b)
        print("Generated sequence:", sequence_c)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
