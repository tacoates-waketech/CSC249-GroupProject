#Menu.py
# This file will contain the main() and start the program

from CourseManager import CourseManager;
def main():
    manager = CourseManager()
    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Drop Course")
        print("3. List Enrolled Courses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            course = input("Enter the name of the course to add: ")
            manager.add_course(course)
        elif choice == '2':
            course = input("Enter the name of the course to drop: ")
            manager.drop_course(course)
        elif choice == '3':
            manager.list_courses()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()