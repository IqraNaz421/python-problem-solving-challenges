
# 🔹 Problem 2: Count Vowels in a String  
# Write a function that counts the number of vowels 
# (a, e, i, o, u) in a string (case-insensitive).  

 # Example 1
def count_vowels(s):
    vowels = "aeiouAEIOU"  # Vowel characters (both lowercase & uppercase)
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

word = "Apple"
vowel_count = count_vowels(word)
print("Original:", word)               # Output : Original: Apple   
print("Vowel Count:", vowel_count)     # Output : Vowel Count: 2 

# Example 2
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels) 

sentence = "Hello, how are you?"
vowel_count = count_vowels(sentence)
print("Original:", sentence)
print("Vowel Count:", vowel_count)
