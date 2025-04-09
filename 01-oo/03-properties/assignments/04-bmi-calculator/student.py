
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg= weight_in_kg
        self.height_in_m= height_in_m
        self.__bmi= (weight_in_kg)/ (height_in_m**2) 

    @property
    def bmi(self):
        return self.__bmi
     
    def __category(self):
        if self.__bmi < 18.5:
            return "underweight"
        elif 18.5<= self.__bmi < 25:
            return "normal"
        else:
            return "overweight"
    @property
    def category(self):
        return self.__category()


