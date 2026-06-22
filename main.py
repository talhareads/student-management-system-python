import os

DATA_FILE = "students.txt"


def load_students():
    students = []
    if not os.path.exists(DATA_FILE):
        return students
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            student_id, name, grade = parts
            students.append({"id": student_id, "name": name, "grade": grade})
    return students


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for student in students:
            file.write(student['id'] + "|" + student['name'] + "|" + student['grade'] + "\n")


def add_student(students):
    student_id = input("Enter student ID: ").strip()
    if any(s["id"] == student_id for s in students):
        print("A student with that ID already exists.")
        return
    name = input("Enter student name: ").strip()
    grade = validate_grade("Enter student grade (0-100): ")
    students.append({"id": student_id, "name": name, "grade": grade})
    save_students(students)
    print("Student added successfully.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def validate_grade(prompt):
    while True:
        grade = input(prompt).strip()
        if grade.isdigit() and 0 <= int(grade) <= 100:
            return grade
        print("Invalid grade. Enter a value between 0 and 100.")


def update_student(students):
    student_id = input("Enter student ID: ").strip()
    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ").strip()
            student["grade"] = validate_grade("Enter new grade (0-100): ")
            save_students(students)
            print("Student updated successfully.")
            return
    print("Student not found.")


def search_student(students):
    query = input("Enter student ID or name to search: ").strip().lower()
    results = [s for s in students if query == s["id"].lower() or query in s["name"].lower()]
    if not results:
        print("No matching students found.")
        return
    print("Matching students:")
    for student in results:
        print("ID: " + student['id'] + ", Name: " + student['name'] + ", Grade: " + student['grade'])


def display_students(students):
    if not students:
        print("No students available.")
        return
    print("All students:")
    for student in students:
        print("ID: " + student['id'] + ", Name: " + student['name'] + ", Grade: " + student['grade'])


def show_menu():
    print("\n" + "=" * 35)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 35)
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Display All Students")
    print("5. Search Student")
    print("6. Exit")


def main():
    students = load_students()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()


