#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! " + "You are " + age)
"""num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)"""

"""print("Roses are {color}")
print("{plural noun} are blue")
print("I love {celebrity}")
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)"""

##Lists
"""lucky_numbers = [8,13,23,2,4,5,15,30]
friends = ["Kevin", "Jin", "Karen", "Jolie"]
friends2 = friends.copy()
#friends.append("Luke")
#friends.insert(2,"Kelly")
#friends.remove("Jin")
#friends.clear()
#friends.pop()
#friends.extend(lucky_numbers)
#print (friends[1:2])
#print(friends.count("Jin"))
#friends.sort()
#friends.reverse()
print(friends2)"""

###Tuples are unmutable, doesnt accept changes
"""coordinates = [(4, 5), (8, 9), (50, 85)]
coordinates[1] = 10
print(coordinates[0])"""

###Functions

"""def say_hi(name, age):
    print("Hello " + name + " you are " + age)
say_hi("Maria", "50")
say_hi("Marco", "45")"""

###Return Statement

"""def cube(num):
   return num*num*num

result = cube(5)
print(result)"""

### if Statement

"""is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")"""

"""is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are neither male or tall or both")"""

# Compare operators

"""def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(20, 50, 10))"""

"""def max_str(str1, str2, str3):
    if str1 == str2 and str1 != str3:
        return str1
    elif str2 != str1 and str2 == str3:
        return str2
    elif str3 == str1 and str3 != str2:
        return str3
    else:
        return

print(max_str("Bananas brancas", "Laranjas laranja", "Limoes verdes"))"""

# Improved Calculator

"""numero1 = float(input("Enter first number: ")) #float convert strings into integer
operador = input("Enter operator: ")
numero2 = float(input("Enter second number: "))"""

"""def operator(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
         return "Invalid operator"

result = operator(operador, numero1, numero2)
print(result)"""
"""p1 = float(input("Enter first number: ")) #float convert strings into integer
ope = input("Enter operator: ")
p3 = float(input("Enter second number: "))

print(operator(ope, p1, p3))"""

## Dictionary
'''monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["01"])
print(monthConversions.get("1", "Not a valid key"))'''

"""### While Loop

i = 1
while i <= 10:
    print(i)
    i += 1
print("While loop stop")"""

"""### Basic Guessing Game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess= input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You are out of guesses")
else:
    print("You win!")"""