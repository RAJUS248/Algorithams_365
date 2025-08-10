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
* LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
* 
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
* 
* -----------------------------------------------------------------------------
"""
class Book:
    def __init__(self, book_title, book_author, book_category, book_id):
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
