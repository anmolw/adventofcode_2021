from typing import List


def get_input() -> List[str]:
    input_lines = []
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    return input_lines


def solve(input_lines: List[str]) -> None:
    positions = [int(pos) for pos in input_lines[0].strip().split(",")]
    positions_visited = set()
    min_fuel = -1
    for pos in positions:
        if not pos in positions_visited:
            positions_visited.add(pos)
            total_fuel = 0
            for origin in positions:
                total_fuel += abs(origin - pos)
            if min_fuel == -1:
                min_fuel = total_fuel
            else:
                min_fuel = min(min_fuel, total_fuel)

    print(min_fuel)


def part2(input_lines: List[str]) -> None:
    positions = [int(pos) for pos in input_lines[0].strip().split(",")]
    min_fuel = -1
    for pos in range(min(positions), max(positions) + 1):
        total_fuel = 0
        for origin in positions:
            dist = abs(origin - pos)
            total_fuel += (dist * (dist + 1)) // 2
        if min_fuel == -1:
            min_fuel = total_fuel
        else:
            min_fuel = min(min_fuel, total_fuel)

    print(min_fuel)


def main() -> None:
    input_lines = get_input()
    solve(input_lines)
    part2(input_lines)


if __name__ == "__main__":
    main()
