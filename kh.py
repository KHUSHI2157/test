"""ch = str(input("a: "))
match ch:
    case ch if ch =="a,e,i,o,u""A,E,I,O,U" :
        print("vowel")
    case _:
        print("consonent")
ch = input("Enter a single character: ").lower()  

match ch:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"{ch} is a Vowel")
    case _ if ch.isalpha() and len(ch) == 1:
        print(f"{ch} is a Consonant")
    case _:
        print("Invalid input! Please enter only one alphabet letter.")"""


num = [3,2,6,8,4,6,2,9]
even = list(map(lambda x:x*2,num))
print(even)

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c:c*9/5+32,celsius))
print(fahrenheit)
