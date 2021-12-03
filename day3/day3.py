import os
from typing import List


def most_common_bit(nums, bit_pos) -> str:
    ones_count = 0
    for num in nums:
        ones_count += int(num[bit_pos])
    if ones_count >= len(nums) / 2:
        return "1"
    else:
        return "0"


def least_common_bit(nums, bit_pos) -> str:
    ones_count = 0
    for num in nums:
        ones_count += int(num[bit_pos])
    if ones_count < len(nums) / 2:
        return "1"
    else:
        return "0"


def binary_to_dec(number: List[int]) -> int:
    dec = 0
    for index, bit in enumerate(number):
        if bit == "1":
            dec += pow(2, len(number) - index - 1)
    return dec


def oxygen_rating(nums, ones_count) -> int:
    bit_pos = 0
    size = len(nums)
    while len(nums) > 1:
        bit = most_common_bit(nums, bit_pos)
        nums = list(filter(lambda num: num[bit_pos] == bit, nums))
        bit_pos += 1
    o2_rating = binary_to_dec(nums[0])
    return o2_rating


def co2_rating(nums, ones_count) -> int:
    bit_pos = 0
    size = len(nums)
    while len(nums) > 1:
        bit = least_common_bit(nums, bit_pos)
        nums = list(filter(lambda num: num[bit_pos] == bit, nums))
        bit_pos += 1
    co2r = binary_to_dec(nums[0])
    return co2r


def main():
    input_list = []
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "./input.txt")
    ) as input_file:
        input_list = [line.strip() for line in input_file.readlines()]

    num_length = len(input_list[0])
    ones_count = [0 for i in range(num_length)]

    for num in input_list:
        for pos, digit in enumerate(num):
            ones_count[pos] += int(digit)

    gamma_list = ["1" if num > len(input_list) / 2 else "0" for num in ones_count]
    gamma_num = 0
    epsilon_num = 0

    for index, num in enumerate(gamma_list):
        if num == "1":
            gamma_num += pow(2, num_length - index - 1)
        else:
            epsilon_num += pow(2, num_length - index - 1)

    o2r = oxygen_rating(input_list, ones_count)
    co2r = co2_rating(input_list, ones_count)
    print(gamma_num * epsilon_num)
    print(o2r * co2r)


if __name__ == "__main__":
    main()
