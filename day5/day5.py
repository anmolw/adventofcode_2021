from typing import List


def get_input() -> List[str]:
    input_lines = []
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    return input_lines


def solve(input_lines: List[str], part2: bool = False):
    points = {}
    for line in input_lines:
        left, right = line.split("->")
        x1, y1 = map(lambda num: int(num), left.split(","))
        x2, y2 = map(lambda num: int(num), right.split(","))

        # Check if line is horizontal or vertical
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if not points.get((x, y)):
                        points[(x, y)] = 0
                    points[(x, y)] += 1

        # Check if the line has a slope of +/- 1
        elif part2 and abs((y1 - y2) / (x1 - x2)) == 1:
            xdiff = 1 if x2 > x1 else -1
            ydiff = 1 if y2 > y1 else -1
            x = x1
            y = y1
            while ((xdiff == 1 and x <= x2) or (xdiff == -1 and x >= x2)) and (
                (ydiff == 1 and y <= y2) or (ydiff == -1 and y >= y2)
            ):
                if not points.get((x, y)):
                    points[(x, y)] = 0
                points[(x, y)] += 1
                x += xdiff
                y += ydiff

    num_overlapping = 0
    for (x, y), num_lines in points.items():
        if num_lines > 1:
            num_overlapping += 1
    print(num_overlapping)


def main():
    input_lines = get_input()
    solve(input_lines)
    solve(input_lines, True)


if __name__ == "__main__":
    main()
