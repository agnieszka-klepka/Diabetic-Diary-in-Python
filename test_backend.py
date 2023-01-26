from model import Model


def main():
    bloodLevel = 85
    measurementDay = '25-01-2023'

    model = Model()
    model.setter(bloodLevel, measurementDay)
    # model.saveDataToBase()
    # print(model.calculateStatistics())
    model.drawMeasure()


if __name__ == '__main__':
    main()
