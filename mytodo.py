# mytodo.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout #QtCore


def mytodoapp(show=True): #  Add the show argument with a default value of True

    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()

    window.resize(1280, 720)
    window.setWindowTitle("Sten's To-Do App")


    helloMsg = QLabel("Todo App Just 4 You")

    layout = QHBoxLayout()
    layout.addWidget(helloMsg)

    #layout.addWidget(helloMsg, alignment=QtCore.Qt.AlignCenter)
    window.setLayout(layout)

    # Show window only if show is True
    window.show() if show else None  

    # Start the event loop.
    return app.exec()

if __name__ == "__main__":
    app = mytodoapp()
    sys.exit(app.exec_())