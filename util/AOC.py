class AOC:
    def __init__(self):
        pass

    def read_input(self, file_path: str) -> list:
        with open(file_path, 'r') as file:
            data = file.read().split('\n')
            return data

if __name__ == "__main__":
    util = Util()