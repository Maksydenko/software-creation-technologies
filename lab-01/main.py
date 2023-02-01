class Person:
    def __init__(self, path_file):
        try:
            with open(path_file, encoding="utf-8") as file:
                self.path_file = path_file
                self.persons = file.readlines()
        except FileNotFoundError as fnfe:
            print(fnfe)

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_int(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def split_lines(lines):
        lines = [line.rstrip() for line in lines]
        splitted_lines = []
        for line in lines:
            splitted_line = line.split()
            splitted_lines.append(splitted_line)
        return splitted_lines

    def read_data(self):
        with open(self.path_file, encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            adults = []
            minors = []

            for line in lines:
                splitted_line = line.split()

                if len(splitted_line) == 4:
                    surname = splitted_line[0]
                    name = splitted_line[1]
                    salary = splitted_line[2]
                    age = splitted_line[3]

                    if (self.is_float(surname) and self.is_float(name)) == False and self.is_float(salary) and self.is_float(age):
                        if self.is_int(age):
                            age = int(age)
                            if 0 > age > 123:
                                continue
                            elif age >= 18:
                                adults.append(line + "\n")
                            else:
                                minors.append(line + "\n")
                    else:
                        continue
                else:
                    continue
            return adults, minors

    def write_data(self):
        adults = self.read_data()[0]
        minors = self.read_data()[1]

        if len(adults):
            with open("adults.txt", "w", encoding="utf-8") as file:
                file.writelines(adults)
        if len(minors):
            with open("minors.txt", "w", encoding="utf-8") as file:
                file.writelines(minors)

    def __str__(self):
        from tabulate import tabulate

        persons = self.persons
        adults = self.read_data()[0]
        minors = self.read_data()[1]
        headers_value = ["Surname", "Name", "Salary", "Age"]

        if len(persons):
            print(
                f"All persons:\n{tabulate(self.split_lines(persons), headers=headers_value, tablefmt='grid')}")
            if len(adults):
                print(
                    f"Adults:\n{tabulate(self.split_lines(adults), headers=headers_value, tablefmt='grid')}")
            if len(minors):
                print(
                    f"Minors:\n{tabulate(self.split_lines(minors), headers=headers_value, tablefmt='grid')}")
        return f"Completed"