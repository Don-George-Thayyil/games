class Timer:
    def __init__(self, hour, minute, second):
        self.hour = self.mod_hour = hour
        self.minute = self.mod_min = minute
        self.second = self.mod_sec = second
        

    def __str__(self):
        if self.hour < 10:
            self.mod_hour = "0"+str(self.hour)
        else:
            self.mod_hour = self.hour
        if self.minute < 10:
            self.mod_min = "0"+str(self.minute)
        else:
            self.mod_min = self.minute
        if self.second < 10:
            self.mod_sec = "0"+str(self.second)
        else:
            self.mod_sec = self.second
        
        return str(self.mod_hour) + ":" + str(self.mod_min) + ":" + str(self.mod_sec)
        
    def next_second(self):
        # if self.hour == 59 and self.minute == 59 and self.second == 59:
        #     self.second = self.minute = self.hour = 00
        self.second += 1
        if self.second > 59:
            self.minute += 1
            self.second = 00
        if self.minute > 59:
            self.hour += 1
            self.minute = 00
        if self.hour > 23:
            self.hour = 00
    def prev_second(self):
        self.second -= 1
        if self.second < 0:
            self.minute -= 1
            self.second = 60 + self.second
        if self.minute < 0:
            self.hour -= 1
            self.minute = 60 + self.minute 
        if self.hour < 0:
            self.hour = 24 + self.hour


timer = Timer(0, 5, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
