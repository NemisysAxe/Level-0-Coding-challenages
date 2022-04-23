"""Task 0.6"""

"""This function returns the highest of three vaules"""
def maximum(value1, value2, value3):
    if (value1 > value2 and value1 > value3):
        print(value1)    
    elif (value2 > value1 and value2 > value3):
         print(value2)
    elif (value3 > value1 and value3 > value2) :
        print(value3)
    
maximum(50, 60, 5)

"""Bonus"""
    
def maximum(*x):
    result = x[0] 
    for values in x:
        if values > result:
            result = values
    print(result)

maximum(1,22,3,2)




