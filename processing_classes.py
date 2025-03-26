# ------------------------------------------------------------------------------------------------- #
# Title: processing_classes
# Description: A collection of classes handling file processing for the application
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/21/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import json
import data_classes as data

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/21/2025,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: data.Employee):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: an reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:  # external file is open and read from
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()   # employee_object is set to return value from employee_type() function
                    employee_object.first_name=employee["FirstName"]    # employee_object.first_name is set to employee first name from list of dictionary data
                    employee_object.last_name=employee["LastName"]      # employee_object.last_name is set to employee last name from list of dictionary data
                    employee_object.review_date=employee["ReviewDate"]  # employee_object.review_date is set to employee review date from list of dictionary data
                    employee_object.review_rating=employee["ReviewRating"]  # employee_object.review_rating is set to employee review rating from list of dictionary data
                    employee_data.append(employee_object)   # employee_object is appended to employee data list
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!") # FileNotFoundError is raised if external file does not exist
        except Exception:
            raise Exception("There was a non-specific error!")  # general Exception is raised if error other than FileNotFoundError is generated
        return employee_data    # employee_data list is returned

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/21/2025,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []  # list_of_dictionary_data is set to list
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }    # employee_json dictionary is assigned employee_data information
                list_of_dictionary_data.append(employee_json)   # employee_json data is appended to list_of_dictionary_data list

            with open(file_name, "w") as file:  # external file is opened to write to
                json.dump(list_of_dictionary_data, file)    # list_of_dictionary_data list is written to external file
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")    # TypeError is raised if data is not in valid JSON format
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission") # PermissionError is raised if program does not have read/write permission for external file
        except Exception as e:
            raise Exception("There was a non-specific error!")  # General Exception is raised if error other than TypeError or PermissionError occurs
