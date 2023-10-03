from models.university import University
from models.faculty import Faculty
from models.student import Student

class FileManager:
    FACULTY_FILE = "text_files/faculties.txt"
    STUDENT_FILE = "text_files/students.txt"



    def save(university):
        with open(FileManager.FACULTY_FILE, 'w') as faculty_file:
            for faculty in university.faculties:
                faculty_data = f"Faculty|{faculty.name}|{faculty.abbreviation}|{faculty.study_field.name}\n"
                faculty_file.write(faculty_data)
                
        with open(FileManager.STUDENT_FILE, 'w') as student_file:
            for faculty in university.faculties:
                for student in faculty.get_enrolled_students() + faculty.get_graduated_students():
                    student_data = f"Student|{faculty.abbreviation}|{student.first_name}|{student.last_name}|{student.email}|{student.enrollment_date}|{student.date_of_birth}|{student.graduated}\n"
                    student_file.write(student_data)

    def load():
        university = University()

        with open(FileManager.FACULTY_FILE, 'r') as faculty_file:
            lines = faculty_file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if data[0] == "Faculty":
                    faculty = Faculty(data[1], data[2], data[3])
                    university.add_faculty(faculty)
        
        with open(FileManager.STUDENT_FILE, 'r') as student_file:
            lines = student_file.readlines()

        for line in lines:
            data = line.strip().split('|')
            if data[0] == "Student":
                faculty_abbreviation = data[1]
                faculty = university.get_faculty_by_abbreviation(faculty_abbreviation)
                if faculty:
                    student = Student(data[2], data[3], data[4], data[5], data[6], True if data[7] == 'True' else False)
                    faculty.add_student(student)

        return university
