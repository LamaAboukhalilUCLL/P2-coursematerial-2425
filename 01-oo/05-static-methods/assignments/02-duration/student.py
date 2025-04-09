class Duration:
    def __init__(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
    
    @staticmethod
    def from_seconds(seconds):
        # Calculate minutes and hours from seconds
        minutes = seconds / 60
        hours = seconds / 3600
        # Return a new Duration object
        return Duration(seconds, minutes, hours)
    
    @staticmethod
    def from_minutes(minutes):
        # Similar conversion logic
        seconds=minutes*60
        hours= minutes/60
        # Return a new Duration object
        return Duration(seconds, minutes, hours)
        
    @staticmethod
    def from_hours(hours):
        # Similar conversion logic
        seconds= 3600* hours
        minutes= 60* hours
        # Return a new Duration object
        return Duration(seconds, minutes, hours)
    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours


# class Duration: WRONG!!!  
#     def __init__(self,seconds, minutes, hours):
#         self.__seconds=seconds
#         self.__minutes=minutes
#         self.__hours=hours
#     #using static methods as factory methods to return new objects 
#     @staticmethod
#     def from_seconds(seconds):
#         return Duration.from_seconds(seconds) #we return an object in this case it is called duration
#     @staticmethod
#     def from_hours(hours):
#         return Duration.from_hours(hours)
#     @staticmethod
#     def from_minutes(minutes):
#         return Duration.from_minutes(minutes)
#     #readonly properties for the time attributes
#     @property
#     def seconds(self):
#         if self is Duration.from_seconds:
#             return self.__seconds
#         elif self is Duration.from_hours:
#             return 3600*self.__hours
#         else: #if self is Duration.from_minutes
#             return 60*self.__minutes
#     @property
#     def hours(self):
#         if self is Duration.from_hours:
#             return self.__hours
#         elif self is Duration.from_minutes:
#             return self.__minutes/60
#         else: #if self is Duration.from_seconds
#             return self.__seconds/3600
#     @property
#     def minutes(self):
#         if self is Duration.from_minutes:
#             return self.__minutes
#         elif self is Duration.from_hours:
#             return 60*self.__hours
#         else: #if it is Duration.from_seconds
#             return self.__seconds/60
    
    
    




    

    

