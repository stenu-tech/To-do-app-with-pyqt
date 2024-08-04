import unittest
from mytodo import greet

class TodoTests(unittest.TestCase):
    def test_greet_output(self):
        greeting = greet()

        self.assertEqual(greeting, "Hello World!")