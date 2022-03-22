import json

def load(path):
    with open(path) as file:
        return json.loads(file.read())

def main():
    map = load("resources\\test.json")
    for c in map['countries']:
        print(map[c])


if __name__ == "__main__":
    main()
