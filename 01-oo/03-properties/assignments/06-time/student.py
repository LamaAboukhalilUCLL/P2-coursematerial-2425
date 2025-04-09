# Write your code here
# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes= minutes
#         self.seconds= seconds

#     @property
#     def hours (self):
#         return self.__hours
#     @hours.setter
#     def hours (self, value):
#         if not 0<= value<= 23:
#             raise ValueError("Hours must be between 0 and 23")
#         self.__hours= value

#     @property
#     def minutes(self):
#         return self.__minutes
#     @minutes.setter
#     def minutes(self, value):
#         if not 0<= value <= 59:
#             raise ValueError("Minutes must be between 0 and 59")
#         self.__minutes= value
        
#     @property
#     def seconds (self):
#         return self.__seconds
#     @seconds.setter
#     def seconds (self, value):
#         if not 0<= value<= 59:
#             raise ValueError("Seconds must be between 0 and 59")
#         self.__seconds= value
        
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours= hours
        self.minutes= minutes
        self.seconds= seconds
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, value):
        if 0<= value <=23:
            self.__hours= value
        else:
            raise ValueError ("Hour should be between 0 and 23")
    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, value):
        if 0<= value <=59:
            self.__minutes= value
        else:
            raise ValueError ("Minutes should be between 0 and 59")
    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self, value):
        if 0<= value <=59:
            self.__seconds= value
        else:
            raise ValueError ("Seconds should be between 0 and 59")
        

    