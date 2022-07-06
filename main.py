from data import read_json


def main():
    given_data = read_json("test1.json")
    for name in given_data.keys():
        print(name, ": ", given_data[name])


if __name__ == "__main__":
    main()
