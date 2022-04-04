from functools import reduce
from statistics import mean


def find_max_element(numbers):
    max_element = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_element:
            max_element = numbers[i]
    return max_element


def find_min_element(numbers):
    min_element = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_element:
            min_element = numbers[i]
    return min_element


def find_average(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers / len(numbers)


def find_average_reduce(numbers):
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    return sum_of_numbers / len(numbers)


def find_conditional_elements(numbers):
    result = []
    average = find_average(numbers)
    for number in numbers:
        if 0 < number < average:
            result.append(number)
    return result


def find_conditional_filter(numbers):
    return list(filter(lambda number: 0 < number < mean(numbers), numbers))


def main():
    numbers = [-10, 3, 16, 1, 4, -2]
    assert max(numbers) == find_max_element(numbers)
    print(f"Maximum element in a list:{find_max_element(numbers)}")

    assert min(numbers) == find_min_element(numbers)
    print(f"Minimum element in a list:{find_min_element(numbers)}")

    assert mean(numbers) == find_average(numbers)
    print(f"Average of all elements in a list:{find_average(numbers)}")

    assert mean(numbers) == find_average_reduce(numbers)
    print(f"Average of all elements in a list (reduce):{find_average_reduce(numbers)}")

    assert [1] == find_conditional_elements(numbers)
    print(f"All elements that are positive and smaller than average:{find_conditional_elements(numbers)}")

    assert [1] == find_conditional_filter(numbers)
    print(f"All elements that are positive and smaller than average (filter):{find_conditional_filter(numbers)}")


if __name__ == "__main__":
    main()
