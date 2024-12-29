import sys

from PyQt6.QtWidgets import QApplication
from calendar_file import PyCalendar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyCalendar()
    ex.show()
    sys.exit(app.exec())
