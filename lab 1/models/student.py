class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, Email: {self.email}, DOB: {self.date_of_birth}, Enrolled: {self.enrollment_date}"
