class University:
    def __init__(self):
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def email_exists(self, email):
        for faculty in self.faculties:
            for student in faculty.enrolled_students + faculty.graduated_students:
                if student.email == email:
                    return True
        return False

    def get_faculty_by_abbreviation(self, abbreviation):
        for faculty in self.faculties:
            if faculty.abbreviation == abbreviation:
                return faculty
        return None

    def get_student_and_faculty_by_email(self, email):
        for faculty in self.faculties:
            for student in faculty.enrolled_students + faculty.graduated_students:
                if student.email == email:
                    return student, faculty
        return None, None
