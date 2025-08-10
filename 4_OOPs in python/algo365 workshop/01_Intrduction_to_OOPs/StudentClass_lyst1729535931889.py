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
class Student:
    # Static variable to count the number of students
    count = 0

    def __init__(self, name=None, age=None, course=None, hometown=None):
        # Initializing public and private attributes
        self.Name = name
        self.Age = age
        self.__Course = course  # Private attribute
        self.__ID = None
        self.Hometown = hometown 

        # If all arguments are passed, register the student
        if name and age and course and hometown:
            self.register()

    # Getters for the attributes
    def get_name(self):
        return self.Name

    def get_age(self):
        return self.Age

    def get_course(self):
        return self.__Course

    def get_hometown(self):
        return self.Hometown

    # Register the student and return the ID
    def register(self):
        Student.count += 1
        self.__ID = Student.count
        return self.__ID

    # Private method to update the name
    def __update_name(self, name):
        self.Name = name

    # Protected method to update the age
    def _update_age(self, age):
        self.Age = age


