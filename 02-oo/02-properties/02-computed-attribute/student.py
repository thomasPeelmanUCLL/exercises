# Write your code here

class BMICalculator:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    @property
    def bmi(self):
        return self.__weight / (self.__height ** 2)

    @property
    def category(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 24.9:
            return "Normal weight"
        elif self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def __str__(self):
        return f"Weight: {self.weight}, Height: {self.height}, BMI: {self.bmi}, Category: {self.category}"