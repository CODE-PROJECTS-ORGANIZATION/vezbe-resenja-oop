import math


def count_quarters_for(start, end, step):
    # number of decimals -> "0.25" -> "25" -> len("25") -> 2
    number_of_decimals = len(str(step).strip().split(".")[1])
    # Increase the magnitude for the loop and then reduce it when you need it.
    start = int(start * math.pow(10, number_of_decimals))
    end = int(end * math.pow(10, number_of_decimals))
    step = int(step * math.pow(10, number_of_decimals))
    counter = 0
    for i in range(start, end, step):
        print(i / math.pow(10, number_of_decimals), end=" ")
        counter += 1
    print()
    return counter


def count_quarters_while(lower_bound, upper_bound, step):
    counter = 0
    while lower_bound < upper_bound:
        lower_bound += step
        counter += 1
    return counter


def count_quarters_generators(start, end, step):
    while start < end:
        yield start
        start += step


def main():
    # [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]
    start = -1
    end = 1.5
    step = 0.25
    print(f"Number of quarters between {start} and {end} is: {count_quarters_for(start, end, step)}")
    print(f"Number of quarters between {start} and {end} is: {count_quarters_while(start, end, step)}")
    print(f"Number of quarters between {start} and {end} is: {len(list(count_quarters_generators(start, end, step)))}")


if __name__ == "__main__":
    main()
