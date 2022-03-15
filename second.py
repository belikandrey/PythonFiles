class FileDoesNotExistException(Exception):
    def __init__(self, message="File With This Name Doesn't Exists"):
        super().__init__(message)


class FileIsEmptyException(Exception):
    def __init__(self, message="File Doesn't Contain Latin Letters"):
        super().__init__(message)


def get_file_name():
    return input('Enter file name : ')


def process_file(filename):
    num_char = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                for char in line:
                    if not char.isalpha():
                        continue
                    char = char.lower()
                    num = num_char.get(char, 0)
                    num_char[char] = num + 1
    except FileNotFoundError:
        raise FileDoesNotExistException
    if len(num_char) == 0:
        raise FileIsEmptyException
    return num_char


def print_result(result):
    for key in result:
        print(key + '->' + str(result[key]))


def run():
    filename = get_file_name()
    result = process_file(filename)
    print_result({k: result[k] for k in sorted(result)})


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(str(e))
