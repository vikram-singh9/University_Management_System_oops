# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


# Student class inheriting from Personxcxccxcvxvxvxvxvxvx
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.courses = []

    def reg_for_course(self, course_name):
        self.courses.append(course_name)


# Instructor class inheriting from Person
class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assign_course(self, course_name):
        self.courses.append(course_name)


# Course class
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []
        self.instructors = []

    def add_student(self, student):
        self.students.append(student)

    def set_instructor(self, instructor):
        self.instructors.append(instructor)


# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

# =====================
# Create some objects
# =====================

# Create department
department = Department('Computer Science')

# Create course and add to department
course = Course(101, ['Python Programming', 'Data Structures', 'Algorithms'])
department.add_course(course)

# Create student and register for course
student = Student('Ahsan', 20, 1234)
student.reg_for_course(course.name)  # student ke object me add hoga
course.add_student(student)          # course ke object me add hoga

# Create instructor and assign to course
instructor = Instructor('Ali', 30, 50000)
instructor.assign_course(course.name)
course.set_instructor(instructor)

# =====================
# Print the system info
# =====================

print(f"Department: {department.name}")
print(f"Courses in Department:")
for c in department.courses:
    print(f" - {c.name}")

print(f"\nCourse: {course.name}")
print(f"Students Registered:")
for s in course.students:
    print(f" - {s.get_name()} (Roll: {s.roll_number})")

print(f"Instructors Teaching:")
for i in course.instructors:
    print(f" - {i.get_name()} (Salary: {i.salary})")
