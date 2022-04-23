"""Task 0.9"""

"""This function returns the vowels from a single string value"""
def pvowels (string, vowels):
    solution = [word1 for word1 in string if word1 in vowels]
    print(solution)             

string = str(" ")
vowels = "AaEeIiOoUu"

pvowels('Umuzi', vowels)

print(("*" * 14) + "end")



