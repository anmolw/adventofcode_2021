#!/usr/bin/env python3

from datetime import datetime
import requests
import json
import argparse
import os

parser = argparse.ArgumentParser(
    description="Get the input for a given day of advent of code"
)

parser.add_argument("day", type=int)
parser.add_argument("--year", type=int, default=datetime.now().year)
args = parser.parse_args()
day = args.day
year = args.year

cookies = ""

with open(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "cookie.json"), "r"
) as cookieFile:
    cookies = json.loads("".join(cookieFile.readlines()))

session = requests.session()
for key, value in cookies.items():
    session.cookies[key] = value

response = session.get(f"https://adventofcode.com/{year}/day/{day}/input")
with open(os.path.join(os.getcwd(), "input.txt"), "w") as outFile:
    outFile.write(response.text)