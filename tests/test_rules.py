import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import unittest
from rules import remove_blocks

class TestRemoveBlocks(unittest.TestCase):

    def test_remove_existing_pattern(self):
        """ Test removing a pattern that exists within the string. """
        self.assertEqual(remove_blocks("Hello World!", "World"), "Hello !")

    def test_remove_non_existing_pattern(self):
        """ Test trying to remove a pattern that does not exist within the string. """
        self.assertEqual(remove_blocks("Hello World!", "Python"), "Hello World!")

    def test_remove_pattern_from_empty_string(self):
        """ Test removing a pattern from an empty string. """
        self.assertEqual(remove_blocks("", "World"), "")

    def test_remove_empty_pattern(self):
        """ Test removing an empty pattern from a string. """
        self.assertEqual(remove_blocks("Hello World!", ""), "Hello World!")

    def test_remove_special_character_pattern(self):
        """ Test removing a pattern that contains special characters. """
        self.assertEqual(remove_blocks("Hello! World!", "!"), "Hello World")

    def test_remove_pattern_with_special_characters_in_string(self):
        """ Test removing a simple pattern from a string that contains special characters. """
        self.assertEqual(remove_blocks("Hello, World!", "World"), "Hello, !")

    def test_remove_multicharacter_pattern(self):
        """ Test removing a multi-character pattern from a string. """
        self.assertEqual(remove_blocks("Hello Hello World!", "Hello "), "World!")

if __name__ == '__main__':
    unittest.main()
