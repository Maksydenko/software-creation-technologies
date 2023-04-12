import os
from tabulate import tabulate


class Persons:
    def __init__(self, file_path):
        try:
            with open(file_path, encoding="utf-8") as file:
                persons = []
                # Skip empty lines
                for line in file:
                    if line == "\n":
                        continue
                    persons.append(line)
                self.persons = persons
                self.splitted_persons = self.split_lines(persons)

                # Paths
                self.file_path = file_path
                self.adults_path = "adults.txt"
                self.minors_path = "minors.txt"
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
            int(value)
            return True
        except ValueError:
            return False

    # Split the words of each line
    @staticmethod
    def split_lines(lines):
        # Delete \n
        lines = [line.rstrip() for line in lines]

        splitted_lines = []

        for line in lines:
            splitted_line = line.split()
            splitted_lines.append(splitted_line)
        return splitted_lines

    # Count the average from the list
    @staticmethod
    def count_average(list):
        len_list = len(list)
        sum = 0

        for number in list:
            sum += number
        average = sum / len_list
        return average

    # Create new files after deleting existing ones
    @staticmethod
    def delete_create(path, data):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        if len(data):
            with open(path, "w", encoding="utf-8") as file:
                file.writelines(data)

    # Read file and write the defined data to new files
    def sort_data(self):
            persons = self.persons
            splitted_persons = self.splitted_persons

            correct_persons = []
            adults = []
            minors = []

            for index in range(len(splitted_persons)):
                if len(splitted_persons[index]) == 4:
                    surname = splitted_persons[index][0]
                    name = splitted_persons[index][1]
                    salary = splitted_persons[index][2]
                    age = splitted_persons[index][3]
                    # Check each value of data line
                    if (self.is_float(surname) or self.is_float(name)) == False \
                            and self.is_float(salary) and self.is_int(age):
                        if self.is_int(age):
                            age = int(age)
                            # Check the correctness of age
                            if 0 > age > 123:
                                continue
                            elif age >= 18:
                                adults.append(persons[index])
                            else:
                                minors.append(persons[index])
                            correct_persons.append(persons[index])
                    else:
                        continue
                else:
                    continue
            self.delete_create(self.adults_path, adults)
            self.delete_create(self.minors_path, minors)
            return correct_persons

    # Count average salaries and ages
    def count_averages(self):
        correct_persons = self.sort_data()
        splitted_persons = self.split_lines(correct_persons)

        salaries = []
        ages = []

        for line in splitted_persons:
            salary = int(line[2])
            salaries.append(salary)

            age = int(line[3])
            ages.append(age)
        average_salary = self.count_average(salaries)
        average_age = self.count_average(ages)
        average_age = round(average_age)
        return average_salary, average_age

    def __str__(self):
        correct_persons = self.sort_data()
        splitted_persons = self.split_lines(correct_persons)

        # Lengths
        len_persons = len(self.persons)
        len_correct_persons = len(correct_persons)

        # Try get data from file
        try:
            with open(self.adults_path, encoding="utf-8") as file:
                adults = file.readlines()
        except FileNotFoundError:
            adults = []

        # Try get data from file
        try:
            with open(self.minors_path, encoding="utf-8") as file:
                minors = file.readlines()
        except FileNotFoundError:
            minors = []

        # Values of header
        headers_value = ["Surname", "Name", "Salary", "Age"]

        # Try output table from file of adults
        if len(adults):
            splitted_adults = self.split_lines(adults)
            print(
                f"Adults:\n{tabulate(splitted_adults, headers=headers_value, tablefmt='grid')}")

        # Try output table from file of minors
        if len(minors):
            splitted_minors = self.split_lines(minors)
            print(
                f"Minors:\n{tabulate(splitted_minors, headers=headers_value, tablefmt='grid')}")

        # Try output table from file of all persons and averages salary and age
        if len_correct_persons:
            print(
                f"All persons:\n{tabulate(splitted_persons, headers=headers_value, tablefmt='grid')}")
            average_salary = self.count_averages()[0]
            average_age = self.count_averages()[1]
            print(
                f"Average salary: {average_salary}; average age: {average_age}")
        # The number of successful and all data
        return f"{len_correct_persons} / {len_persons} correct persons"
