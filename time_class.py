class Time:
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.day = 1

        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def __str__(self):
        return "Day {} {}:{:02d}:{:02d}".format(self.day, self.hour, self.minute, self.seconds)


    def __add__(self, other_time):
        new_time = Time()

        if(self.seconds + other_time.seconds) >= 60:
            self.minute += 1
            new_time.seconds = (self.seconds + other_time.seconds) - 60
        else:
            new_time.seconds = self.seconds + other_time.seconds

        if(self.minute + other_time.minute) >=60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = (self.minute + other_time.minute)

        if(self.hour + other_time.hour) > 23:
            new_time.day +=1
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = (self.hour + other_time.hour)

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(26, 41, 30)
    print(time2)

    print time1 + time2
main()