from models.study_field import StudyField

class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        try:
            self.study_field = StudyField[study_field]
        except KeyError:
            raise ValueError(f"Invalid study field: {study_field}")
        self.enrolled_students = []
        self.graduated_students = []

    def add_student(self, student):
        if student.graduated:
            self.graduated_students.append(student)
        else:
            self.enrolled_students.append(student)

    def validate_student_graduation(self, student):
        if student in self.graduated_students:
            print(f"{student.first_name} {student.last_name} has already graduated from {self.abbreviation}.")
            return False
        elif student in self.enrolled_students:
            self.enrolled_students.remove(student)
            self.graduated_students.append(student)
            student.graduated = True
            print(f"Student {student.first_name} {student.last_name} has graduated from {self.abbreviation}.")
            return True
        else:
            print(f"{student.first_name} {student.last_name} is not enrolled in {self.name}.")
            return False


    def get_enrolled_students(self):
        return self.enrolled_students

    def get_graduated_students(self):
        return self.graduated_students

    def check_student_belongs(self, email):
        return any(student.email == email for student in self.enrolled_students + self.graduated_students)

    def __repr__(self):
        return f"Name: {self.name}, Abbreviation: ({self.abbreviation}), Study Field: {self.study_field.name}"

