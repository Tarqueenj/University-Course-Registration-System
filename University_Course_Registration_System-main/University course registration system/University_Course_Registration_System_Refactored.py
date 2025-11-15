from datetime import datetime

class Person:
    def __init__(self, person_id, name, email, phone=None):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.phone = phone

class Student(Person):
    def __init__(self, student_id, name, email, phone=None):
        super().__init__(student_id, name, email, phone)
        self.courses = []
        self.grades = {}
        self.attendance = {}

    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def _calculate_gpa(self):
        points = {'A':4,'B':3,'C':2,'D':1,'E':0}
        return round(sum(points.get(g,0) for g in self.grades.values())/len(self.grades),2) if self.grades else 0

    def _attendance_rate(self):
        if not self.attendance: return 0
        return round(sum(len([r for r in rec if r])/len(rec)*100 for rec in self.attendance.values())/len(self.attendance),1)

    def evaluate_performance(self):
        gpa = self._calculate_gpa()
        attendance = self._attendance_rate()
        print(f"GPA: {gpa}, Attendance: {attendance}%")

class Course:
    def __init__(self, code, title, credit_hours):
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        self.lecturer = None
        self.students = []

    def assign_lecturer(self, lecturer):
        self.lecturer = lecturer
        lecturer.courses.append(self)

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            student.register_course(self)

class Lecturer(Person):
    def __init__(self, staff_id, name, email, department):
        super().__init__(staff_id, name, email)
        self.department = department
        self.courses = []

    def grade_student(self, student, course_code, grade):
        student.grades[course_code] = grade

class Registrar:
    def __init__(self):
        self.students = []
        self.courses = []
        self.lecturers = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def report(self):
        for course in self.courses:
            print(f"{course.code}: {course.title}, Credits: {course.credit_hours}, Lecturer: {course.lecturer.name if course.lecturer else 'TBA'}")
            for s in course.students:
                print(f"- {s.name}")
        for student in self.students:
            student.evaluate_performance()

def main():
    reg = Registrar()

    c1 = Course("CS101","Intro to Programming",3)
    c2 = Course("CS201","Data Structures",4)

    l1 = Lecturer("L001","Dr. Smith","smith@uni.com","CS")
    reg.add_lecturer(l1)

    s1 = Student("S001","Alice","alice@uni.com")
    s2 = Student("S002","Bob","bob@uni.com")
    reg.add_student(s1)
    reg.add_student(s2)

    c1.assign_lecturer(l1)
    c1.enroll(s1)
    c1.enroll(s2)
    l1.grade_student(s1,"CS101","A")
    l1.grade_student(s2,"CS101","A")

    s1.attendance["CS101"]=[True,True,False,True]
    s2.attendance["CS101"]=[True,False,True,False]

    reg.add_course(c1)
    reg.add_course(c2)
    reg.report()

if __name__=="__main__":
    main()
