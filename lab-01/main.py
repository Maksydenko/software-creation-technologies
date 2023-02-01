class Person:
    def __init__(self, path_file):
        try:
            with open(path_file, encoding="utf-8") as file:
                self.path_file = path_file
                self.persons = file.readlines()
        except FileNotFoundError as fnfe:
            print(fnfe)

    # Check whether the value can be the float
    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Check whether the value can be the int
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

    @staticmethod
    def count_average(list):
        len_list = len(list)
        sum = 0

        for number in list:
            sum += number
        average = sum / len_list
        return average

    def read_data(self):
        with open(self.path_file, encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            correct_persons = []
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
                            correct_persons.append(line + "\n")
                    else:
                        continue
                else:
                    continue
            return correct_persons, adults, minors

    def write_data(self):
        adults = self.read_data()[0]
        minors = self.read_data()[1]

        if len(adults):
            with open("adults.txt", "w", encoding="utf-8") as file:
                file.writelines(adults)
        if len(minors):
            with open("minors.txt", "w", encoding="utf-8") as file:
                file.writelines(minors)

    def count_averages(self):
        correct_persons = self.read_data()[0]
        splitted_persons = self.split_lines(correct_persons)

        salaries = []
        ages = []

        for line in splitted_persons:
            salary = line[2]
            salary = int(salary)
            salaries.append(salary)

            age = line[3]
            age = int(age)
            ages.append(age)
        average_salary = self.count_average(salaries)
        average_age = self.count_average(ages)
        average_age = round(average_age)
        return average_salary, average_age

    def __str__(self):
        from tabulate import tabulate

        persons = self.persons
        correct_persons = self.read_data()[0]

        len_persons = len(persons)
        len_correct_persons = len(correct_persons)

        adults = self.read_data()[1]
        minors = self.read_data()[2]

        splitted_persons = self.split_lines(correct_persons)
        splitted_adults = self.split_lines(adults)
        splitted_minors = self.split_lines(minors)

        headers_value = ["Surname", "Name", "Salary", "Age"]

        if len_correct_persons:
            average_salary = self.count_averages()[0]
            average_age = self.count_averages()[1]

        if len(correct_persons):
            print(
                f"All persons:\n{tabulate(splitted_persons, headers=headers_value, tablefmt='grid')}")
        if len(adults):
            print(
                f"Adults:\n{tabulate(splitted_adults, headers=headers_value, tablefmt='grid')}")
        if len(minors):
            print(
                f"Minors:\n{tabulate(splitted_minors, headers=headers_value, tablefmt='grid')}")
        if len_correct_persons:
            print(f"salary: {average_salary}; average age: {average_age}")
        return f"{len_correct_persons} / {len_persons} correct persons"


test = Person("lab-01/persons.txt")
print(test)
