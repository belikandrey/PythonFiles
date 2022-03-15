class Student:
    def __init__(self, firstname, lastname, mark):
        self.firstName = firstname
        self.lastName = lastname
        self.mark = mark

    def __str__(self):
        return self.firstName + " " + self.lastName + "\t" + str(
            self.mark)


class FileDoesNotExistException(Exception):
    def __init__(self, message="File With This Name Doesn't Exists"):
        super().__init__(message)


class BadLineException(Exception):
    def __init__(self, message="Bad Data In File"):
        super().__init__(message)


class FileIsEmptyException(Exception):
    def __init__(self, message="File Is Empty"):
        super().__init__(message)


def get_file_name():
    return input('Enter file name : ')


def process_file(filename):
    students = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                students.append(parse_student(line))
    except FileNotFoundError:
        raise FileDoesNotExistException
    if len(students) == 0:
        raise FileIsEmptyException
    return students


def parse_student(line):
    lines = line.split(' ')
    if len(lines) != 3:
        raise BadLineException
    s = Student(lines[0].strip(), lines[1].strip(), float(lines[2].strip()))
    if not validate_student(s):
        raise BadLineException
    return s


def validate_student(s):
    if not s.firstName or not s.lastName or not s.mark or s.mark <= 0:
        return False
    return True


def calculate_statistics(students):
    st = []
    for s in students:
        if any(elem.firstName == s.firstName and elem.lastName == s.lastName for elem in st):
            continue
        elems = list(filter(lambda x: x.firstName == s.firstName and x.lastName == s.lastName, students))
        mark = 0
        for el in elems:
            mark += el.mark
        st.append(Student(s.firstName, s.lastName, mark))
    return st


def sort_students(students):
    return sorted(students, key=lambda x: x.firstName + x.lastName, reverse=False)


def print_statistics(statistics):
    for s in statistics:
        print(s)


def run():
    filename = get_file_name()
    students = process_file(filename)
    statistics = sort_students(calculate_statistics(students))
    print_statistics(statistics)


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(str(e))
