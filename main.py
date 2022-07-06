from data import read_json
from algo import find_cycles


def main():
    given_data = read_json("test1.json")
    cycles = find_cycles(given_data)
    print(cycles)


if __name__ == "__main__":
    main()
