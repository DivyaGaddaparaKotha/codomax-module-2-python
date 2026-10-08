import csv
import json
import os

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

FIELDS = ["ID", "Name", "Age", "Course", "CGPA"]


# -------------------------------
# INITIALIZE FILES
# -------------------------------

def initialize_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump([], file, indent=4)


# -------------------------------
# READ ALL STUDENTS
# -------------------------------

def load_students():
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


# -------------------------------
# SAVE STUDENTS TO CSV
# -------------------------------

def save_to_csv(students):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


# -------------------------------
# SAVE STUDENTS TO JSON
# -------------------------------

def save_to_json(students):
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)


# -------------------------------
# CREATE
# -------------------------------

def add_student():
    student = {
        "ID": input("Enter Student ID: "),
        "Name": input("Enter Name: "),
        "Age": input("Enter Age: "),
        "Course": input("Enter Course: "),
        "CGPA": input("Enter CGPA: ")
    }

    students = load_students()

    # Check duplicate ID
    for existing_student in students:
        if existing_student["ID"] == student["ID"]:
            print("Student ID already exists!")
            return

    students.append(student)

    save_to_csv(students)
    save_to_json(students)

    print("\nStudent added successfully!")


# -------------------------------
# READ
# -------------------------------

def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print(
            f"ID: {student['ID']} | "
            f"Name: {student['Name']} | "
            f"Age: {student['Age']} | "
            f"Course: {student['Course']} | "
            f"CGPA: {student['CGPA']}"
        )


# -------------------------------
# UPDATE
# -------------------------------

def update_student():
    student_id = input("Enter Student ID to update: ")

    students = load_students()
    found = False

    for student in students:

        if student["ID"] == student_id:

            print("\nEnter new details:")

            student["Name"] = input("Enter Name: ")
            student["Age"] = input("Enter Age: ")
            student["Course"] = input("Enter Course: ")
            student["CGPA"] = input("Enter CGPA: ")

            found = True
            break

    if found:
        save_to_csv(students)
        save_to_json(students)

        print("\nStudent updated successfully!")

    else:
        print("\nStudent ID not found.")


# -------------------------------
# DELETE
# -------------------------------

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    students = load_students()

    new_students = [
        student for student in students
        if student["ID"] != student_id
    ]

    if len(new_students) == len(students):
        print("\nStudent ID not found.")
        return

    save_to_csv(new_students)
    save_to_json(new_students)

    print("\nStudent deleted successfully!")


# -------------------------------
# MAIN MENU
# -------------------------------

def main():

    initialize_files()

    while True:

        print("\n======================================")
        print("   STUDENT RECORD MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                update_student()

            elif choice == "4":
                delete_student()

            elif choice == "5":
                print("\nThank you for using the system!")
                break

            else:
                print("\nInvalid choice. Please enter 1-5.")

        except (ValueError, FileNotFoundError, PermissionError) as error:
            print(f"\nError: {error}")

        except Exception as error:
            print(f"\nUnexpected error: {error}")


# -------------------------------
# PROGRAM START
# -------------------------------

if __name__ == "__main__":
    main()