import math


def calculate_distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def find_minimum_distance(x_values, y_values):
    if len(x_values) != len(y_values):
        raise ValueError("Number of x and y coordinates are not same !!!")
    result_points = [0, 1]
    distance = calculate_distance(x_values[0], x_values[1], y_values[0], y_values[1])
    for i in range(len(x_values)):
        """
        skip: 
        1. distance(Point_n-1, Point_n) = distance(Point_n, Point_n-1 ) comparison
        2. distance(Point_n, Point_n) = 0 comparison
        """
        for j in range(i + 1, len(y_values)):
            if calculate_distance(x_values[i], x_values[j], y_values[i], y_values[j]) < distance:
                distance = calculate_distance(x_values[i], x_values[j], y_values[i], y_values[j])
                result_points[0] = i
                result_points[1] = j
    return result_points


def main():
    # first example
    x_values = [21, 15, 10, 6, 3, 1, 0]
    y_values = [21, 15, 10, 6, 3, 1, 0]
    try:
        points = find_minimum_distance(x_values, y_values)
        print(f"The shortest distance is between Point({x_values[points[0]]},{y_values[points[0]]}) and "
              f"Point({x_values[points[1]]},{y_values[points[1]]})")
    except ValueError as e:
        print(e)

    # second example
    x_values = [9, 1, 5, 8]
    y_values = [5, 5, 8, 1]
    try:
        first_point = find_minimum_distance(x_values, y_values)[0]
        second_point = find_minimum_distance(x_values, y_values)[1]
        assert [(9, 5), (8, 1)] == [(x_values[first_point], y_values[first_point]),
                                    (x_values[second_point], y_values[second_point])]
        points = find_minimum_distance(x_values, y_values)
        print(f"The shortest distance is between Point({x_values[points[0]]},{y_values[points[0]]}) and "
              f"Point({x_values[points[1]]},{y_values[points[1]]})")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
