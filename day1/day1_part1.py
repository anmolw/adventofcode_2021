def get_input() -> list:
    with open("./input.txt", "r") as input_file:
        input_list = [int(line) for line in input_file.readlines()]
        return input_list


def solve(input_list: list) -> int:
    count = 0
    for (i, val) in enumerate(input_list):
        if i > 0 and input_list[i - 1] < val:
            count += 1
    return count


def main():
    input_list = get_input()
    ans = solve(input_list)
    print(ans)


main()