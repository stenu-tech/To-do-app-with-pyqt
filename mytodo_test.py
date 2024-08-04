import unittest
from mytodo import mytodoapp

class TodoTests(unittest.TestCase):
    
    def test_qt_window_parameters(self):
        """Test window sizes, title and hello message."""

        # Create the application without showing it (for testing)
        app = mytodoapp(show=False)

        # Get the window object
        window = app.window()

        # Assert the width and height of the window
        self.assertEqual(window.width(), 1280)
        self.assertEqual(window.height(), 720)
        self.assertEqual(window.windowTitle(), "Sten's To-Do App")

        # Find the QLabel widget with the hello message
        hello_label = window.findChild(QLabel)

        # Assert the text of the label
        self.assertEqual(hello_label.text(), "Todo App Just 4 You")

        # Close the application (optional)
        app.exit()