# Student Records System using Tuples
student_db = []

def add_student():
    id = int(input("Enter Id"))
    name = input("Enter name")
    branch = input("enter branch")
    year = int(input("Enter year"))
    record = (id,name,branch,year)
    student_db.append(record)

def display():
    if not student_db:
        print("No records available")

    for student in student_db:
        print(f"ID:{student[0]}, Name:{student[1]}, Branch:{student[2]}  year:{student[3]}")

def search_by_id():
    search_id = int(input("Enter ID to search: "))
    found = False
    for student in student_db:
        if student[0] == search_id:
            print(f"✅ Found: {student}")
            found = True
            break
    if not found:
        print("❌ Student not found.")

def main():
    while True:
        print("\n1. Add Student  2. Display All  3. Search by ID  4. Exit")
        choice = input("Choose an Option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display()

        elif choice == '3':
            search_by_id()

        elif choice == '4':
            print("exit")
            break
        else:
            print("Invalid choice")             
            return 
main()