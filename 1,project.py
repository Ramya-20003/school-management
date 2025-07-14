# Simple School Management System
#git init

students = {}

def add_student():
    student_id = input(" Enter Student ID: ")
    name = input(" Enter Name: ")
    grade = input(" Enter Grade: ")
    age = input(" Enter Age: ")
    students[student_id] = {"Name": name, "Grade": grade, "Age": age}
    print(f" Student '{name}' added successfully!\n")

def view_students():
    if not students:
        print(" No student records found.\n")
        return
    print(" Student Records:")
    for sid, info in students.items():
        print(f" ID: {sid} | Name: {info['Name']} | Grade: {info['Grade']} | Age: {info['Age']}")
    print()

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        name = input(" New Name: ")
        grade = input(" New Grade: ")
        age = input(" New Age: ")
        students[student_id] = {"Name": name, "Grade": grade, "Age": age}
        print(f" Student ID '{student_id}' updated successfully!\n")
    else:
        print(f" Student ID '{student_id}' not found.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print(f" Student ID '{student_id}' deleted successfully!\n")
    else:
        print(f" Student ID '{student_id}' not found.\n")

def main():
    while True:
        print("\n🎓 School Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option. Try again.\n")
main()
