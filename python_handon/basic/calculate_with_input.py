    # Write a Python program that accepts an integer (n) and computes the value of 
    #n+nn+nnn. Go to the editor\n",
    # Sample value of n is 5 \n",
    # Expected Result : 615"
"""number = int(input("Enter a number: "))

def some(number):
    result=number+(number*11)+(number*111)
    return result

print(some(number))"""

a = int(input("Enter a number: "))
print(str(a) + str(a+a) + str(a+a+a))