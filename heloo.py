"""def greetings(name):
    print("Hello," + name + "!")
greetings("max")
#required argument
def greetings(name):
    print("Hello," + name + "!")
greetings("class")#class as argument

#DEFAULT ARGUMENT
def greetings(name="World"):
    print("Hello," + name + "!")
greetings()
greetings("max")

#KEYWORD ARGUMENT
def divide(a,b):
    return a/b
result=divide(b=10,a=20)
print (result)
#ARBITERARY ARGUMENTS
def add_numbers(*args):
    return sum (args)
result = add_numbers(1,2,3,4)
print(result)
#here *args collects all  the passed arguments into a tuple and sum()function add them
def greetings (*names):
    for name in names:
        print(f"Hello,{name}!")
greetings("Madhan","risha","visakha")





#ARMSTRONG NUMBER
def armstrong_number(num):
    digit = str(num)
    power = len(digit)
    sum = 0
    for i in digit :
        sum+= int(i) ** power
    if sum == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
armstrong_number(153)



def print_details(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")
print_details(name="Madhav" , age=26, city= "Delhi")


def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item,price in products.items():
        print(f"{item}: {price}")
        total += price
    print(f"total:{total}")
shopping_cart(apple=15,orange=15,mango=10)

num=[3,2,6,8,4,6,2,9]
evens = list(filter(lambda x:x%2==0,num))
print(evens)

names=['alice','Bob','Ankit','Anurag']
give= list(filter(lambda x:x[0] in 'A',names))
print(give)

words = ['sun','planet','moon','jupiter','star']
length=list(filter(lambda x: len(str(x))>=4 , words))
print(length)



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers are:", prime_numbers)
words = ['AI','Data Science','Python']
length = list(map(lambda x: len(x),words))
print(length)
names = ['Alice','bob','rahul']
upper = list(map(str.upper,names))
print(upper)
#REDUCED FUNCTION IN THIS WE 
from functools import reduce
num = [3,2,6,8,4,6,2,9]
reduce_values =reduce(lambda a,b :a+b,num)
print(reduce_values)
#FIND MAX NO. FROM GIVEN LIST OF NUMBERS
from functools import reduce

numbers = [0,10,45,3,8]

max_num = reduce(lambda a,b: a if a>b else b,numbers)

print(max_num)
#FIND THE LONGEST STRING FROM THE GIVEN LIST OF WORDS
from functools import reduce
words = ["AI","Datascience","Python"]
largest_word = reduce(lambda a , b : a if len(a)>len(b) else b, words)
print(largest_word)
# remove empty strings from  a list 

words = ['AI','','MU']
empty = list(filter(lambda x:x!= "",words))
print(empty)
#OR
clean = list(filter(None,words)) 
print(clean)
# compute factorial of n = 5

from functools import reduce

n = 5
fact = reduce(lambda x, y: x * y, range(1, n + 1))
print(fact)
n = 5
fact = 1
for i in range (1,n+1):
    fact*=i
print(fact)

#convert all the names starting from 's' in uppercase
names = ['Sachin', 'ram','Sonali','riva']

#upper = list(map(lambda x: x.upper() if x.lower().startswith('s') else x, names))

#upper = [name for name in names if name.lower().startswith('s')]

upper = list(filter(lambda x: x . startswith('s'),names))
upper_names = list(map(str.upper,upper))
print(upper)

def app1(value):
    return 6 + square(value)
def square (x):
    return x *2
list1 = [1,2,3,4]
print(list(map(app1,list1)))

#HIGH ORDER FUNCTION
def app1 (fx,value):
    return 6+fx(value)
def square(x):
    return x * 2
def cube(x):
    return x ** 3
print(app1(square,4))#6*(square(4))= 6+8=14
print(app1(cube,2))#6*(cube(2))= 6+8=14

# global scope A varialble has global scope,if its created outside the function
a = 100
def demo():
    print(a)
print(a)
#call demo function 
demo()
print(a)
#LOCAL SCOPE
def demo():
    a = 100#local variable
print(a)#Trying to access local variable outside the function
#call the demo function
demo()

value1 = input("enter the first value")
value2 = input("enter the second value")
value3 = input("enter the third value")
list1 = value1,value2,value3

print(list1[0])
print(list1[1])
print(list1[2])
list1.append("code is life")
print(list1)
value4 = input("enter the first value")
value5 = input("enter the second value")
value6 = input("enter the third value")

list2 = [1,2,3]
list1.extend(list2)
print(list1)


#WAP TO INVERT A DICTIONARY . ASSUMING ALL VALUES AND KEYS ARE UNIQUE
# Original dictionary
o_d = {'a': 1, 'b': 2, 'c': 3}

inv_dic = {v: k for k, v in o_d.items()}

print(inv_dic)

#NEXT QUESTION
o_d = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

inv_dic = {}
for key, value in o_d.items():
    inv_dic.setdefault(value, []).append(key)
print(inv_dic)

word = "heloo"
char_count = {ch:word.count(ch) for ch in set(word)}
print(char_count)

d = {
    1:"aman",
    2:"suman",
    3:"aman",
    4:"rahul",
    5:"samay"
}
C = {}
text = input()
count = {}
for char in text :
    count[char] = count.get(char,0)+1
print("frequency: ")
for char ,counts in count .items():
    print(f"{char}:{counts}")


#FOR DICTIONRY IF WE HAVE TO CONCATENATE WE WILL USE - **  AND IN CASE OF TUPLE WE ONLY USE SINGLE *
dup ={}
for key,value in dup.items():
    if value not in dup:
        dup[key] = value
print(dict(sorted(dup,reverse=True)))"""

#GET A LIST OFF ALL VALUES OF A DOCTIONARY AND PRINT THE KEY WITH MAX VALUE
"""d = {
    'n1': 60,
    'n2': 30,
    'n3': 90,
    'n4': 35,
    'n5': 100
}

print("All values:", d.values())
max_value = max(d.values())
for k, v in d.items():
    if v == max_value:
        print("Key with max value:", k)




#CREATE A DICTIONARY WHICH DEFAULT VALUES OF EACH ELEMENT OF LIST ,TAKE DEFAULT VALUE AS "Unknown"
list = ["name","age","city" ,"roll no."]
dict = {}

for key in list:
    dict[key] = "Unknown"

print(dict)
#FROMKEYS WHICH TAKE TWO ARGUMENTS
d1 ={'n1':100 , 'n2':200}
d2 ={'n3':200, 'n4':400}
merge = {**d1,**d2}
print(merge)


#QUESTION PRACTICE take  n from  the user to take input values in that range and based on selected name 
# find the avg of list of marks corressponding to that name  
students = {
    "mallika": [52, 60, 48],
    "aryan": [44, 30, 32],
    "shreyan": [41, 57, 61]
}
n = int(input("Enter how many names u want to check : "))
for i in range(n):
    name = input("Enter student name: ")

    if name in students:
        marks = students[name]
        avg = sum(marks) / len(marks)
        print(f"Average marks of {name}")
    else:
        print("Name not found!")


n = int(input())
s = {}
for i  in range(n):
    name,*line = input().split()
    scores= list(map(int,line))
    s[name] = scores
name = input()
marks = s[name] 
avg= sum(marks) / len(marks)
print(avg)"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
res = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(res)