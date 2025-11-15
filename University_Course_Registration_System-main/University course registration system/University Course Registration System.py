# University Course Registration System – Metrics-Based Refactoring

Course Title: Software Design and Quality Metrics  
Project Title: University Course Registration System – Metrics-Based Refactoring  
Group Members: 
1. TARQUEEN JEPKOECH - INTE/MG/3289/09/22
2. OGORO GESARE EUVINE- INTE/MG/2948/09/22
3. SPELLY LETICIA- INTE/MG/1256/09/22
4. KURGAT CLEON -  INTE/MG/3032/09/22

Date: 15/11/2025

Table of Contents

1. [Introduction](#1-introduction)  
2. [Part A: Metric Analysis](#2-part-a-metric-analysis)  
   - [2.1 Cyclomatic Complexity (CC)](#21-cyclomatic-complexity-cc)  
   - [2.2 Lines of Code (LOC)](#22-lines-of-code-loc)  
   - [2.3 Coupling Between Objects (CBO)](#23-coupling-between-objects-cbo)  
   - [2.4 Depth of Inheritance Tree (DIT)](#24-depth-of-inheritance-tree-dit)  
   - [2.5 Lack of Cohesion of Methods (LCOM)](#25-lack-of-cohesion-of-methods-lcom)  
   - [2.6 Problematic Areas](#26-problematic-areas)  
3. [Part B: Diagnosis](#3-part-b-diagnosis)  
4. [Part C: Refactoring](#4-part-c-refactoring)  
   - [4.1 Refactored Code](#41-refactored-code)  
   - [4.2 Post-Refactoring Metric Improvements](#42-post-refactoring-metric-improvements)  
5. [Conclusion](#5-conclusion)  
6. [References](#6-references)

---

# 1. Introduction

This report evaluates and refactors the University Course Registration System implemented in Python. The original design demonstrates several software engineering weaknesses such as high coupling, low cohesion, and high cyclomatic complexity. These issues can reduce maintainability, extensibility, and code readability.

Using object-oriented design metrics such as CK metrics (CBO, DIT, LCOM), Cyclomatic Complexity (CC), and Lines of Code (LOC), this analysis identifies problem areas, explains the implications of these metrics, and proposes refactoring solutions to improve design quality.

---

# 2. Part A: Metric Analysis

The system consists of five main classes:

- `Person`  
- `Student`  
- `Lecturer`  
- `Course`  
- `Registrar`  

and one procedural method: `main()`.

# 2.1 Cyclomatic Complexity (CC)

| Class/Method | Description | CC Value | Analysis |
|---------------|--------------|-----------|-----------|
| `Student.calculate_performance()` | Multiple conditionals and loops | **10** | High complexity; difficult to maintain and test. |
| `Registrar.full_report()` | Iterates through all entities, nested method calls | **6** | Moderate complexity; too many responsibilities. |
| `main()` | Instantiates and links multiple objects | 8 | High procedural dependency; violates modular design. |
| Other methods | Simple loops or conditionals | 1–3 | Acceptable complexity. |

> Threshold: CC > 10 is considered complex; ideal is ≤ 5 per method.

---

# 2.2 Lines of Code (LOC)

| Class | Total LOC | Problem Indicator |
|--------|------------|-------------------|
| `Student` | 55 | Long method (calculate_performance) contributes ~25 LOC. |
| `Registrar` | 40 | Overloaded with system-level orchestration. |
| `Course` | 35 | Acceptable. |
| `Lecturer` | 30 | Acceptable. |
| `Person` | 15 | Acceptable. |

> Methods exceeding **20 LOC** may reduce readability and increase defect probability.

---

# 2.3 Coupling Between Objects (CBO)

| Class | CBO Value | Description |
|--------|------------|-------------|
| `Registrar` | **4** | Highly coupled with Student, Course, and Lecturer classes. |
| `Student` | **3** | Depends on Course and Registrar indirectly. |
| `Lecturer` | **3** | Tightly coupled with Course and Student classes. |
| `Course` | **2** | Acceptable level of coupling. |

> High CBO (≥ 4) reduces modularity and complicates maintenance.

---

# 2.4 Depth of Inheritance Tree (DIT)

| Class | Parent Class | DIT |
|--------|---------------|----|
| `Person` | Object | 1 |
| `Student` | Person | 2 |
| `Lecturer` | Person | 2|
| Others | No inheritance | 1 |

> Moderate DIT (2) is good; higher values can increase complexity and reusability challenges.

---

# 2.5 Lack of Cohesion of Methods (LCOM)

| Class | LCOM | Analysis |
|--------|-------|----------|
| `Student` | **0.6 (Low Cohesion)** | Methods share too many unrelated responsibilities. |
| `Registrar` | **0.7 (Low Cohesion)** | Manages multiple entities; violates SRP. |
| `Course` | 0.3 | Good cohesion. |
| `Lecturer` | 0.4 | Moderate cohesion. |

> High LCOM (≥ 0.6) implies methods do not work toward a common goal.

---

# 2.6 Problematic Areas

1. `Student.calculate_performance()` 
   - High CC (10) and low cohesion.  
   - Combines GPA, attendance, and performance evaluation.

2. `Registrar.full_report()` 
   - Combines reporting for students, lecturers, and courses.  
   - High coupling and poor modularization.

3. `main()` 
   - Procedural structure violates separation of concerns.  
   - Should delegate operations to a controller or service class.

---

3. Part B: Diagnosis

 3.1 Interpretation of Metrics

- **High Cyclomatic Complexity (CC):**  
  Indicates excessive conditional logic and loops, reducing understandability and increasing the likelihood of logical errors.

- High CBO:
  The `Registrar` and `Student` classes are overly dependent on others, making changes in one class ripple through the system.

- **Low Cohesion (High LCOM):**  
  Methods in `Student` and `Registrar` handle unrelated concerns, reducing maintainability and reusability.

- High LOC: 
  Long methods such as `calculate_performance()` are difficult to test and prone to bugs.

# 3.2 Implications for Software Quality

| Quality Attribute | Impact |
|--------------------|---------|
| **Maintainability** | Decreases with high CC and CBO. |
| **Reusability** | Low cohesion and tight coupling reduce reusability of individual classes. |
| **Testability** | Complex control structures require more test cases. |
| **Extensibility** | System modifications become error-prone. |

---

 4. Part C: Refactoring

# Refactoring Objectives
- Reduce cyclomatic complexity by splitting large methods.  
- Reduce coupling between `Registrar`, `Student`, and `Course`.  
- Improve cohesion and encapsulation.

---

 4.1 Refactored Code

```python
from datetime import datetime

class Person:
    def __init__(self, person_id, name, email, phone=None):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        return f"ID: {self.person_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Student(Person):
    def __init__(self, student_id, name, email, phone=None):
        super().__init__(student_id, name, email, phone)
        self.courses = []
        self.grades = {}
        self.attendance = {}

    def register_course(self, course):
        if course.code not in [c.code for c in self.courses]:
            self.courses.append(course)
            print(f"{self.name} registered for {course.title}")

    def _calculate_gpa(self):
        grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
        total_points = sum(grade_points.get(g, 0) for g in self.grades.values())
        return round(total_points / len(self.grades), 2) if self.grades else 0

    def _calculate_attendance_rate(self):
        if not self.attendance:
            return 0
        total_rate = sum(
            (len([r for r in rec if r]) / len(rec)) * 100 for rec in self.attendance.values()
        )
        return round(total_rate / len(self.attendance), 1)

    def evaluate_performance(self):
        gpa = self._calculate_gpa()
        attendance = self._calculate_attendance_rate()
        print(f"GPA: {gpa}, Attendance: {attendance}%")
        if gpa >= 3.5 and attendance >= 90:
            print("Excellent performance!")
        elif gpa < 2.0 or attendance < 60:
            print("Warning: Poor performance")


class Course:
    def __init__(self, code, title, credit_hours):
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        self.lecturer = None
        self.students = []

    def assign_lecturer(self, lecturer):
        self.lecturer = lecturer
        lecturer.assign_course(self)

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            student.register_course(self)

    def get_summary(self):
        return f"{self.code} - {self.title} ({self.credit_hours} Credits)"


class Lecturer(Person):
    def __init__(self, staff_id, name, email, department):
        super().__init__(staff_id, name, email)
        self.department = department
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def grade_student(self, student, course_code, grade):
        student.grades[course_code] = grade


class Registrar:
    def __init__(self):
        self.students = []
        self.courses = []
        self.lecturers = []

    def register_student(self, student):
        self.students.append(student)

    def register_course(self, course):
        self.courses.append(course)

    def register_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def generate_report(self):
        print("=== University Report ===")
        for course in self.courses:
            print(course.get_summary())
        for student in self.students:
            student.evaluate_performance()
