#!/usr/bin/python3
import unittest
from models.square import Square
import io
import sys

class TestSquare(unittest.TestCase):
    
    def test_square_init(self):
        """Test initialization of Square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        
        s2 = Square(10, 3, 4, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

    def test_square_invalid_size(self):
        """Test Square initialization with invalid size."""
        with self.assertRaises(TypeError):
            Square("5")

        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        """Test area calculation."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(9)
        self.assertEqual(s2.area(), 81)

    def test_display(self):
        """Test the display method."""
        s1 = Square(3)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "###\n###\n###\n")
    
    def test_display_with_x_and_y(self):
        """Test display with non-zero x and y."""
        s1 = Square(3, 2, 1)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__
        expected = "\n  ###\n  ###\n  ###\n"
        self.assertEqual(output.getvalue(), expected)

    def test_to_dictionary(self):
        """Test the dictionary representation of Square."""
        s1 = Square(5, 2, 1, 10)
        self.assertEqual(s1.to_dictionary(), {'id': 10, 'size': 5, 'x': 2, 'y': 1})

    def test_update_args(self):
        """Test update method with *args."""
        s1 = Square(5)
        s1.update(10, 7, 2, 3)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        s1 = Square(5)
        s1.update(size=8, y=1, id=15)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 15)

    def test_save_to_file(self):
        """Test saving to file."""
        s1 = Square(5, 2, 1, 10)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertTrue(len(content) > 0)

    def test_load_from_file(self):
        """Test loading from file."""
        s1 = Square(5, 2, 1, 10)
        Square.save_to_file([s1])
        list_squares = Square.load_from_file()
        self.assertEqual(len(list_squares), 1)
        self.assertEqual(list_squares[0].size, 5)

if __name__ == "__main__":
    unittest.main()
