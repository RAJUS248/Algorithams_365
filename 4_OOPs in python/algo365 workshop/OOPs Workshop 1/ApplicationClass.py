from StudentClass import Student
from BookClass import Book
from BookManagemengtClass import BookManagement
from EmployeeClass import Employee


# Main application logic
def main():
    demo = 5  # creating an integer object and assigning the value 5

    # Declaring the variable new_student and creating an object of type Student 
    new_student = Student()  # Dynamic memory allocation

    # Access the public variables of the class and update values 
    new_student.Name = "Raj"
    new_student.Age = 22
    new_student._Hometown = "ramdurg"

    # new_student.ID = 1  # You can't access private variable like this

    # Access or invoke public methods of the class for the object new_student
    print(f"Student name is {new_student.get_name()}")
    print(f"Student age is {new_student.get_age()}")
    print(f"student hometown is {new_student.get_hometown()}")

    # new_student.update_name("Sita")  # You can't access private method like this

    # Handling NoneType (similar to NullPointerException)
    second_student = None
    if second_student is not None:
        second_student.Name = "Sita"  # Dead code, this will never be executed

    # Creating another student object with constructor taking input
    second_student = Student("Rajat", 45, "Science", "Bengaluru")
    print(f"Student name is {second_student.get_name()}")
    print(f"Student age is {second_student.get_age()}")

    operations = BookManagement()
    book1 = Book("Python", "Raju", "Coding", "1")

    operations.checkout_book(second_student, book1)
    operations.checkout_book(new_student, book1)

    operations.return_book(new_student, book1)


# Run the application
if __name__ == "__main__":
    main()
