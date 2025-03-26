# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes
# Description: unit testing for the data_classes module
# ChangeLog: (Who, When, What)
# Alberto Arriola, 3/25/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    """
    A collection of unit tests to test the data layer modules

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/25/2025,Created Class
    """

    def test_person_init(self):
        # unit test to verify Person init creates Person object correctly
        person = Person("Bob", "Baker")     # person is Person object with "Bob" first_name and "Baker" last_name
        self.assertEqual("Bob", person.first_name)      # verify person first_name = "Bob"
        self.assertEqual("Baker", person.last_name)     # verify person last_name = "Baker"

    def test_person_invalid_name(self):
        # unit test to verify person first_name and last_name only contain alpha characters
        with self.assertRaises(ValueError):     # ValueError is expected
            person = Person("123", "Baker")     # person first_name contains non-alpha characters
        with self.assertRaises(ValueError):     # ValueError is expected
            person = Person("Bob", "123")       # person last_name contains non-alpha characters

    def test_person_str(self):
        # unit test to verify person string is created correctly
        person = Person("Bob", "Baker")  # person is Person object with "Bob" first_name and "Baker" last_name
        self.assertEqual("Bob,Baker", str(person))    # verify person is equal to "Bob, Baker"


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):
    # unit test to verify Employee init creates Person object correctly
        employee = Employee("Bob", "Baker", "2025-11-11", 3)
        # employee is Employee object with "Bob" first_name, "Baker" last_name, "2025-11-11" review_date, and 3 review_rating
        self.assertEqual("Bob", employee.first_name)  # verify employee first_name = "Bob"
        self.assertEqual("Baker", employee.last_name)  # verify employee last_name = "Baker"
        self.assertEqual("2025-11-11", employee.review_date) # verify employee review_date = "2025-11-11"
        self.assertEqual(3, employee.review_rating) # verify employee review_rating = 3

    def test_employee_invalid_date_format(self):
        # unit test to verify employee review_date is formatted YYYY-MM-DD
        with self.assertRaises(ValueError):     # ValueError is expected
            employee = Employee("Bob", "Baker", "11-11-2025", 3)     # employee review_date is in MM-DD-YYYY format

    def test_employee_invalid_rating_value(self):
        # unit test to verify employee review_rating is 1, 2, 3, 4 or 5
        with self.assertRaises(ValueError):     # ValueError is expected
            employee = Employee("Bob", "Baker", "2025-11-11", 6)     # employee review_date is in MM-DD-YYYY format

    def test_employee_str(self):
        # unit test to verify employee string is created correctly
        employee = Employee("Bob", "Baker", "2025-11-11", 3)
        self.assertEqual("Bob,Baker,2025-11-11,3", str(employee))


if __name__ == "__main__":
    unittest.main()