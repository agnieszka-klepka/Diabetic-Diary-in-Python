import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
from PySide2.QtWidgets import QMainWindow, QHBoxLayout


class Calendar(QWidget):

    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.lbl = None
        self.chosenOne = None
        self.createCalendar()

    def createCalendar(self):
        cal = QCalendarWidget()
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self._showDate)

        self.lbl = QLabel()
        date = cal.selectedDate()
        print(date)

        vbox = QVBoxLayout()
        vbox.addWidget(cal)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def _showDate(self, date):
        self.chosenOne = date.toString()
        self._parent.returnDate(self.chosenOne)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calendar()
    sys.exit(app.exec_())
