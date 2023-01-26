import sys

from PySide2.QtWidgets import QApplication

from calendar import Calendar
import model
import view

'''
    CONTROLLER
'''


class Controller:

    def __init__(self):
        myApp = QApplication(sys.argv)

        self._view = view.ViewWindow(self)
        self._view.resize(600, 600)
        self._view.show()

        self._model = model.Model()

        myApp.exec_()
        sys.exit(0)

    '''
        VIEW -> MODEL
    '''

    def viewDataToDB(self, _sugarLevel, _measurementDay):
        sugarLevel = _sugarLevel
        measurementDay = _measurementDay

        self._model.setter(sugarLevel, measurementDay)
        self._model.saveDataToBase()


    '''
        MODEL -> VIEW
    '''

    def actualGraph(self):
        self._model.drawMeasure()

    def printFromDB(self):
        return self._model.dataFromDB()

    def getStats(self):
        return self._model.calculateStatistics()

    def quit(self):
        QApplication.quit()


if __name__ == '__main__':
    diabetes = Controller()
