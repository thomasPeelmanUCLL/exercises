class LenghtConverter:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def meters(self):
        return self._value

    @property
    def inches(self):
        return self._value * 39.3701

    @property
    def feet(self):
        return self._value * 3.28084

    @property
    def yards(self):
        return self._value * 1.09361

    @property
    def miles(self):
        return self._value * 0.000621371

    @property
    def kilometers(self):
        return self._value / 1000

    @property
    def centimeters(self):
        return self._value * 100

    @property
    def millimeters(self):
        return self._value * 1000

    @property
    def __str__(self):
        return f'{self._value} m'

    @value.setter
    def value(self, value):
        self._value = value