#!/usr/bin/python3

import os
import sys  # for command line arguments

from data import read_json
from algo import find_cycles


def main(json_file_path: str):
    if not os.path.exists(json_file_path):
        raise FileNotFoundError
    given_data = read_json(json_file_path)
    cycles = find_cycles(given_data)
    print(cycles)


if __name__ == "__main__":
    file_path = str(sys.argv[1])
    main(file_path)
