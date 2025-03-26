# ------------------------------------------------------------------------------------------------- #
# Title: data_classes
# Description: A collection of classes handling input and output for the application
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/21/2025,Created Script
# ------------------------------------------------------------------------------------------------- #
from operator import truediv

import data_classes as data

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/21/2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")  # custom error message is displayed
        if error is not None:   # if statement is triggered if error data is sent to output_error_messages function
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')  # Python error information is displayed


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :return: None
        """
        print()
        print(menu) # menu is displayed
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")   # choice is set to user input
            if choice not in ("1", "2", "3", "4"):  # Note these are strings; if statement triggered if choice is not 1,2,3,4 or 5
                raise Exception("Please, choose only 1, 2, 3, or 4")    # Exception is raised if choice is not 1,2,3,4 or 5
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice   # choice value is returned


    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:  # for Loop executes for each employee in employee_data list
            if employee.review_rating == 5:     # if statement triggered if review rating = 5
                message = " {} {} is rated as 5 (Leading)"  # message is set if employee's review rating = 5
            elif employee.review_rating == 4:   # if statement triggered if review rating = 4
                message = " {} {} is rated as 4 (Strong)"   # message is set if employee's review rating = 4
            elif employee.review_rating == 3:   # if statement triggered if review rating = 3
                message = " {} {} is rated as 3 (Solid)"    # message is set if employee's review rating = 3
            elif employee.review_rating == 2:   # if statement triggered if review rating = 2
                message = " {} {} is rated as 2 (Building)" # message is set if employee's review rating = 2
            elif employee.review_rating == 1:   # if statement triggered if review rating = 1
                message = " {} {} is rated as 1 (Not Meeting Expectations)" # message is set if employee's review rating = 1

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
            # message is printed for each employee
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: data.Employee):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()   # employee_object is set to employee_type() object
            employee_object.first_name = input("What is the employee's first name? ")   # employee_object.first_name is set to user first name input
            employee_object.last_name = input("What is the employee's last name? ")     # employee_object.last_name is set to user last name input
            employee_object.review_date = input("What is their review date?(YYYY-MM-DD) ")  # employee_object.review_date is set to user review date input
            employee_object.review_rating = int(input("What is their review rating?(1 through 5) "))    # employee_object.review_rating is set to user review rating input
            employee_data.append(employee_object)   # employee object data is appended to employee_data list

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)  # ValueError occurs if user enters invalid type of data
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)  # Exception error occurs for any error other than ValueError

        return employee_data    # employee_data list is returned
