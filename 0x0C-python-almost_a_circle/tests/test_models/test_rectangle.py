#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Resets everything before running a test."""
        Base._Base__nb_objects = 0

    def test_width(self):
        """Test valid and invalid values for width."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)

        with self.assertRaises(TypeError):
            Rectangle("10", 5)  # width as a string

        with self.assertRaises(ValueError):
            Rectangle(0, 5)  # width should be > 0

        with self.assertRaises(ValueError):
            Rectangle(-5, 5)  # width should be > 0

    def test_height(self):
        """Test valid and invalid values for height."""
        r2 = Rectangle(5, 10)
        self.assertEqual(r2.height, 10)

        with self.assertRaises(TypeError):
            Rectangle(5, "10")  # height as a string

        with self.assertRaises(ValueError):
            Rectangle(5, 0)  # height should be > 0

        with self.assertRaises(ValueError):
            Rectangle(5, -5)  # height should be > 0

    def test_x(self):
        """Test valid and invalid values for x."""
        r3 = Rectangle(5, 10, 3, 4)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 10)
        self.assertEqual(r4.x, 0)  # x has a default value of 0

        with self.assertRaises(TypeError):
            Rectangle(5, 10, "3")  # x as a string

        with self.assertRaises(ValueError):
            Rectangle(5, 10, -3)  # x should be >= 0

    def test_y(self):
        """Test valid and invalid values for y."""
        r5 = Rectangle(5, 10, 3, 4)
        self.assertEqual(r5.y, 4)

        r6 = Rectangle(5, 10)
        self.assertEqual(r6.y, 0)  # y has a default value of 0

        with self.assertRaises(TypeError):
            Rectangle(5, 10, 3, "4")  # y as a string

        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -4)  # y should be >= 0

    def test_id_auto(self):
        """Test if id is auto-incremented when not provided."""
        r1 = Rectangle(10, 5)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(7, 2)
        
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_id_custom(self):
        """Test if custom id works correctly."""
        r1 = Rectangle(10, 5, id=100)
        r2 = Rectangle(3, 4, id=200)
        
        self.assertEqual(r1.id, 100)
        self.assertEqual(r2.id, 200)

    def test_id_mixed(self):
        """Test a mix of auto-incremented and custom ids."""
        r1 = Rectangle(10, 5)  # Auto-assigned id
        r2 = Rectangle(3, 4, id=999)  # Custom id
        r3 = Rectangle(7, 2)  # Auto-assigned id should continue after custom
        
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 999)
        self.assertEqual(r3.id, 2)

    def test_area(self):
        """Test if area works well."""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test___str__(self):
        """Test if the magic string works."""
        r = Rectangle(2, 8, 5, 6, 57)
        str_rep = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(r.__str__(), str_rep)

    def test_display_no_x_no_y(self):
        """Test the display method when no x and y are provided."""
        r = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        
        # Redirect stdout to capture print output
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_with_y_only(self):
        """Test the display method with only y provided."""
        r = Rectangle(4, 3, 0, 2)  # x = 0, y = 2
        expected_output = "\n\n####\n####\n####\n"
        
        # Redirect stdout to capture print output
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_with_x_and_y(self):
        """Test the display method with both x and y provided."""
        r = Rectangle(4, 3, 2, 2)  # x = 2, y = 2
        expected_output = "\n\n  ####\n  ####\n  ####\n"
        
        # Redirect stdout to capture print output
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
