# Projekt Informatyczne Systemy Medyczne
# Dziennik diabetyka
import datetime

import numpy as np
import matplotlib.pyplot as plt
from database import Database
from os import getenv

'''
    MODEL
'''

sugarLevelList = []
measurementDayList = []


def Average(lst):
    return sum(lst)/len(lst)


class Model:

    def __init__(self, _sugarLevel=0, _measurementDay=0):
        self.sugarLevel = _sugarLevel
        self.measurementDay = _measurementDay

    def setter(self, _sugarLevel, _measuremenrDay):
        self.sugarLevel = _sugarLevel
        self.measurementDay = _measuremenrDay

    def getter(self):
        return self.sugarLevel, self.measurementDay

    def saveDataToBase(self):
        db = Database(getenv('DB_NAME'))
        values = self.getter()  # tuple
        db.insert('diabetes', None, values[0], values[1])

    def calculateStatistics(self):
        db = Database(getenv('DB_NAME'))
        omg = db.printData()

        for om in omg:
            if om[1] > 0:
                sugarLevelList.append(om[1])

        # Finding minimal, maximum, average value and standard deviation
        minValue = min(sugarLevelList)
        maxValue = max(sugarLevelList)
        avg = Average(sugarLevelList)
        std = round(np.std(sugarLevelList), 2)

        return minValue, maxValue, avg, std

    def dataFromDB(self):
        db = Database(getenv('DB_NAME'))
        return db.printData()

    # TODO
    def drawMeasure(self):
        _x = []
        y = []

        db = Database(getenv('DB_NAME'))
        omg = db.printData()

        for om in omg:
            if om[1] > 0:
                y.append(int(om[1]))
                _x.append(om[2])

        x = []
        for tup in _x:
            dat = tup.split("-")
            if int(dat[0]) > 0 and int(dat[1]) > 0 and int(dat[2]) > 0:
                _date = datetime.date(int(dat[0]), int(dat[1]), int(dat[2]))
                x.append(_date)

        plt.bar(_x, y, color='g', width=0.50, label="Blood Sugar Level")
        plt.xlabel('Date')
        plt.ylabel('BSL')
        plt.title('Diabetes course')
        plt.gcf().autofmt_xdate()
        plt.legend()
        plt.show()

