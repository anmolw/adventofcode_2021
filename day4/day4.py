from typing import List, Set, Tuple

CARD_ROWS = 5
CARD_COLS = 5


class BingoCard:
    def __init__(self, numbers: List[List[int]]):
        self._numbers = numbers
        self._won = False

    def mark_number(self, number: int) -> None:
        for i in range(CARD_ROWS):
            for j in range(CARD_COLS):
                if self._numbers[i][j] == number:
                    self._numbers[i][j] = -1

    def won_this_turn(self) -> bool:
        for i in range(CARD_ROWS):
            if self._row_is_complete(i):
                self._won = True
                return True
        for i in range(CARD_COLS):
            if self._col_is_complete(i):
                self._won = True
                return True
        return False

    def already_won(self) -> bool:
        return self._won

    def _row_is_complete(self, row: int) -> bool:
        for i in range(CARD_COLS):
            if self._numbers[row][i] != -1:
                return False
        return True

    def _col_is_complete(self, col: int) -> bool:
        for i in range(CARD_ROWS):
            if self._numbers[i][col] != -1:
                return False
        return True

    def calc_winning_score(self, last_number) -> int:
        sum = 0
        for i in range(CARD_ROWS):
            for j in range(CARD_COLS):
                if self._numbers[i][j] != -1:
                    sum += self._numbers[i][j]
        return sum * last_number


def get_input() -> List[str]:
    input_lines = []
    with open("input.txt", "r") as input_file:
        input_lines = list(
            map(
                lambda line: line.strip().replace("  ", " "),
                filter(lambda line: line != "\n", input_file.readlines()),
            )
        )
    return input_lines


def solve(input_lines) -> None:
    drawn_numbers = [int(num.strip()) for num in input_lines[0].split(",")]
    cards: List[BingoCard] = []
    i = 0
    while i < len(input_lines) - 1:
        card_numbers = []
        for row in range(CARD_ROWS):
            current_row = [
                int(num) for num in input_lines[i + row + 1].strip().split(" ")
            ]
            card_numbers.append(current_row)
        cards.append(BingoCard(card_numbers))
        i += CARD_ROWS

    num_drawn = 0
    last_to_win = 0
    winner_found = False

    for number in drawn_numbers:
        num_drawn += 1
        for card in filter(lambda card: not card.already_won(), cards):
            card.mark_number(number)
            if num_drawn >= 5 and card.won_this_turn():
                last_to_win = card.calc_winning_score(number)
                if not winner_found:
                    winner_found = True
                    print(last_to_win)

    print(last_to_win)


def main():
    input_lines = get_input()
    solve(input_lines)


if __name__ == "__main__":
    main()
