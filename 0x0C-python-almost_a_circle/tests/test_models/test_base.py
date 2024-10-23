#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset the class-level counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_increment(self):
        """Test if id is auto-incrementing when not provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_custom(self):
        """Test if custom id works."""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string(self):
        """Test if to_json_string works."""
        data = [{"id": 12}]
        json_str = Base.to_json_string(data)
        self.assertTrue(isinstance(json_str, str))

    def test_save_to_file_none(self):
        """Test if saving to file handles None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == "__main__":
    unittest.main()
