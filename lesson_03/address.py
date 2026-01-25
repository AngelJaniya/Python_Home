class Address:
    def __init__(self, zip_code, city, street, building, flat):
        self._zip_code = zip_code
        self._city = city
        self._street = street
        self._building = building
        self._flat = flat

    def to_string(self):
        return (self._zip_code + ', ' + self._city + ', ' +
                self._street + ', ' + self._building + ' - ' + str(self._flat))
