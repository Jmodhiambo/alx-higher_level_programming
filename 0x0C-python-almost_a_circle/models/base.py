#!/usr/bin/python3
"""
This has class Base which is going to be the 'base' of this project.
"""
import json
import csv
import turtle


class Base:
    """This is class Base: the base of this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id.
        Increments __nb_objects for every initialization that id is None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        Overwrites the file if it is not empty.
        """
        filename = f"{cls.__name__}.json"

        # Convert list_objs to a list of dictionaries (using to_dictionary)
        dlist = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        # Write the JSON string to the file
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set, using a dummy instance.
        Arguments:
        **dictionary -- a dictionary of attribute values
        """
        # Create a dummy instance depending on the class type.
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create Rectangle with dummy width and height
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create Square with dummy size

        # Update the dummy instance with the actual values from the dictionary
        dummy.update(**dictionary)

        # Return the updated instance
        return dummy

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Arguments:
        **dictionary -- dictionary of attributes to set on the instance
        """
        # Create a dummy instance depending on the class type.
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a Rectangle with dummy width and height
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a Square with a dummy size

        # Update the dummy instance with the actual values from the dictionary
        dummy.update(**dictionary)

        # Return the updated instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances based on the JSON file for the class.
        If the file doesn't exist, return an empty list.
        """
        # Define the filename based on the class name
        filename = cls.__name__ + ".json"

        try:
            # Try to open the file and read its content
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()  # Read the JSON string from the file
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []

        # Convert the JSON string to a list of dictionaries
        list_dictionaries = cls.from_json_string(json_string)

        # Create a list of instances from the list of dictionaries
        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to a CSV file.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)

            if cls.__name__ == "Rectangle":
                # Write header for Rectangle
                writer.writerows([[obj.id, obj.width, obj.height, obj.x, obj.y]
                                  for obj in list_objs])

            elif cls.__name__ == "Square":
                # Write header for Square
                writer.writerows([[obj.id, obj.size, obj.x, obj.y]
                                  for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.
        """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, mode="r", newline='', encoding="utf-8") as f:
                reader = csv.reader(f)
                objs_list = []

                if cls.__name__ == "Rectangle":
                    # Create instances for Rectangle
                    for row in reader:
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                        objs_list.append(cls.create(**obj_dict))

                elif cls.__name__ == "Square":
                    # Create instances for Square
                    for row in reader:
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                        objs_list.append(cls.create(**obj_dict))

            return objs_list

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using the turtle graphics module.
        """
        # Setup the screen
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        # Create a turtle
        artist = turtle.Turtle()
        artist.speed(1)  # Set the drawing speed

        # Draw rectangles
        artist.color("blue")
        for rect in list_rectangles:
            artist.penup()
            artist.goto(rect.x, rect.y)  # Position the turtle at (x, y)
            artist.pendown()
            artist.begin_fill()
            for _ in range(2):  # Draw rectangle
                artist.forward(rect.width)
                artist.right(90)
                artist.forward(rect.height)
                artist.right(90)
            artist.end_fill()

        # Draw squares
        artist.color("green")
        for square in list_squares:
            artist.penup()
            artist.goto(square.x, square.y)  # Position the turtle at (x, y)
            artist.pendown()
            artist.begin_fill()
            for _ in range(4):  # Draw square
                artist.forward(square.size)
                artist.right(90)
            artist.end_fill()

        # Complete the drawing
        artist.hideturtle()  # Hide the turtle
        screen.mainloop()  # Keep the window open
