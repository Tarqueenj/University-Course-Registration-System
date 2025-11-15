from datetime import datetime

class Person:
    def __init__(self, person_id, name, email, phone=None):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = None

    def display_info(self):
        print(f"ID: {self.person_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}")

    def update_contact(self, email, phone):
        self.email = email
        self.phone = phone
        print(f"{self.name}'s contact updated.")

class Student(Person):
    def __init__(self, student_id, name, email, phone=None):
        super().__init__(student_id, name, email, phone)
        self.role = "Student"
        self.courses = []
        self.grades = {}
        self.attendance = {}
        self.last_login = datetime.now()

    def register_course(self, course):
        if course.code not in [c.code for c in self.courses]:
            self.courses.append(course)
            print(f"{self.name} registered for {course.title}")
        else:
            print(f"{self.name} already registered for {course.title}")

    def calculate_performance(self):
        total_points = 0
        for code, grade in self.grades.items():
            if grade == "A": total_points += 4
            elif grade == "B": total_points += 3
            elif grade == "C": total_points += 2
            elif grade == "D": total_points += 1
            elif grade == "E": total_points += 0
        gpa = round(total_points / len(self.grades), 2) if self.grades else 0

        attendance_rate = 0
        total_days = 0
        for course, records in self.attendance.items():
            total_days += len(records)
            attended = len([r for r in records if r])
            attendance_rate += (attended / len(records)) * 100 if records else 0
        avg_attendance = attendance_rate / len(self.attendance) if self.attendance else 0

        print(f"GPA: {gpa}, Attendance: {avg_attendance:.1f}%")
        if gpa >= 3.5 and avg_attendance >= 90:
            print("Excellent performance!")
        elif gpa < 2.0 or avg_attendance < 60:
            print("Warning: Poor performance")
        return gpa

class Course:
    def __init__(self, code, title, credit_hours, lecturer=None):
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        self.lecturer = lecturer
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        student.register_course(self)
        print(f"{student.name} added to {self.title}")

    def display_details(self):
        print(f"{self.code}: {self.title}, Credits: {self.credit_hours}, Lecturer: {self.lecturer.name if self.lecturer else 'TBA'}")
        print("Enrolled students:")
        for s in self.students:
            print(f"- {s.name}")

class Lecturer(Person):
    def __init__(self, staff_id, name, email, department):
        super().__init__(staff_id, name, email)
        self.role = "Lecturer"
        self.department = department
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.lecturer = self
            print(f"{self.name} assigned to {course.title}")

    def submit_grades(self, students, course_code, grade):
        for s in students:
            s.grades[course_code] = grade
            print(f"Assigned grade {grade} to {s.name} for {course_code}")

    def print_summary(self):
        print(f"Lecturer: {self.name}")
        for c in self.courses:
            print(f"Teaching: {c.title} ({len(c.students)} students)")

class Registrar:
    def __init__(self):
        self.students = []
        self.courses = []
        self.lecturers = []

    def add_student(self, s):
        self.students.append(s)
        print(f"Added student {s.name}")

    def add_course(self, c):
        self.courses.append(c)

    def add_lecturer(self, l):
        self.lecturers.append(l)

    def full_report(self):
        print("=== Full University Report ===")
        for c in self.courses:
            c.display_details()
        for l in self.lecturers:
            l.print_summary()
        for s in self.students:
            s.calculate_performance()

def main():
    reg = Registrar()

    c1 = Course("CS101", "Intro to Programming", 3)
    c2 = Course("CS201", "Data Structures", 4)

    l1 = Lecturer("L001", "Dr. Smith", "smith@uni.com", "CS")
    reg.add_lecturer(l1)

    s1 = Student("S001", "Alice", "alice@uni.com")
    s2 = Student("S002", "Bob", "bob@uni.com")
    reg.add_student(s1)
    reg.add_student(s2)

    l1.assign_course(c1)
    c1.enroll_student(s1)
    c1.enroll_student(s2)
    l1.submit_grades([s1, s2], "CS101", "A")

    s1.attendance["CS101"] = [True, True, False, True]
    s2.attendance["CS101"] = [True, False, True, False]

    reg.add_course(c1)
    reg.add_course(c2)
    reg.full_report()

if __name__ == "__main__":
    main()
