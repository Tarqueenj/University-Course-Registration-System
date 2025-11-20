University Course Registration System

Project Description

This project implements a University Course Registration System in Python. The system allows managing students, lecturers, courses, and performance evaluation. It includes both an original implementation and a refactored version that improves code maintainability and design quality.

The system demonstrates:

- Object-Oriented Programming concepts (Person, Student, Lecturer, Course, Registrar)
- Course registration and enrollment
- Lecturer assignment and grading
- Student performance calculation (GPA and attendance)
- Reporting for students, lecturers, and courses

Authors

1.	TARQUEEN JEPKOECH – INTE/MG/3289/09/22

2.	OGORO GESARE EUVINE- INTE/MG/2948/09/22

3.	SPELLY LETICIA- INTE/MG/1256/09/22

4.	KURGAT CLEON- INTE/MG/3032/09/22

Files

- University_Course_Registration_System.py – Original implementation
- University_Course_Registration_System_Refactored.py – Refactored version with improved design, cohesion, and reduced coupling
- README.md – Project documentation

Features

- Student Registration: Add students and allow them to register for courses.
- Course Management: Create courses and enroll students.
- Lecturer Management: Assign lecturers to courses and submit grades.
- Performance Evaluation: Compute GPA and attendance rates for students.
- Full Report: Generate a full report showing course details, enrolled students, lecturer assignments, and student performance.

How to Run

1. Clone or download the repository.
2. Ensure Python 3.x is installed on your system.
3. Run the original system:
   python University_Course_Registration_System.py
4. Run the refactored system:
   python University_Course_Registration_System_Refactored.py

Improvements in Refactored Version

- Reduced Cyclomatic Complexity in student performance calculations.
- Improved cohesion by separating GPA and attendance calculations into helper methods.
- Reduced coupling between Student, Course, and Lecturer.
- Simplified class responsibilities and encapsulated behavior.
- Easier to maintain, extend, and test.

Contact

For questions or contributions, contact the project authors listed above.
