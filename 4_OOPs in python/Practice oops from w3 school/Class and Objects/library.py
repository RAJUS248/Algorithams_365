# 🔹 Student Class
class Student:
    # Static/class variable
    count = 0

    def __init__(self, name=None, age=None, course=None, hometown=None):
        self.Name = name
        self.Age = age
        self.__Course = course       # Private attribute
        self.__ID = None             # Private attribute
        self._Hometown = hometown    # Protected attribute

        # Auto-register only if all data is provided
        if name and age and course and hometown:
            self.register()

    def get_name(self):
        return self.Name

    def get_age(self):
        return self.Age

    def get_course(self):
        return self.__Course

    def get_hometown(self):
        return self._Hometown

    def register(self):
        Student.count += 1
        self.__ID = Student.count
        return self.__ID

    def __update_name(self, name):  # Private method
        self.Name = name

    def _update_age(self, age):  # Protected method
        self.Age = age


# 🔹 Book Class
class Book:
    def __init__(self, book_title, book_author, book_category, book_id):
        self.__title = book_title
        self.__author = book_author
        self.__category = book_category
        self.__id = book_id

    def print_book_details(self):
        print(self.__title)
        print(self.__author)
        print(self.__category)
        print(self.__id)

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author


# 🔹 Book Management Class
class BookManagement:
    def checkout_book(self, student, book):
        print(f"Student {student.Name} is taking book '{book.get_title()}', Author: {book.get_author()}")
        return True

    def return_book(self, student, book):
        print(f"Student {student.Name} is returning book '{book.get_title()}'")
        return True


# 🔹 (Optional) Employee Class - Not used, just placeholder
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id


# 🔹 Main application logic showing how everything connects
def main():
    # 📌 Creating a student using default constructor
    new_student = Student()
    new_student.Name = "Raj"
    new_student.Age = 22
    new_student._Hometown = "Ramdurg"

    # Access student info using public getters
    print(f"Student name is {new_student.get_name()}")
    print(f"Student age is {new_student.get_age()}")
    print(f"Student hometown is {new_student.get_hometown()}")

    # 📌 Handling NoneType safely
    second_student = None
    if second_student is not None:
        second_student.Name = "Sita"  # Will not run

    # 📌 Creating another student with all fields (auto-register)
    second_student = Student("Rajat", 45, "Science", "Bengaluru")
    print(f"Student name is {second_student.get_name()}")
    print(f"Student age is {second_student.get_age()}")

    # 📌 Creating a book object
    book1 = Book("Python Programming", "Raju", "Coding", "B101")

    # 📌 BookManagement object to manage checkouts
    operations = BookManagement()
    
    # Book checkout and return operations
    operations.checkout_book(second_student, book1)
    operations.checkout_book(new_student, book1)

    operations.return_book(new_student, book1)


# 🔹 Run the app
if __name__ == "__main__":
    main()
