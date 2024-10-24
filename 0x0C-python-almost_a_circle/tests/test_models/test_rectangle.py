#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys
import os


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Resets everything before running a test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleanup the test environment by removing files after each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

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
        # Reset stdout to default to print normally again
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

    def test_to_dictionary(self):
        """Test the to_dictionary method for the Rectangle class."""
        r1 = Rectangle(10, 2, 1, 9, 5)
        expected_dict = {
            'id': 5,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9
        }
        self.assertEqual(r1.to_dictionary(), expected_dict)

    def test_to_dictionary_auto_id(self):
        """Test to_dictionary when id is auto-generated."""
        r2 = Rectangle(3, 4, 2, 2)
        expected_dict = {
            'id': 1,  # Since this is the first object, id will be 1
            'width': 3,
            'height': 4,
            'x': 2,
            'y': 2
        }
        self.assertEqual(r2.to_dictionary(), expected_dict)

    def test_to_dictionary_updated(self):
        """Test to_dictionary after updating the attributes."""
        r3 = Rectangle(5, 5, 1, 1, 15)
        r3.width = 20
        r3.height = 30
        r3.x = 3
        r3.y = 4
        expected_dict = {
            'id': 15,
            'width': 20,
            'height': 30,
            'x': 3,
            'y': 4
        }
        self.assertEqual(r3.to_dictionary(), expected_dict)

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dictionary."""
        r4 = Rectangle(7, 8)
        self.assertTrue(isinstance(r4.to_dictionary(), dict))

    def test_update_args(self):
        """Test update method with positional arguments."""
        r1 = Rectangle(10, 20, 5, 7, 1)
        r1.update(89, 4, 3, 2, 1)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_update_kwargs(self):
        """Test update method with keyword arguments."""
        r1 = Rectangle(10, 20, 5, 7, 1)
        r1.update(id=89, width=4, height=3, x=2, y=1)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_update_args_and_kwargs(self):
        """Test update method with both args and kwargs, only args should be used."""
        r1 = Rectangle(10, 20, 5, 7, 1)
        r1.update(89, 4, 3, 2, 1, id=50, width=99, height=98, x=99, y=100)

        # Positional arguments take precedence over keyword arguments
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_update_no_args(self):
        """Test update method with no arguments, nothing should change."""
        r1 = Rectangle(10, 20, 5, 7, 1)
        r1.update()

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

    def test_update_invalid_args(self):
        """Test update method with invalid arguments."""
        r1 = Rectangle(10, 20, 5, 7, 1)

        with self.assertRaises(TypeError):
            r1.update(89, "invalid_width")  # Invalid width (string instead of int)
        
        with self.assertRaises(ValueError):
            r1.update(89, -10, 20)  # Invalid width (negative value)

    def test_update_partial_kwargs(self):
        """Test update method with partial keyword arguments."""
        r1 = Rectangle(10, 20, 5, 7, 1)
        r1.update(width=30)

        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 20)  # Unchanged
        self.assertEqual(r1.x, 5)  # Unchanged
        self.assertEqual(r1.y, 7)  # Unchanged

    def test_create_rectangle(self):
        """Test the create method to create a new Rectangle from dictionary."""
        rect_dict = {'id': 89, 'width': 10, 'height': 4, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)

        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_create_rectangle_default_id(self):
        """Test create method when id is not provided."""
        rect_dict = {'width': 10, 'height': 4, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_save_to_file(self):
        """Test the save_to_file method with normal Rectangle instances."""
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([rect1, rect2])

        with open("Rectangle.json", "r") as file:
            content = file.read()

        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, expected)

    def test_save_to_file_empty_list(self):
        """Test the save_to_file method with an empty list."""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        """Test the save_to_file method when None is passed."""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(content, "[]")

    def test_load_from_file(self):
        """Test the load_from_file method with normal Rectangle instances."""
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([rect1, rect2])

        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)

        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 8)

        self.assertEqual(rectangles[1].id, 2)
        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 0)
        self.assertEqual(rectangles[1].y, 0)

    def test_load_from_file_no_file(self):
        """Test the load_from_file method when no file exists."""
        rectangles = Rectangle.load_from_file()

        self.assertEqual(rectangles, [])

if __name__ == "__main__":
    unittest.main()
