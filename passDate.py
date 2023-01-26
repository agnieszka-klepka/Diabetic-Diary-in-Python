
class PassDate:

    def __init__(self):
        self._data = None

    def setter(self, data):
        self._data = data
        print(self._data)

    def getter(self):
        return self._data
