class Book:
    def __init__(self, book_title, book_author, book_category, book_id):
        # private attributes
        self.__title = book_title
        self.__author = book_author
        self.__category = book_category
        self.__id = book_id

     # method to print the book details

    def print_book_details(self):
        print(self.__title)
        print(self.__author)
        print(self.__category)
        print(self.__id)

    # getter for the title attribute

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author