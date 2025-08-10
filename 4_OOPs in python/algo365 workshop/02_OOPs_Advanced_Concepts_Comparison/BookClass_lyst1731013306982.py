"""
* -----------------------------------------------------------------------------
* 
* Copyright <2024> <algorithms365>
* 
* Professional Coding Skills Workshops
* 
* Licensed under the MIT License:
*  
* https://opensource.org/licenses/MIT
* 
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365 
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://in.linkedin.com/company/algorithms365
* 
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
* 
* -----------------------------------------------------------------------------
"""
from LibraryItemClass import LibraryItem

#Child class 
class Book(LibraryItem):
    def __init__(self, book_title, book_author, book_category, book_id, count, id):
        
        super().__init__(count, id)
        # Private attributes
        self.__title = book_title
        self.__author = book_author
        self.__category = book_category
        self.__id = book_id

    # Method to print book details
    def print_book_details(self):
        print(self.__title)
        print(self.__author)
        print(self.__category)
        print(self.__id)

    # Getter for the title attribute
    def get_title(self):
        return self.__title

    def search(self, title, author=None):
        if author:
            print(f"Searching by title and author: {title}, {author}")
        else:
            print(f"Searching by title: {title}")

    def check_out(self):
        print("Invoking checkout from child class Book")
        