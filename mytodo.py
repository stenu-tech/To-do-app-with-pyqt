# mytodo.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QtCore


def greet():
    return "Hello World!"

def mytodoapp():

    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()

    window.resize(1280, 720)
    window.setWindowTitle("Sten's To-Do App")


    helloMsg = QLabel("Todo App Just 4 You")

    layout = QHBoxLayout()

    layout.addWidget(helloMsg, alignment=QtCore.Qt.AlignCenter)
    window.setLayout(layout)

    window.show()

    # Start the event loop.
    return app

if __name__ == "__main__":
    app = mytodoapp()
    sys.exit(app.exec_())