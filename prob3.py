# 🔹 Problem 3: Sum of Digits  
# Write a function that takes a non-negative integer and returns
#  the sum of its digits.  

 # Example 1
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n)) 

num = 1234
result = sum_of_digits(num)
print("Original:", num)         # output : Original: 1234          
print("Sum of Digits:", result) # output : Sum of Digits: 10  

# Example 2 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10 
    return total

num = 9876
result = sum_of_digits(num)
print("Original:", num)         #output : Original: 9876  
print("Sum of Digits:", result) #Output : Sum of Digits: 30  
