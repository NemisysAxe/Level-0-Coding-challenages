#Task 0.1
import string
from unittest import result


x = 0
y = 1
print(x)
print(y)

x = x + 3
y = y + x

print(x)
print(y)

print(("*" * 14) + "end")


#Task 0.2
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + (1 * 2)
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2) / 2

print(x) 
print(y) 
print(z) 
print(a) 
print(b)

print(("*" * 14) + "end")

#Task 0.3

def hello():
    new_value = "Hello " + str("Tshepo")
    print(new_value)
    
hello()

print(("*" * 14) + "end")

#Task 0.4
def even_or_odd(value):
    
    if value % 2 == 0:   
        print("even") 
    else : 
        
        if value % 2 != 0: 
         print("odd")
        
even_or_odd(80)

print(("*" * 14) + "end")


#Task 0.5

def triangle_area(constant, height, breath):
    #constant = 0.5
    tri_area = constant * height * breath
    print(tri_area)
    
triangle_area(0.5, 10, 6)

print(("*" * 14) + "end")


#Task 0.6
def maximum(value1, value2, value3):
    if (value1 > value2 and value1 > value3):
        print(value1)    
    elif (value2 > value1 and value2 > value3):
         print(value2)
    elif (value3 > value1 and value3 > value2) :
        print(value3)
    
maximum(50, 60, 5)

#Bonus
    
def maximum(*x):
    result = x[0] 
    for values in x:
        if values > result:
            result = values
    print(result)

maximum(1,22,3,2)

print(("*" * 14) + "end")


#Task 0.7
def temp_C(x):
    """The function will convert temperture from Celsius to Fahrenheit"""
    multiplier = 1.8
    constant = 32
    temp_F = (x * multiplier) + constant
    
    print(str(temp_F) + " F")
    
    
temp_C(11)


print(("*" * 14) + "end")


#Task 0.8
def time(t):
    hours = (t // 60) 
    minutes = (t % 60)
    print((str(hours) + " hour") + " " + ( str(minutes) + " minutes") )

    
time(71)

print(("*" * 14) + "end")

#Task 0.9
def pvowels (string, vowels):
    solution = [word1 for word1 in string if word1 in vowels]
    print(solution)             

string = str(" ")
vowels = "AaEeIiOoUu"

pvowels('Umuzi', vowels)

print(("*" * 14) + "end")


#Task 0.10
#def pvowels (string1, string2, vowels):
    #solution1 = [word2 for word2 in string1 if word2 in vowels]
   # print(solution1)
    
    #solution2 = [word3 for word3 in string2 if word3 in vowels]
   # print(solution2)             
             

#string1 = str(" ")
#string2 = str(" ")
#vowels = "AaEeIiOoUu"

#pvowels(string1, string2, vowels);

#pvowels('house', 'computers', vowels)

