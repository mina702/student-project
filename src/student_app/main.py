import json
from pathlib import Path

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, API_KEY
from student_app.logger import logger
from student_app.models.student import Student
from student_app.reports.student_report import display_report
from student_app.services.calculator import calculate_grade
from student_app.utils.validation import validate_name, validate_marks

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "student.json"


def load_student():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def show_config():
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")
    print(f"API key loaded: {API_KEY is not None}")  # only True/False, never the key


def show_json_student():
    data = load_student()
    print("\nStudent Information (from JSON)")
    print("-------------------------------")
    print(f"ID: {data['id']}")
    print(f"Name: {data['name']}")
    print(f"Program: {data['program']}")
    print(f"Semester: {data['semester']}")
    print(f"Marks: {data['marks']}")
    grade = calculate_grade(data["marks"])
    display_report(Student(data["name"], data["marks"], grade, data["id"]))


def read_student_from_user():
    name = input("\nEnter student name: ")
    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return None

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered (not a number)")
        print("Error: Marks must be a number.")
        return None

    if not validate_marks(marks):
        logger.warning(f"Invalid marks entered: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return None

    return Student(name, marks, calculate_grade(marks))


def main():
    logger.info("Application started")
    show_config()
    show_json_student()
    student = read_student_from_user()
    if student is not None:
        display_report(student)
        logger.info(f"Report generated for {student.name}")


if __name__ == "__main__":
    main()
