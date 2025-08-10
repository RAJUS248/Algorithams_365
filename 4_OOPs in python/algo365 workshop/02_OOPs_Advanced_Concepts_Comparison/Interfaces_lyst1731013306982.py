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
from abc import ABC, abstractmethod

# Interface for borrowable items
class Borrowable(ABC):
    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

# Interface for reservable items
class Reservable(ABC):
    @abstractmethod
    def reserve(self):
        pass

# Class implementing both interfaces
class Book(Borrowable, Reservable):
    def __init__(self, title):
        self.title = title

    def check_out(self):
        print(f"Checking out book: {self.title}")

    def return_item(self):
        print(f"Returning book: {self.title}")

    def reserve(self):
        print(f"Reserving book: {self.title}")

# Example usage
book = Book("Python Crash Course")
book.check_out()
book.return_item()
book.reserve()
