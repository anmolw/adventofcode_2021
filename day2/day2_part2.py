def get_input() -> list:
    with open("./input.txt", "r") as input_file:
        input_list = [line.strip() for line in input_file.readlines()]
        return input_list


def solve(input_list: list[str]):
    aim = 0
    horizontal_pos = 0
    depth = 0
    for line in input_list:
        (direction, magnitude) = line.split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal_pos += magnitude
            depth += aim * magnitude
        elif direction == "up":
            aim -= magnitude
        else:
            aim += magnitude
    print(horizontal_pos * depth)


def main():
    input_list = get_input()
    solve(input_list)


main()