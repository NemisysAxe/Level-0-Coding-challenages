"""Task 0.7"""

"""The function will convert temperture from Celsius to Fahrenheit"""
def temp_C(x):
    multiplier = 1.8
    constant = 32
    temp_F = (x * multiplier) + constant
    
    print(str(temp_F) + " F")
    
    
temp_C(11)


