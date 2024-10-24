#!/usr/bin/python3
import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the class-level counter before each test."""
        Square._Base__nb_objects = 0

    def test_square_initialization(self):
        """Test the basic initialization of Square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(7, 2, 3, 10)
        self.assertEqual(s2.size, 7)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_invalid_size(self):
        """Test if size raises errors for invalid input."""
        with self.assertRaises(TypeError):
            Square("4")  # size should be an integer
        with self.assertRaises(ValueError):
            Square(-4)  # size should be > 0
        with self.assertRaises(ValueError):
            Square(0)  # size should be > 0

    def test_invalid_x_y(self):
        """Test if x and y raise errors for invalid input."""
        with self.assertRaises(TypeError):
            Square(4, "2", 3)  # x should be an integer
        with self.assertRaises(ValueError):
            Square(4, -2, 3)  # x should be >= 0

        with self.assertRaises(TypeError):
            Square(4, 2, "3")  # y should be an integer
        with self.assertRaises(ValueError):
            Square(4, 2, -3)  # y should be >= 0

    def test_square_str(self):
        """Test the __str__ method of Square."""
        s = Square(4, 1, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 1/1 - 4")

    def test_square_display(self):
        """Test the display method of Square."""
        s = Square(4, 2, 1)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(output.getvalue(), expected_output)

        s2 = Square(3)
        output = io.StringIO()
        sys.stdout = output
        s2.display()
        sys.stdout = sys.__stdout__
        expected_output = "###\n###\n###\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_square_to_dictionary(self):
        """Test to_dictionary method of Square."""
        s = Square(5, 1, 1, 20)
        s_dict = s.to_dictionary()
        expected = {'id': 20, 'size': 5, 'x': 1, 'y': 1}
        self.assertEqual(s_dict, expected)

    def test_square_update_args(self):
        """Test the update method of Square with *args."""
        s = Square(5)
        s.update(10, 7, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_kwargs(self):
        """Test the update method of Square with **kwargs."""
        s = Square(5)
        s.update(id=20, size=6, x=1, y=2)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_square_save_to_file(self):
        """Test save_to_file method of Square."""
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 1, 4, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            expected = '[{"id": 1, "size": 10, "x": 2, "y": 8}, {"id": 2, "size": 2, "x": 1, "y": 4}]'
            self.assertEqual(file.read(), expected)

    def test_square_save_to_file_empty(self):
        """Test save_to_file method when list is empty."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_square_load_from_file(self):
        """Test load_from_file method of Square."""
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 1, 4, 2)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 10)
        self.assertEqual(squares[0].x, 2)
        self.assertEqual(squares[0].y, 8)

        self.assertEqual(squares[1].id, 2)
        self.assertEqual(squares[1].size, 2)
        self.assertEqual(squares[1].x, 1)
        self.assertEqual(squares[1].y, 4)


if __name__ == "__main__":
    unittest.main()
