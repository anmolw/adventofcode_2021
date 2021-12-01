def get_input() -> list:
    with open("./input.txt", "r") as input_file:
        input_list = [int(line) for line in input_file.readlines()]
        return input_list


def solve(input_list: list) -> int:
    count = 0
    # Store the sum of the last sliding window of size 3
    last_window_sum = 0
    # Initialize window_sum
    for i in range(0, 3):
        last_window_sum += input_list[i]
    # Loop through all other windows
    for i in range(1, len(input_list) - 2):
        current_window_sum = last_window_sum - input_list[i - 1] + input_list[i + 2]
        if current_window_sum > last_window_sum:
            count += 1
        last_window_sum = current_window_sum
    return count


def main():
    input_list = get_input()
    ans = solve(input_list)
    print(ans)


main()