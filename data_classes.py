# ------------------------------------------------------------------------------------------------- #
# Title: data_classes
# Description: A collection of classes handling data for the application
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/21/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

from datetime import date

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - Alberto Arriola, 3/21/2025: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """ This method is the Person class constructor

        :param first_name: string data with first name
        :param last_name: string data with last name
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        self.first_name = first_name    # first_name property assignment
        self.last_name = last_name      # last_name property assignment

    # getter for the first_name property
    @property
    def first_name(self):
        """ This method is the first_name getter for the Person class

        :param: None
        :return: first_name string in Title format

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return self.__first_name.title()    # return first_name string in Title format

    # setter for the first_name property
    @first_name.setter
    def first_name(self, value: str):
        """ This method is the first_name setter for the Person class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        if value.isalpha() or value == "":  # check if first_name string contains only letters or is blank
            self.__first_name = value   # first_name string is set to passed value if it contains only letters
        else:
            raise ValueError("The first name should not contain numbers.")  # ValueError is raised if first_name doesn't contain only letters

    # getter for the last_name property
    @property
    def last_name(self):
        """ This method is the last_name getter for the Person class

        :param: None
        :return: first_name string in Title format

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return self.__last_name.title() # return last_name string in Title format

    # setter for the last_name property
    @last_name.setter
    def last_name(self, value: str):
        """ This method is the last_name setter for the Person class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        if value.isalpha() or value == "":  # check if last_name string contains only letters or is blank
            self.__last_name = value    # last_name string is set to passed value if it contains only letters
        else:
            raise ValueError("The last name should not contain numbers.")   # ValueError is raised if last_name doesn't contain only letters

    # override __str__() method to return Person data
    def __str__(self):
        """ This method is the __str__() override for the Person class

        :param: None
        :return: f string format of first_name and last_name

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - Alberto Arriola, 3/21/2025: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        """ This method is the Employee class constructor

        :param first_name: string data with first name
        :param last_name: string data with last name
        :param review_date: string data with date
        :param review_rating: integer data with review rating
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        super().__init__(first_name=first_name,last_name=last_name)     # call to Person constructor for first_name and last_name
        self.review_date = review_date      # review_date property assignment
        self.review_rating = review_rating  # review_rating property assignment

    # getter for review_date property
    @property
    def review_date(self):
        """ This method is the review_date getter for the Employee class

        :param: None
        :return: review_date string

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return self.__review_date   # return review_date string

    # setter for review_date property
    @review_date.setter
    def review_date(self, value: str):
        """ This method is the review_date setter for the Employee class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        try:
            date.fromisoformat(value)   # fromisoformat sets date format to YYYY-MM-DD
            self.__review_date = value  # review_date is set to value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD") # ValueError is raised if date format is not YYYY-MM-DD

    # getter for review_date property
    @property
    def review_rating(self):
        """ This method is the review_rating getter for the Employee class

        :param: None
        :return: review_date string

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return self.__review_rating     # return review_rating string

    # setter for review_rating property
    @review_rating.setter
    def review_rating(self, value: str):
        """ This method is the review_rating setter for the Employee class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        if value in (1, 2, 3, 4, 5):    # if statement checks if value is 1,2,3,4 or 5
            self.__review_rating = value    # review_rating is set to value
        else:
            raise ValueError("Please choose only values 1 through 5")   # ValueError is raised if value is not 1,2,3,4 or 5

    # override __str__() method to return Person data
    def __str__(self):
        """ This method is the __str__() override for the Employee class

        :param: None
        :return: f string format of first_name, last_name, review_date, and review_rating

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025, Created method
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"