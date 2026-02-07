class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def print_first_name(self):
        print(self._first_name)

    def print_last_name(self):
        print(self._last_name)

    def print_full_name(self):
        print(self._first_name, self._last_name)
