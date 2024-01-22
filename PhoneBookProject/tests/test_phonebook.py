from PhoneBookProject.phonebook.phonebook import (
    add_record,
    update_record,
    delete_record_by_phone,
    search_record_by_value
)
import unittest
import json


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.test_record = {
            "first_name": "Test_Name",
            "last_name": "Test_Last_Name",
            "full_name": "Test_Name Test_Last_Name",
            "phone": "0123456789",
            "city": "Test_City"
        }
        self.file_path = r"C:\python-course\PhoneBookProject\tests\test_data\data.json"
        self.initial_content = ('[{"first_name": "Daryna", "last_name": "Nikitenko", "full_name": "Daryna Nikitenko", '
                                '"phone": "+48698249023", "city": "Torun"}, {"first_name": "Natalia", "last_name": '
                                '"Nikitenko", "full_name": "Natalia Nikitenko", "phone": "+380979965586", '
                                '"city": "Kyiv"}]')
        self.records = []

    def test_record_is_found(self):
        add_record(self.file_path, self.records, self.test_record)
        record = search_record_by_value(self.test_record["phone"], self.records)
        self.assertEqual(self.test_record, record, "Record is not found.")

    def test_record_is_not_added(self):
        record = search_record_by_value(self.test_record["first_name"], self.records)
        self.assertNotEqual(self.test_record, record, "Record is found.")

    def test_add_record(self):
        add_record(self.file_path, self.records, self.test_record)
        with open(self.file_path, "r") as file:
            updated_content = file.read()

        self.assertTrue(len(self.records) > 0, "Record list is empty.")
        self.assertNotEqual(self.initial_content, updated_content, "Record was not added.")

    def test_delete_record(self):
        add_record(self.file_path, self.records, self.test_record)
        delete_record_by_phone(self.file_path, self.records, self.test_record["phone"])
        with open(self.file_path, "r") as file:
            updated_content = file.read()

        self.assertTrue(len(self.records) == 0, "Record list is not empty.")
        self.assertNotIn(json.dumps(self.test_record), updated_content, "Record was not deleted.")

    def test_update_record(self):
        add_record(self.file_path, self.records, self.test_record)
        update_record(self.file_path, self.records, self.test_record["phone"], "first_name",
                      "Test_Name_Name")
        with open(self.file_path, "r") as file:
            updated_content = file.read()

        self.assertEqual(self.test_record["first_name"], json.loads(updated_content)[0]["first_name"],
                         "Record first_name was not updated.")

    def tearDown(self):
        with open(self.file_path, "w") as file:
            file.write(self.initial_content)


if __name__ == '__main__':
    unittest.main()
