from typing import List


def get_input() -> List[str]:
    input_lines = []
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    return input_lines


def part1(input_lines: List[str]) -> None:
    fish_list = [int(num) for num in input_lines[0].strip().split(",")]
    num_days = 80
    for day in range(num_days):
        newborn_fish = []
        for (index, fish) in enumerate(fish_list):
            if fish == 0:
                fish_list[index] = 6
                newborn_fish.append(8)
            else:
                fish_list[index] -= 1
        fish_list.extend(newborn_fish)
    print(len(fish_list))


def part2(input_lines: List[str]) -> None:
    fish_list = [int(num) for num in input_lines[0].strip().split(",")]
    count_list = [0 for _ in range(9)]

    for fish in fish_list:
        count_list[fish] += 1

    num_days = 256
    for day in range(num_days):
        newborn_fish = 0
        for index, count in enumerate(count_list):
            if index == 0:
                newborn_fish += count
            else:
                count_list[index - 1] += count
            count_list[index] -= count
        count_list[8] += newborn_fish
        count_list[6] += newborn_fish
    print(sum(count_list))


def main() -> None:
    input_lines = get_input()
    part1(input_lines)
    part2(input_lines)


if __name__ == "__main__":
    main()
