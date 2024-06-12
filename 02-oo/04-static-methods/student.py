class Duration:

    def __init__(self, *, durationInSeconds):
        self.__durationInSeconds=durationInSeconds

    @staticmethod
    def from_seconds(amount):
        return Duration(durationInSeconds=amount)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(durationInSeconds=amount*60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(durationInSeconds=amount*3600)
    
    @property
    def seconds(self):
        return self.__durationInSeconds

    @property
    def minutes(self):
        return self.__durationInSeconds / 60

    @property
    def hours(self):
        return self.__durationInSeconds / 3600