class Smartphone:
    def __init__(self, brand, model, number):
        self._brand = brand
        self._model = model
        self._number = number

    def show(self):
        print(self._brand, '-',  self._model + '.', self._number)
