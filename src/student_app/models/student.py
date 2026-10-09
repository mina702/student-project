class Student:
    def __init__(self, name, marks, grade, student_id=None):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.grade = grade

    def get_details(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "marks": self.marks,
            "grade": self.grade,
        }
