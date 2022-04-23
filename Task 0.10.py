"""Task 0.10"""

"""This function returns the vowels from two string input"""
def prvowels (string1, string2, vowels):
    solution1 = [word2 for word2 in string1 if word2 in vowels]
    print(solution1)
    
    solution2 = [word3 for word3 in string2 if word3 in vowels]
    print(solution2)             
             
string1 = str(" ")
string2 = str(" ")
vowels = "AaEeIiOoUu"

prvowels(string1, string2, vowels);

prvowels('house', 'computers', vowels)



