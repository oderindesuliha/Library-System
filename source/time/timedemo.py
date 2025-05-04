class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value not in range(0, 24):
            raise ValueError(f'{value} is invalid')
            ' PM' if self.hour >= 12 else ' AM'
            value -= 12
            self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value not in range(0, 59):
            raise ValueError(f'{value} is invalid')
        self._minute = value

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if value not in range(0, 59):
            raise ValueError(f'{value} is invalid')
        self._second = value

    def set_time(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __str__(self):
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}'





t1 = Time(12, 30, 58)
t1.set_time(12, 25, 60)
t2 = Time()
t2.set_time(12, 30, 58)
print(t1)
print(t2)
