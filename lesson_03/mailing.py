class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self._to_address = to_address
        self._from_address = from_address
        self._cost = cost
        self._track = track

    def show(self):
        from_adr = self._from_address.to_string()
        to_adr = self._to_address.to_string()
        print('Отправление', self._track,
              'из', from_adr,
              'в', to_adr + '. Стоимость',
              self._cost, 'рублей.')
