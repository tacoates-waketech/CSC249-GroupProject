#CourseManager.py
# This file will contain the UI

class CourseManager:
    def __init__(self):
        self.enrolled_courses = set()

    def add_course(self, course):
        if course in self.enrolled_courses:
            print("You are already enrolled in this course.")
        else:
            self.enrolled_courses.add(course)
            print(f"Successfully enrolled in {course}.")

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"Successfully dropped {course}.")
        else:
            print("You are not enrolled in this course.")

    def list_courses(self):
        if self.enrolled_courses:
            print("Courses you are enrolled in:")
            for course in self.enrolled_courses:
                print(course)
        else:
            print("You are not enrolled in any courses.")