"""x = int(input("x:50"))
y = int(input("y:50"))

if x == 0 or y == 0:
    print("value must be non zero")
else:
    gcd = 1
    i = 1
    while i <= x:
        if(x%i==0)and(y%i==0):
            gcd=i
        i+=1
        print("gcd:"<gcd)"""
"""ow = 5

for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()"""
"""password = input("Enter your password: ")
if len(password) >= 8:
    print("password is valid")
else:
    print("password is too short,it must contain more than 8 diit or 8 digit")"""
"""x = int(input("Enter your number: "))
if x%2==0:
        print("even")
else:
        print("odd")"""
"""has_fever = True
has_cough = True
has_rash = False
if has_fever:
    print("take fever medication")
if has_cough:
    print("take cough medication")
if has_rash:
    print("take cough medication")"""
"""sentence = "My class K25MP"
count = 0 
vowel = "aeiouAEIOU"
for ch in sentence :
    if ch in vowel:
        count += 1
print(count)

sentence = "My course coordinator"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longes_word):
        longest_word = word
print(longest_word)"""


"""username = input("My class")
password = input("12345 ")

match (username, password):
    case ("1234"):
        print("Login successful")
    case ("My class", "12345"):
        print("Login successful")
    case ("My class"):
        print("Login successful")
    case (_, _):   
        print("Invalid username or password")



predefined_username = "My class"
predefined_password = "12345"
username = input()
password = input()

if username == predefined_username:
        if password == predefined_password:
            print("login successfull")
        else:
            print("invalid password")
else:
        print("invalid username")



num = 5

if num == 0:
    print(0)
elif num == 1:
    print(0, 1)
else:
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(num - 2):   
        c = a + b
        print(c, end=" ")
        a = b
        b = c


num = int(input("Enter a number: 3"))
rev = 0
while(num>0):
    rev = num %10 
    rev = rev *10 +rev
    num //= 10
print("rev of a number is:", rev)



#check wheather a no. is prime or not:

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is neither prime nor composite")
else:
    is_prime = True
    for i in range(2, int(num)):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime number")
    else:
        print(num, "is a Composite number")

#pattern
for i in range(1, 5):  
    for j in range(1, 6):   
        print(i * j, end="\t")
    print()  

def celsius_to_fahrenheit(celsius): 
     fahrenheit=(celsius*9/5)+32
     return fahrenheit
print(celsius_to_fahrenheit(25))"""

def addition(a,b):
    return (a+b)

def subtraction(a,b):
    return (a-b)

def multiplication(a,b):
    return(a*b)

def division(a,b):
    return(a/b)
'''print("Addition:", addition(5, 8))
print("Subtraction:", subtraction(4, 3))
print("Multiplication:", multiplication(90, 12))
print("Division:", division(10, 2))'''
a = int(input())
b = int(input())
select = int(input("enter the operation you want to perform: "))
match select:
    case 1:
        print("a + b = ", addition(a,b))
    case 2 :
        print("a - b = ", subtraction(a,b) )
    case 3 :
        print("a * b = ", division(a,b) )
    case _ :
        print("default case")
        