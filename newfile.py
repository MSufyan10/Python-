#My first code
print ("M.Sufyan")
print ("i am good")
a = ("apple")
print (a)
b = ("1")
print (a+b)
print ("Sufyan"+a+b)
#day 2
print ("i am a good boy i like mango")
print ("i am a good boy \nand i like mango")
print ("i am a \"good boy\" \nand i like apple")
print ("hi", 1, 2, sep="~")
print ("hi", 1, 2, sep="~", end="009")
print ("hi", 1, 2, end="009\n")
print ("Sufyan")
#day 3
a = 1 
print (a)
b = 199229292
print (b)
c = ("sufyan")
print (c)
d = True
e = 1.1
f = None

complex = (8, 2)
print (type(a))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
print (complex)

g = True
print ("i can speak english")
#list 
list1 = [8, 2.3, [-4, 5],["apple","banana"]]
print (list1) #collection of diffrent data elements is called list
#mutable means can be change
#unmutable means cannot be change

#tuple
tuple1 = (("parrot","sparrow"),("lion","tiger"))
print (tuple1) #unmutable

#dist #distionary
dist1 = {"name": "sufyan", "age": 20, "canVote" : True}
print (dist1)

#in python everything is object
# video 7

#operator  operator name  example
 #    +           addition          15+7
  #   -           subtraction       15-7
   #  *           multiplication   15*7
  #   /           division            15/7
  #   %          module           15%7
  #   //          floor division    15//7
  #   **          exponetial       5**3
 
