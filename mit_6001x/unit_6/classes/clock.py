# class Clock(object):
#     def __init__(self, class_time, class_day):
#       self.time = class_time
#       self.day = class_day
#     def print_time(self, time, day):
#       print(time, day)
#       print(self.time)
#       print(self.day)

# clock = Clock('5:30', 'Mon')
# clock.print_time('10:30', "Tue")


class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print(self.time)


boston_clock = Clock("5:30")
paris_clock = boston_clock
paris_clock.time = "10:30"
boston_clock.print_time()
Clock("asdf").time = "20:30"
new_clock = Clock("5:30")
# new_clock.time = 'asdfasdf'
new_clock.print_time()
