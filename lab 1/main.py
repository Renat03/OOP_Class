from models.university import University
from models.faculty import Faculty
from models.study_field import StudyField
from models.student import Student


class ApplicationLoop:
    def __init__(self):
        self.university = University()
        self.command = ""

    def print_main_menu(self):
        print('''Welcome to TUM's student management system!\nWhat do you want to do?
    g - General operations
    f - Faculty operations
              
    q - Quit Program''')
        
    def print_general_menu(self):
        print('''General Operations:
    nf/<faculty name>/<faculty abbreviation>/<field> - Create a new faculty
    ss/<email> - Search which faculty a student belongs to by his email
    df - Display faculties
    df/<field> - Display faculties of a field
              
    b - Back to main menu''')
        
    def print_faculty_menu(self):
        print('''Faculty Operations:
    ns/<faculty abbreviation>/<first name>/<last name>/<email>/<day>/<month>/<year> - Create student
    gs/<email> - Graduate student
    ds/<faculty abbreviation> - Display enrolled students
    dg/<faculty abbreviation> - Display graduated students
    bf/<faculty abbreviation>/<email> - check if student belongs to faculty

    b - Back to main menu
''')
    
    def run(self):
        self.print_main_menu()
        while self.command != 'q':
            self.command = input("Main Menu> ")
            if self.command == 'g':
                self.general_operations()
            elif self.command == 'f':
                self.faculty_operations()
            elif self.command == 'q':
                print("Exiting the program.")
            else:
                print("Invalid command")

    def general_operations(self):
        self.print_general_menu()
        command = ""
        while command != 'b':
            command = input("General Menu> ")
            commands_list = command.split("/")
            if commands_list[0] == 'nf':
                self.create_faculty(commands_list)
            elif commands_list[0] == 'df':
                self.display_faculties(commands_list)
            elif commands_list[0] == 'ss':
                self.ss_search_student_faculty(commands_list)
            elif command == 'b':
                print("Going back to main menu.")
            else:
                print("Invalid command")

    def faculty_operations(self):
        self.print_faculty_menu()
        command = ""
        while command != 'b':
            command = input("Faculty Menu> ")
            commands_list = command.split("/")
            if commands_list[0] == 'ns':
                self.create_student(commands_list)
            elif commands_list[0] == 'gs':
                self.graduate_student(commands_list)
            elif commands_list[0] == 'ds':
                self.display_enrolled_students(commands_list)
            elif commands_list[0] == 'dg':
                self.display_graduated_students(commands_list)
            elif commands_list[0] == 'bf':
                self.check_student_faculty(commands_list)
            elif command == 'b':
                print("Going back to main menu.")
            else:
                print("Invalid command")

    def create_faculty(self, commands):
        if len(commands) == 4:
            name, abbreviation, study_field = commands[1], commands[2], commands[3]

            faculty = Faculty(name, abbreviation, study_field)
            self.university.add_faculty(faculty)

            print(f"Faculty {name} has been added to the university.")
        else:
            print("Invalid command format for creating faculty")

    def ss_search_student_faculty(self, commands):
        if len(commands) == 2:
            email = commands[1]
            student_found = False
            
            for faculty in self.university.faculties:
                if faculty.check_student_belongs(email):
                    print(f"The student with email {email} belongs to {faculty.abbreviation} - {faculty.name}.")
                    student_found = True
                    break

            if not student_found:
                print(f"No faculty found for student with email {email}.")
        else:
            print("Invalid command format for searching student faculty")

    def display_faculties(self, commands):
        faculties = self.university.faculties
        
        if len(commands) > 1:
            field = commands[1]
            try:
                study_field = StudyField[field]
                faculties = [faculty for faculty in faculties if faculty.study_field == study_field]
            except KeyError:
                print(f"Invalid study field: {field}")
                return
        
        if faculties:
            print("The faculties the university has are:")
            for faculty in faculties:
                print(faculty)
        else:
            print("There have been no faculties provided or none match the specified field!")

    def create_student(self, commands):
        if len(commands) == 7:
            faculty_abbrev = commands[1]
            faculty = self.university.get_faculty_by_abbreviation(faculty_abbrev)

            if not faculty:
                print(f"No faculty found with abbreviation {faculty_abbrev}")
                return
            
            first_name, last_name, email = commands[2], commands[3], commands[4]

            if self.university.email_exists(email):
                print(f"The email {email} is already in use. Please use a different email.")
                return

            dob, enrollment_date = commands[5], commands[6]
            student = Student(first_name, last_name, email, enrollment_date, dob)
            faculty.add_student(student)

            print(f"Student {first_name} {last_name} has been added to {faculty_abbrev}.")
        else:
            print("Invalid command format for creating student")


    def graduate_student(self, commands):
        if len(commands) == 2:
            email = commands[1]
            student, faculty = self.university.get_student_and_faculty_by_email(email)

            if not student:
                print(f"No student found with email {email}")
                return
            
            faculty.graduate_student(student)
            print(f"Student {student.first_name} {student.last_name} has graduated from {faculty.abbreviation}.")
        else:
            print("Invalid command format for graduating student")

    def display_enrolled_students(self, commands):
        if len(commands) == 2:
            faculty_abbrev = commands[1]
            faculty = self.university.get_faculty_by_abbreviation(faculty_abbrev)

            if not faculty:
                print(f"No faculty found with abbreviation {faculty_abbrev}")
                return
            
            students = faculty.get_enrolled_students()
            print(f"Enrolled students in {faculty_abbrev}:")
            for student in students:
                print(student)
        else:
            print("Invalid command format for displaying enrolled students")

    def display_graduated_students(self, commands):
        if len(commands) == 2:
            faculty_abbrev = commands[1]
            faculty = self.university.get_faculty_by_abbreviation(faculty_abbrev)

            if not faculty:
                print(f"No faculty found with abbreviation {faculty_abbrev}")
                return
            graduates = faculty.get_graduated_students()
            print(f"Graduated students from {faculty_abbrev}:")
            for student in graduates:
                print(student)
        else:
            print("Invalid command format for displaying graduated students")


    def check_student_faculty(self, commands):
        if len(commands) == 3:
            faculty_abbrev = commands[1]
            email = commands[2]
            faculty = self.university.get_faculty_by_abbreviation(faculty_abbrev)
            
            if not faculty:
                print(f"No faculty found with abbreviation {faculty_abbrev}")
                return
            
            student_belongs = faculty.check_student_belongs(email)
            if student_belongs:
                print(f"The student with email {email} belongs to {faculty_abbrev}.")
            else:
                print(f"The student with email {email} does not belong to {faculty_abbrev}.")
        else:
            print("Invalid command format for checking student belongs to faculty")



if __name__ == "__main__":
    app = ApplicationLoop()
    app.run()
