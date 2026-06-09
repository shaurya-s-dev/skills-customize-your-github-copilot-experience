"""Starter Code: Fix the Broken Gradebook"""

import csv

GRADEBOOK_FILE = "grades.csv"


def load_grades(file_path):
    students = []

    with open("gradebook.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            score = row["score"]
            students.append({"name": name, "score": score})

    return students


def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


def main():
    students = load_grades(GRADEBOOK_FILE)

    print("Student scores:")
    for student in students:
        print(student["name"] + ": " + student["score"])

    print("Average score:", calculate_average(students))
    print("Highest score:", max(students))
    print("Lowest score:", min(students))


if __name__ == "__main__":
    main()