print (5+6)
print (15-6)
print (15*6)
print (15/6)
print (15//6)
print (15%6)
print (5**3)

a = 45
b = 55
ans1 = a+b
print ("addition of" ,a, "and" ,b, "is", ans1)
ans2 = a-b
print ("subtraction of" ,a, "and" ,b, "is", ans2)
ans3 = a*b
print ("multiplication of" ,a, "and" ,b, "is", ans3)
ans4 = a/b
print ("division of" ,a, "and" ,b, "is", ans4)
ans5 = a**b
print ("exponetial of" ,a, "and" ,b, "is", ans5)
ans6 = a//b 
print ("floor division of" ,a, "and" ,b, "is", ans6)
ans7 = a%b
print ("module of" ,a, "and" ,b, "is", ans7)

#video 9
a = "7"
b = "7"
print (a+b) #answer is 77
#if i want to change the string to integer without changing the command
c = "7" 
d = "7"
print (int(a) + int(b)) #answer is 14

#Explicit conversion mean i am changing the function
c = "7" 
d = "7"
print (int(a) + int(b))

#implicit conversion mean python is changing the function
c = 1.9
d = 8
print (c+d)  #answer 9.9 #in implicit type casting python automaticaly change function with higher function
 
 #video 11
#how to make multi line comment
#first way
a = ("my name is Sufyan \ni am 17 years old") 
print (a)   
#second way is use (""") or (''')
apple = " " " my name is sufyan i am 17 years old i live in bustan " " "
print (apple)
#
name = ("sufyan")
print (name[0])    #s
print (name[1])    #u
print (name[2])    #f
print (name[3])    #y
print (name[4])    #a
print (name[5])    #n
#print (name[6]) error

#loop 
name = ("sufyan")
for character in name:
   print(character)  #answer s
                                 #u 
                                 #f
                                 #y
                                 #a
                                 #n
                                
#video 12 if i only want one of them
names = "muhammad,sufyan"
print (names[0:8]) #ans muhammad

#if i want to find the length of a string
names = "muhammad.sufyan"
print (len(names)) #ans 15

#
fruit = "mango"
len1 = len(fruit)
print ("mango is a",len1,"letter word")
#ans mango is a 5 letter word
#slicing
fruit = "mango"
mangolen = len(fruit)
print (mangolen) #ans 5
print (fruit[0:4])   # mang
print (fruit[:5]) #it automatically add 0
print (fruit[1:4]) #ng

#negative slicing
fruit = "mango"
#python automatically add len(fruit-3)
print (fruit[0:len(fruit)-3]) #ans ma 
print (fruit[0:-3]) #ans ma    
print (fruit[-1:-3]) #ans 
print (fruit[-3:-1]) #ans ng
#quiz
nm = "harry"
print (nm[-4:-2]) #ar

#video 13
#if you want to change the word into upper case or lower case use this
a = "Sufyan"
print (a.upper())  #ans SUFYAN
print (a.lower())  #ans  sufyan
# (rstrip)
# if i want to strip the exclamation mark i will use (rstrip)
a = "Sufyan!!!!!!!!"
print (a.rstrip("!")) #ans Sufyan

# (replace)
#if i want to change the string ex Sufyan to Subhan i will use (replace)
a = "Sufyan"
print (a.replace("Sufyan", "Subhan"))
#ans Subhan

#split
#if a want to split the strings
a = "sufyan subhan sameer"
print (a.split (" "))  #ans "sufyan","subhan","sameer"

#capitalize
#if you want to capitalize the first letter
a = "learning Python language"
print (a.capitalize()) 
#ans Learning python language

#center 
#if you want to aligns the string to the center
a = "welcome"
print (a.center(50)) #ans     welcome

#count
#if you want to know how many time a thing is in the string
a = "sufyan,ayan,aman,sufyan"
print (a.count("sufyan")) #ans  2

#endswith()
#if i want to to check if the string ends with a given value. true or false answer
a = "i am learning python !!!"
print (a.endswith("!!!")) #ans true
#we can even check for q value in between string by providing start and end position
a = "iam learning python"
print (a.endswith("le" , 2,6))  #ans true

#find()  #if you want to find the position of a string
a = "He's name is sufyan. he is a good boy"
print (a.find("is"))  #ans 10

#index  #same as find.if a given value is absent from the string then raise an exception
a = "i am a good boy"
print (a.find("aa")) #ans -1
#print (a.index("aa")) #ans error

#isalnum()  #if you want to find if your string is alpha numerical or not.(A-Z,a-z,0-9)
a ="iam a good boy"
print (a.isalnum())  #ans  True

#isalpha()  #if you want to find if your string is (A-Z,a-z) not 0-9 
a ="iam a good boy1"
print (a.isalpha())  #ans  False

#islower()  #if you want to know that every charactor is in lower case (a-z)
a = "i am a good boy"
print (a.islower())  #ans  True

#isprintable  #if you want to know the value you have given is printable or not
a ="i am a good boy"
print (a.isprintable())   #ans True
a = "i am a good boy\n"
print (a.isprintable())   #ans False

#isspace  #if you want to know if the string contains white spaces.
a = "           "
print (a.isspace())  #ans True


#istitle() #if you want to know that the first letter of each word is capitalize in the string
a = "Iam A Good Boy"
print (a.istitle())

#isupper()  #if you want to know that every charactor is in upper case (A-Z)
a = "IAM A GOOD BOY"
print (a.isupper())  #True

#startswith  #if you want to check if the string starts with given value.
a = "iam a good boy" 
print (a.startswith("iam")) #True

#swapcase()  #if you want to change the uppercase to lowercase or lowercase to uppercase
a = "Iam a Good Boy"
print (a.swapcase())  #iAM A gOOD bOY

#title  #if you want to capitalize each letter of the word in the string
a = "my name is sufyan"
print = (a.title())#ans My Name Is Sufyan

print = (a.title()) # My Name Is Sufyan

#video 14
# if-else statements.
# Some the programmes needs to check the evolution. of certain expressionist, whether the expression (5) False. If the expression evalua evaluate to Toue of to false, then the program execution follow different path then it would have it the expression had execu evaluted to True
#if-esle statement
a = int(input("Enter your age: "))
print ("your age is:" ,a)
if (a>=18):
   print ("you can drive")
else:
    ("you cannot drive")

#Enter your age 29
#your age is 29
#you can drive

#coditional operator
#>, <, >=, <=, ==, !=
a = int(input("Enter your age: ")) #ans18
print (a>18)  #ans False
print (a<=18) #ans True
print (a==18) #ans True
print (a!=18) #ans  False

#elif   #if i wqnt to execuite more than  one statement. #i can add multiple elif
num = int(input("Enter the value of num:"))
if (num < 0):
      print ("number is negative.")
elif (num ==0):
     print ("number is zero.")
else:
     print ("number is positive")
#ans if i input 17 #number is positive
#ans if i input 0 #number is zero
#ans if i input -7 #number is negqtive
 
 #Nested if statement 
 # we can use if, if-else,elif statement inside other if statement

num = int(input("Enter the number"))
if (num < 0):
    print ("number is negative.")
elif (num > 0):
    if (num <= 10):
        print ("number is between 1-10")
    elif (num > 10 and num <= 20):
        print ("number is between 11-20")
    else:
        print ("number is greater than 20")
else:
    print ("number is zero")
  #ans if you put 18 ans number is between 11 - 20
  
import time
name = input("Enter your name")
name = name.capitalize()
present_time =time.strftime("%H:%M:%S")
present_time = int(time.strftime("%H"))
if (4 <= present_time >= 12):
    print (f"Good morning {name}","its time:",present_time)
    print ("Thank you sir")
elif (12>= present_time <=5):
    print (f"Good afternoon {name}","its time:",present_time)
    print ("Thank you sir")
elif (5>=present_time<=8):
        print (f"Good evening {name}","its time:" ,present_time)
        print ("Thank you sir")
else:
        print (f"Good night {name}","its time:", present_time)
        print ("Thank you sir")

#loop #if i want to execuite a group of statement multiple time
#for loop      #while loop
#iterating over string 
name = "sufyan"    #ans   s
for i in name:        #       u
    print (i)            #        f
                         #         y
                         #         a
                         #        n
#iterating over list
colors = ["Red","Green","Blue","Yellow"]
for colors in colors:
    print (colors)       #ans  Red
                            #       Green
                            #       Blue
                            #       Yellow

colors = ["Red","Green","Blue","Yellow"]
for color in colors:   
   print (color)
   for i in color:
     print (i)
#ans
#R
#e
#d
#Green
#G
#r
#e
#e
#n
#Blue
#B
#l
#u
#e
#Yellow
#Y
#e
#l
#l
#o
#w

#range()    #if you want to print thousands of charactor
         #range (5) mean 0 to 4
for k in range (5):   #ans 0
   print (k)             #     1
                           #     2
                           #     3
                           #     4
                           
for k in range (5):   #ans 1
    print (k+1)        #       2
                          #      3
                          #      4
                          #      5

for k in range (1,20001):  #ans 1 
    print (k)                  # to
                                # 20000
#range for 3 charactor (x,y,z)
for k in range (1,12,3): #ans 1
    print (k)               #     4
                              #     7
                              #    10
#video 18
#while loop
i = 0
while (i<=3):
    print (i)
    i = i + 2
    
#else with while loop
count = 5
while (count > 0):
    print (count)
    count = count -1
else:
    print("Done")

#Break statements and Continue statements
#Break statement  #if you want to skip a part of a code or statement

for i in range (12):
    print ("5 ×", i + 1, " = ", 5 * (i + 1))
    
#ans 5 × 1  =  5
#5 × 2  =  10
#5 × 3  =  15
#5 × 4  =  20
#5 × 5  =  25
#5 × 6  =  30
#5 × 7  =  35
#5 × 8  =  40
#5 × 9  =  45
#5 × 10  =  50
#5 × 11  =  55
#5 × 12  =  60

#but if i use break statement
for i in range(12):
    if (i == 10):
        break
    print ("5×", i+1, "=", 5 * (i+1))
print ("Breaks at 10")

#ans
#5× 1 = 5
#5× 2 = 10
#5× 3 = 15
#5× 4 = 20
#5× 5 = 25
#5× 6 = 30
#5× 7 = 35
#5× 8 = 40
#5× 9 = 45
#5× 10 = 50
#Breaks at 10

#continue statement #if you want to break the whole loop 
#breaking out of loop
for i in range (12):
    if (i==10):
       print ("Skip the itretation")
       continue
    print ("5×", i, "=", 5 * (i))
#ans
#5× 0 = 0
#5× 1 = 5
#5× 2 = 10
#5× 3 = 15
#5× 4 = 20
#5× 5 = 25
#5× 6 = 30
#5× 7 = 35
#5× 8 = 40
#5× 9 = 45
#Skip the itretation
#5× 11 = 55

#Do while loop in pyton
i = 0
while True:     #ans  1 to 99 
    print (i)
    i = i + 1
    if (i%100 == 0):
        break

#function  #a function is a block of code that perform a specific task whenever it is called
#def mean function
a = 9
b = 8
c = 7
d = 6
def calculate (a, b):
    mean = (a*b)/(a+b)
    print (mean)
calculate (a, b)
calculate (c, d)
#ans
#4.235294117647059
#3.230769230769231

#we can use if or else function in def function too

a = 9
b = 8
c = 7
d = 6
def calculate (a, b):
    mean = (a*b)/(a+b)
    print (mean)
if (a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")
calculate (a, b)

#ans
#First number is greater
#4.235294117647059
#3.230769230769231


#pass function   #if you want to hold a code for later

a = 9
b = 8
c = 7
d = 6
def calculate (a, b):
    mean = (a*b)/(a+b)
    print (mean)
if (a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")
calculate (a, b)

def islesser(a,b):
    pass   #the progrom will not execuite it
    
#Function Argument amd return statement
#Default argument
def average (a,b):
    print ("The average is", (a+b)/2)
average (1,5)  #ans 3.0
#other  #if i give a value in function and give another value in print function is will execuite print function
#if i dont give another value in print fun
def name (fname, mname = "Ali", lname = "Ahmed"):
    print ("Hello,", fname, mname, lname)
name("M")  #ans M Ali Ahmed
#but if a give another value in print fun
def name (fname, mname = "Ali", lname = "Ahmed"):
    print ("Hello,", fname, mname, lname)
name ("M", "Sufyan","Ali")
 #ans  M Sufyan Ali
 
 #keyword function  #if i have provided a key value in def function like (a=5,b=7) so i dont have to be in order in print fun
def average(a=6, b=8):
    print ("The average is", (a+b)/2)
average(b=9, a=5) #ans will be same

#Required arugument #if i have not given a value in def function like (a,b) than i have to give a value in print fun
def average (a,b):
    print ("Thr average is", (a+b)/2)
average (a=5, b=7)  #ans 6

#Variable length arguments  #if i want to get a average of multiple number                                (*numbers)= tuple
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:" ,sum/ len(numbers))
average (5, 6, 7, 8, 9)  #ans 7.0

#lists            #if you want to put multiple things under one name
list1 = [1,2,3,4,5,6]
list2 = ["Red","Green","Blue"]
print (list1)    #ans [1,2,3,4,5,6]
print (list2)   #ans [Red Green Blue]

#list index (0,1,2,3)
print (list2[0])  #ans Red

#negative index
print (list1[-3])   #ans 4

#Check whether an item is present in list 
colors = ["Red","Green","Blue"]
if "Blue" in colors:
    print ("Yes")
else:
    print ("No")     #ans Yes
    
#same thing apply for strings
colors2 = ("Red ,Blue, Green")
if "Bl" in colors2:
    print ("Yes")
else:
    print ("No")      #ans Yes
  
#Slicing
print (colors[0:2])   #ans Blue Green

#jump index
list3 = [1,2,3,4,5,6,7,8]
print (list3[1:8:3])     #ans [2 5 8]

#list comprehension
list = [i*i for i in range(4)]
print (list)    #ans [0,1,4,9'']

#List method
#.append()    #if you want to add a value at the end of a list
l = [1,2,3,4]
l.append(7)
print (l)        #ans [1,2,3,4,7]

#.sort()        #if you want to sort the list in ascending order
l = [11,3,4,5,7]
l.sort()
print (l)     #ans  [3,4,5,7,11]

#.reverse()   #if yoi want to sort the list in decending order
l.reverse()
print (l)     #ans [11,7,5,4,3]

#index      #if yoi want find the position of a specific value in the list
print (l.index(3))    #ans 1

#.count()    if you want to count how many times a specific value have given in the list
print (l.count(5))   #ans 5

#copy()       #if you want to make a copy of a list 
m = l.copy()
print (l)        #[11,3,4,5,7]

#insert()     #if you want to insert a value in the list 
l.insert(1,34)    
print (l)     #ans [11,34,3,4,5,7]

#.extend()  #if you want to add a list into another list
m = [50,60,70]
l.extend(m)
print (l)     #ans [11,3,4,5,7,50,60,70]

#if you want to add a list into another list but don want to change the original list 
m = [50,70,90]
k = l+m
print (k)        #ans [11,3,4,5,7,50,60,90

#tuple     #we use roumd bracket and commas in tuple 
tup = (1,2,3,4,5)
print (tup)        #1,2,3,4,5
print (tup[0])      #1
print (tup[1])        #2
print (len(tup))    #5
if 2 in tup:
    print ("Yes")    #yes
    
#Manipulating tuple  #if you want to change tuple first convert it into list then you can change ot and then convert it into tuple again
countries = ("Pakistan", "Afghanistan", "Bangladesh", "Sri lanka")
countries2 = ("Vietnam", "India", "China")
southeastasia = countries + countries2
print (southeastasia)


#String formating in python  
#old method
letter = "Hey my name is {0} and i am from {1}"
name = "Sufyan"
country = "Pakistan"
print (letter.format(name, country))
#ans Hey my name is sufyan and i am from pakistan

#f-string in python  #new method
name = "Sufyan"
country = "Pakistan"
print (f"Hey my name is {name} and i am from {country}")

#other
price = 49.0999
txt = f"for only {price: 2f} dollar!"
print (txt)  #ans 49.999

#if you want print bracket with string use {{ }}
print (f"We use f-string like this: Hey my name is {{name}} and i am from {{country}}")  #ans We use f-string like this: Hey my name is {name} and i am from {country}

#Docstring in python  #docstring are like string that appear of the defination of a class,function,method,module
def square(n):
    ' ' 'Takes in a number n, return the square of n' ' '
    print (n**2)
square(5)
print (square.__doc__)
#ans     #25
#Takes in a number n, return the square of n

#same
def square(n):
    "Takes in a number n, return the square of n"
    print (n**2)
square(5)
print (square.__doc__)
#ans     #25
#Takes in a number n, return the square of n

#Recurision in python #we can call a functio back in function 
def factorial(n):
    if(n==0 or n==1):
      return 1
    else:
      return n * factorial(n-1)
print (factorial(5))  #ans 120 
            #5*4*3*2*1 = 120 this is factorial #other #fibocci series
def fibo(f):
    if(f==0 or f==1):
      return 1
    else:
      return f-1 + f-2
      
#python set  #in python we dont get value in order {}
s = {2,4,2,6}
print (s)     #ans {2,4,6} #we don't get repeated value
info = {"Carla",19, False, 5.9 ,19}
print (info) #ans {False, 19, 5.9, 'Carla'}
   #dont maintain order
for value in info:
    print (value) #False
                        #19
                        #5.9
                        #Carla

#Joining sets  #we can perform union and intersection in python 
#union() and update()
s1 = {1,2,5,6}
s2 = {3,5,7} #in union set are untouchable 
print (s1.union(s2))   #ans {1, 2, 3, 5, 6, 7}
print (s1,s2)  # {1, 2, 5, 6} {3, 5, 7}
s1.update(s2)  #it will update the original set

#intersection and intersection_update
#in intersection will will get the thing that is same in both set
cities  = {"Tokyo", "Karachi","Berlin","Lahore"}
cities2 = {"Tokyo","Seoul","Kabul","Karachi"}
cities3 = cities.intersection(cities2)
print (cities3) #ans {"Tokyo","Karachi"}
cities.intersection_update(cities2)
#it will update the original set 

#symmetric_difference and symmtric_difference_update
#in symmetric_diffrence we will get the value which isn't common in both set
cities  = {"Tokyo", "Karachi","Berlin","Lahore"}
cities2 = {"Tokyo","Seoul","Kabul","Karachi"}
cities3 = cities.symmetric_difference(cities2)
print (cities3)
#ans {'Kabul', 'Lahore', 'Seoul', 'Berlin'}
 

#difference() and difference_update()
#in difference () we will get A - B
cities  = {"Tokyo", "Karachi","Berlin","Lahore"}
cities2 = {"Tokyo","Seoul","Kabul","Karachi"}
cities3 = cities.difference(cities2)
print (cities3)
#ans {'Lahore','Berlin'}
                                          
#Set Methods
#isdisjoint()  #if you want to know that there is no common element in both set (True or False)
cities  = {"Tokyo", "Karachi","Berlin","Lahore"}
cities2 = {"Tokyo","Seoul","Kabul","Karachi"}
print (cities.isdisjoint(cities2)) #False

cities  = {"Tokyo1", "Karachi1","Berlin","Lahore"}
cities2 = {"Tokyo","Seoul","Kabul","Karachi"}
print (cities.isdisjoint(cities2)) #True

#issuperset() #if the value of set B in set A the ans will be True either False 
cities  = {"Tokyo", "Karachi","Berlin","Delhi"}
cities2 = {"Tokyo","Karachi"} 
print (cities.issuperset(cities2)) #True    

#issubset #if you want know if all the items of original set are present in particular set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
cities2 = {"Karachi","Madrid"}
print (cities2.issubset(cities)) #ans True 

#add()    #if you want to add a single thing in set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
cities.add("Lahore")
print (cities) #{'Karachi', 'Madrid', 'Tokyo', 'Lahore', 'Berlin'}

#update()   #if you want add more than one thing in set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
cities2 = {"Lahore","Delhi"}
cities.update(cities2)
print (cities) #{'Lahore', 'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Karachi'}

#remove()/discard() #if you want to remove somethifrom a set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
cities.remove("Tokyo")
print (cities) #{'Madrid', 'Karachi', 'Berlin'}
#The difference between remove and discard is that if you want to remove the value and it isn't available in the set remove will show error but discorddon't 
#pop     #pop method catches a random item from set 
cities = {"Tokyo","Madrid","Berlin","Karachi"}
item = cities.pop()
print (item)   #Berlin ans will be random

#del #if you want to delethe whole set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
del cities  #ans                                                          
#clear #if you don't want to remove the whole set
cities = {"Tokyo","Madrid","Berlin","Karachi"}
cities.clear()
print (cities)  

#if you want to check if an item exist in set
info = {"Carla",19,False,5.9}
if "Carla" in info:
    print ("yes")
else:
    print ("No")  #ans Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        