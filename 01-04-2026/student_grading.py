class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        else:
            return "C"


students = [
    Student("Parashuram", 95),
    Student("Vilas", 75),
    Student("Nagendra", 60)
]

for s in students:
    print(s.name, s.calculate_grade())