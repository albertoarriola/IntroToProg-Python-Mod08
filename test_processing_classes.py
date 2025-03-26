# ------------------------------------------------------------------------------------------------- #
# Title: test_processing_classes
# Description: unit testing for the processing_classes module
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/25/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
from processing_classes import FileProcessor
import data_classes as data

class TestFileProcessor(unittest.TestCase):
    """
    A collection of unit tests to test the file processing layer modules

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/25/2025,Created Class
    """

    def setUp(self):
        # function to setup a temporary external file; executed before every unit test
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)  # set temp_file to the temporary file object
        self.temp_file_name = self.temp_file.name   # set temp_file_name to name of temp_file
        self.employee_data = []     # initialize employee_data list

    def tearDown(self):
        # function to tear down temporary external file setup; executed before every unit test
        self.temp_file.close()  # close the temporary file

    def test_read_data_from_file(self):
        # unit test to verify data from temporary file is read correctly
        sample_data = [{"FirstName": "Vincent", "LastName": "Cane", "ReviewDate": "2025-12-11", "ReviewRating": 3},
                       {"FirstName": "Sue", "LastName": "Jones", "ReviewDate": "2024-11-09", "ReviewRating": 4},
        ]    # sample_data is assigned valid Employee values
        with open(self.temp_file_name, "w") as file:    # open temporary file as file to write data to
            json.dump(sample_data, file)    # dump data from sample_data list to temporary file

        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name,
                                                               employee_data=self.employee_data,
                                                               employee_type=data.Employee)
        # read data from temporary file using read_employee_data_from_file function in IO class of processing_classes file into employees list
        self.assertEqual(len(sample_data), len(employees))  # verify length of data in sample data is equal to length of data read from the external file

        for i in range(len(sample_data)):   # for loop runs for number of items in sample_data list
            self.assertEqual(sample_data[i]["FirstName"], employees[i].first_name)  # verify first name of item in sample data equals first name of item in employees list
            self.assertEqual(sample_data[i]["LastName"], employees[i].last_name)    # verify last name of item in sample data equals last name of item in employees
            self.assertEqual(sample_data[i]["ReviewDate"], employees[i].review_date)    # verify review date of item in sample data equals review date of item in employees
            self.assertEqual(sample_data[i]["ReviewRating"], employees[i].review_rating) # verify review rating of item in sample data equals review rating of item in employees

    def test_write_data_to_file(self):
        # unit test to verify data is written to external file correctly
        sample_data = [
            data.Employee("Vincent","Cane","2025-11-11",3),
            data.Employee("Sue","Jones","2025-11-11",4)
        ]   # sample_data is assigned valid Employee values
        FileProcessor.write_employee_data_to_file(file_name=self.temp_file_name, employee_data=sample_data) # write_employee_data_to_file writes sample data to external temporary file

        with open(self.temp_file_name, "r") as file:    # open temporary file as file to read data from
            file_data = json.load(file)     # assign value of data read from temporary file to file_data list

        self.assertEqual(len(sample_data), len(file_data))  # verify length of items in sample_data equals length of items read from temporary file

        for i in range(len(sample_data)):   # for loop runs for number of items in sample_data list
            self.assertEqual(sample_data[i].first_name, file_data[i]["FirstName"])  # verify first name of item in sample data equals first name of item read from temporary file
            self.assertEqual(sample_data[i].last_name, file_data[i]["LastName"])    # verify last name of item in sample data equals last name of item read from temporary file
            self.assertEqual(sample_data[i].review_date, file_data[i]["ReviewDate"])    # verify review date of item in sample data equals review date of item read from temporary file
            self.assertEqual(sample_data[i].review_rating, file_data[i]["ReviewRating"])    # verify review rating of item in sample data equals review rating of item read from temporary file


if __name__ == "__main__":
    unittest.main()