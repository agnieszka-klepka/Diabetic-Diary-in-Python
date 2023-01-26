from PySide2.QtCore import QDate
from PySide2.QtWidgets import QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QStyle, \
    QCalendarWidget, QVBoxLayout, QWidget

from passDate import PassDate

'''
    VIEW
'''
passDate = PassDate()


class ViewWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()

        self._controller = controller

        self.calend = None
        self.dayLevel = None
        self.openCalendar = None
        self.saveButton = None
        self.drawButton = None
        self.printButton = None
        self.statsButton = None
        self.labelLevel = None
        self.bloodSugarLevel = None
        self.textArea1 = None
        self.textArea2 = None
        self.calendarInput = None
        self.textCalendar = None
        self.closeButton = None
        self.saveDate = None
        self.setWindowTitle("My Diabetes")
        self.setGeometry(500, 200, 400, 400)

        # closebtn.clicked.connect(self.quit)

        self.windowElements()

    def windowElements(self):
        box = QHBoxLayout()

        # labels
        self.labelLevel = QLabel('Enter sugar level: ', self)
        self.labelLevel.setGeometry(20, 20, 180, 20)

        self.dayLevel = QLabel('Enter date: ', self)
        self.dayLevel.setGeometry(180, 20, 180, 20)

        # text areas
        self.textArea1 = QTextEdit(self)
        self.textArea1.setReadOnly(True)
        self.textArea1.move(20, 320)
        self.textArea1.resize(560, 260)

        self.textArea2 = QTextEdit(self)
        self.textArea2.setReadOnly(True)
        self.textArea2.move(20, 100)
        self.textArea2.resize(420, 200)

        # edit lines
        self.bloodSugarLevel = QLineEdit('mg/dL', self)
        self.bloodSugarLevel.move(20, 50)

        # date from calendar
        self.textCalendar = QTextEdit(self)
        self.textCalendar.setReadOnly(True)
        self.textCalendar.move(180, 50)

        # buttons
        self.openCalendar = QPushButton("", self)
        self.openCalendar.clicked.connect(self.letsOpenCalendar)
        self.openCalendar.setGeometry(280, 47, 40, 37)
        pixmapi = getattr(QStyle, 'SP_ArrowDown')
        icon = self.style().standardIcon(pixmapi)
        self.openCalendar.setIcon(icon)

        self.saveDate = QPushButton("", self)
        self.saveDate.clicked.connect(self.saveDateToField)
        self.saveDate.setGeometry(310, 47, 40, 37)
        pixmapi2 = getattr(QStyle, 'SP_ArrowUp')
        icon2 = self.style().standardIcon(pixmapi2)
        self.saveDate.setIcon(icon2)

        self.saveButton = QPushButton("Save", self)
        self.saveButton.clicked.connect(self.saveMeasure)
        self.saveButton.move(480, 50)

        self.drawButton = QPushButton("Draw", self)
        self.drawButton.clicked.connect(self.drawMeasure)
        self.drawButton.move(480, 100)

        self.printButton = QPushButton("Print", self)
        self.printButton.clicked.connect(self.printData)
        self.printButton.move(480, 150)

        self.statsButton = QPushButton("Statistics", self)
        self.statsButton.clicked.connect(self.printCalcStats)
        self.statsButton.move(480, 200)

        self.closeButton = QPushButton("Exit", self)
        self.closeButton.clicked.connect(self.myCloseEvent)
        self.closeButton.move(480, 250)

        box.addWidget(self.labelLevel)
        box.addWidget(self.dayLevel)
        box.addWidget(self.textArea1)
        box.addWidget(self.textArea2)
        box.addWidget(self.bloodSugarLevel)
        box.addWidget(self.textCalendar)
        box.addWidget(self.openCalendar)
        box.addWidget(self.saveButton)
        box.addWidget(self.drawButton)
        box.addWidget(self.printButton)
        box.addWidget(self.statsButton)
        box.addWidget(self.saveDate)
        box.addStretch(1)
        self.setLayout(box)

    '''
        VIEW -> CONTROLLER
    '''

    def saveMeasure(self):
        self.textArea2.clear()

        sugarLevel = self.bloodSugarLevel.text()
        measurementDay = self.textCalendar.toPlainText()

        self.bloodSugarLevel.clear()
        self.textCalendar.clear()

        # HEALTH STATUS
        if int(sugarLevel) < 99:
            self.textArea2.insertPlainText("RIGHT BSL VALUE \n")

        if 100 <= int(sugarLevel) <= 125:
            self.textArea2.insertPlainText("WARNING! PRE-DIABETES \n")

        if int(sugarLevel) >= 126:
            self.textArea2.insertPlainText("WARNING! DIABETES \n")

        self._controller.viewDataToDB(sugarLevel, measurementDay)

    def letsOpenCalendar(self):
        self.textCalendar.clear()
        self.calend = Calendar()
        self.calend.show()

    def saveDateToField(self):
        omg = passDate.getter()
        weekDay, _month, day, year = omg.split()
        month = self.revertMonth(_month)
        if int(day) / 10 < 0:
            day = "0" + day
            print(day)

        toPrint = year + "-" + month + "-" + day
        self.textCalendar.insertPlainText(toPrint)
        self.calend.close()

    def revertMonth(self, _month):
        if _month == "Jan":
            month = '01'
        elif _month == "Feb":
            month = '02'
        elif _month == "Mar":
            month = '03'
        elif _month == "Apr":
            month = '04'
        elif _month == "May":
            month = '05'
        elif _month == "Jun":
            month = '06'
        elif _month == "Jul":
            month = '07'
        elif _month == "Aug":
            month = '08'
        elif _month == "Sep":
            month = '09'
        elif _month == "Oct":
            month = '10'
        elif _month == "Nov":
            month = '11'
        elif _month == "Dec":
            month = '12'

        return month

    def myCloseEvent(self):
        self._controller.quit()

    '''
        CONTROLLER -> VIEW
    '''

    def drawMeasure(self):
        self._controller.actualGraph()

    def printData(self):
        self.textArea1.clear()
        data = self._controller.printFromDB()
        for _data in data:
            id, s, date = _data
            self.textArea1.insertPlainText("Sugar level: " + str(s) +
                                           " , date of measurement: " + str(date) + "\n")

    def printCalcStats(self):
        self.textArea2.clear()
        data = self._controller.getStats()
        minValue, maxValue, avg, std = data
        self.textArea2.insertPlainText(
            "Minimal value: " + str(minValue) + "\n" + "Maximal value: " + str(maxValue) + "\n" + "Average value:  "
            + str(avg) + "\n" + "Standard deviation: " + str(std) + "\n")


class Calendar(QWidget):

    def __init__(self):
        super().__init__()
        self.saveDate = None
        self.lbl = None
        self.chosenOne = None

        self.createCalendar()

    def createCalendar(self):
        cal = QCalendarWidget()
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self._showDate)

        self.lbl = QLabel("Calendar")
        date = cal.selectedDate()

        vbox = QVBoxLayout()
        vbox.addWidget(cal)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)

    def _showDate(self, date):
        self.chosenOne = date.toString()
        passDate.setter(self.chosenOne)
