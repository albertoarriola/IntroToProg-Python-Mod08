# ------------------------------------------------------------------------------------------------- #
# Title: test_presentation_classes
# Description: unit testing for the presentation_classes module
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/25/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
import data_classes as data

class TestIO(unittest.TestCase):
    """
    A collection of unit tests to test the presentation layer modules

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/25/2025,Created Class
    """

    def test_input_menu_choice(self):
        # unit test to verify input_menu_choice records the expected value
        with patch("builtins.input", return_value="2"):     # use patch to override return value from input_menu_choice
            choice = IO.input_menu_choice()     # assign choice value of input_menu_choice return value
            self.assertEqual("2", choice)   # verify choice is equal to "2"

    def test_input_employee_data(self):
        # unit test to verify employee review date is in the correct format
        with patch("builtins.input", side_effect=["Vincent","Cane","2025-11-11",3]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=data.Employee)
            self.assertEqual(1, len(employees))     # verify the employees list has the contains the correct data
            self.assertEqual("Vincent", employees[0].first_name)    # verify first name of Employee in employees list is correct
            self.assertEqual("Cane", employees[0].last_name)    # verify last name of Employee in employees list is correct
            self.assertEqual("2025-11-11", employees[0].review_date)    # verify review date of Employee in employees list is correct
            self.assertEqual(3, employees[0].review_rating)     # verify review rating of Employee in employees list is correct

    def test_input_valid_employee_data(self):
        # unit test to verify the employee review date is in the correct format and the employee review rating has a valid value
        with self.assertRaises(ValueError):  # ValueError is expected
            employee = data.Employee("Bob", "Baker", "11-11-2025", 3)  # employee review date is in invalid format
        with self.assertRaises(ValueError):  # ValueError is expected
            employee = data.Employee("Bob", "Baker", "2025-11-11", 6)  # employee review rating is an invalid value

if __name__ == "__main__":
    unittest.main()