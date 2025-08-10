class BookManagement:

    def checkout_book(self,student,book):
        print(f"student {student.Name} is taking book {book.get_title()} the author is {book.get_author()}")
        return True
    
    def return_book(self, student , book):
        print(f"student {student.Name} is returbing book {book.get_title()}")
        return True