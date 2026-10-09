#operator overloading in python #operator overloading is a feature in Python that allows developers to redefine the behaviour of mathematical and comparison operator for custom data types
class vector:
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j
        self.k = k
        
    def __add__(self, x):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
v1 = vector(3, 5, 6)
v2 = vector(1, 2, 9)
print (v1 + v2)  #4i + 7j + 15k

#single inheritance in python # Single inheritance is a type of inherence where a class inherence properties and behavior from a single parent class
class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound (self):
        print ("sound made by the animals")       
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "dog")
        self.breed = breed
    def make_sound(self):
        print ("Bark")
        
d = dog("dog", "doggerman")
d.make_sound() #Bark

a = animal("dog", "dog")
a.make_sound() #sound made by the animals

#multiple inheritance #multiple inheritance is a powerful feature in oop that allows a class to inherts attributes and methods from multiple parent classes
class Employee:
    def __init__(self, name):
        self.name = name
        
class Dancer:
    def __init__ (self, dance):
        self.danec = dance
      
class DancerEmployee:
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
o = DancerEmployee("kathak", "Shivani") 
print (o.name) #ans Shivani
print (o.dance)  #ans kathak

#Multilevel inheritance  # Multi-Level inheritance is a type of inheritance in oop where a defined class inherits from another drived class 
class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print (f"Name: {self.name}")
        print (f"Species: {self.species}")
        
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "dog")
        self.breed = breed
        
    def show_details(self):
        animal.show_details(self)
        print (f"Breed: {self.breed}")

class GoldenRetriever(dog):
    def __init__(self, name, color):
        dog.__init__ (self, name, breed = "Golden Retriever")
        self.color = color
    
    def show_details(self):
        dog.show_details(self)
        print (f"color: {self.color}")
        
o = GoldenRetriever ("Tommy", "Black")  
o.show_details() #ans Name: Tommy
                       #Species: dog
                     #Breed: Golden Retriever
                       #color: Black
                       
#Hybrid inheritance #hybrid inheritance is a combination of multiple inheritance and single inheritance. it is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single drived class        
class Baseclass:
    pass
   
class Drived1(Baseclass):
    pass
    
class Drived2(Baseclass):
    pass
    
class Drived3(Drived1, Drived2):
    pass
    
#Hierarchical inheritance #hierarchical inheritance is a type of inheritance where multiples subclasses inherit form a single base class. in other words a bese class act as a parent class for multiple sub classes
class Baseclass:
    pass  
    
class D1(Baseclass):
    pass
    
class D2(Baseclass):
    pass
    
class D3(D1):
    pass

#Time module in python #the time module provide set of function that work with time related operation

#time.time()   #The time.time() function return the current time as a floating point number representing the number of second since the epoch (the point in the time when the time model was initialised)
import time
print (time.time()) #ans1785305586.345269

#time.sleep()   #The time.sleep function suspend the execution of the code for specified number of second
import time
print ("Start:", time.time())
time.sleep(3)
print ("End:", time.time())
#Start: 1785305718.7219048
#the code will take 3 second for the other code to execute 
#End: 1785305721.7222514

#time.strftime() #The time.strftime function formats time value is a string,base on a specific format. this function is particularly useful for formatting date and time
import time
t = time.localtime()
formatted_time = ("%Y-%M-%D %H:%M:%S", t)
print (formatted_time)
#ans ('%Y-%M-%D %H:%M:%S', time.struct_time(tm_year=2026, tm_mon=7, tm_mday=29, tm_hour=11, tm_min=40, tm_sec=1, tm_wday=2, tm_yday=210, tm_isdst=0))

#Creating mind line utilities in Python 
#command line utility are program that can be run from the terminal or command line interface and they are essential part of many development works flows #didn't understand 

#walrus operator #the walrus operator allows you to assign a value to a variable with in an expression. this can be useful when you need to use a value multiple time in a loop. but didn't want to repeat the calculation
#without walrus
foods = list()
while True:
    food = input("what food do you like? :")
    if food == "quit":
        break
foods.append(food)

#with walrus
foods = list()
while (food := input("What food do you like? :")) != "quit":
    foods.append(food)
    
#import shutil

#shutil.copy # This function copies the file located at src to a new location is specified by dst
import shutil
shutil.copy ("main.py", "main.py2")
    
#shutil.copy2() # This function is similar to shutil.copy but It also preserve more metadata about the original file such as time.stamp
shutil.copy2("main.py2", main.py2)

#shutil.copytree(src, dst) # This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists it will merge the original file with it
shutil.copytree("tutorial", "mytutorial")

#shutil.move() #This function move the file located at src to a new location specified by dst
shutil.move("tutorial/file.file", "file.file")

#request module # This module is a HTTP library that enables developers to send HTTP request in Python this module enables you to send HTTP request using python code and make it possible to interact with Apis and web services

#pip install request 

import requests
response  = request.get("http://wee.google.com")
print (response.text) # i will get all the html code of google.com

#Generators # Generator are special type of function that allows you to create an iterable sequence of values. a generated function returns a generator object. which can be used to generate the value one by one
#we use yield function to generate value
def my_generator():
    for i in range(5):
        yield i
        
gen = my_generator()
print (next(gen)) #ans 0
print (next(gen)) #ans 1
print (next(gen)) #ans 2
print (next(gen)) #ans 3
print (next(gen)) #ans 4

#function caching #function caching is a technique for improving the performance of a program by storing the result of a function call so that you can reuse the result instead of recomputing them every time the function is called
#function caching can be achieved using the functool.lru_cache decorator

import functools
import time
@functool.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print (fx(20)) 
print ("done for 20") 
print (fx(2))
print ("done for 2")
#but if we print them again it will not take time    
print (fx(20))
print ("done for 20")
print (fx(2))
print ("done for 2")
#ans 100 it will take 5 second 
#ans done for 20
#ans 10 it will take 5 second 
#ans done for 2
#ans 100 it will not take time
#ans done for 20
#ans 10  it will not take time
#ans done for 2

#Regular expression # Regular expression or regex for short are a powerful tool for working with strings and text data in Python they allows you to match and manipulate strings based on patterns making it easy to perform complex string operation with just a #line of code
#[] represent a character class
#^ matches the beginning 
#$ matches the end
#. matches any character except new line
#| means or (matches with any of the characters separated by it.)
#* any number of occurrence (including o
#0 occurrence)
#+ one or more occurrences
#{} indicate number of occurrences of a precdingRe to match
#() enclose a group of REs
import re
pattern  r"expression" #what do you want to find
text "Hello, world!" #The text
match = re.search (pattern, text)
if match:
    print ("match found")
else:
    print ("match not found")

import re
pattern = "was"
text = ' ' 'i was living in a town then i moved to karachi for higher studies it was fun' ' '
match = re.search(pattern, text)     
#ans space(4, 7) match "was"

#Async IO #async is a programming pattern that allows for higher performance IO operations in a concurrent and non blocking manners. Async programming is achieved through the use of the async io module and asynchronous function
import asyncio
async def my_async_function():
    await asyncio.sleep(1)
    return "Hello world"
    
async def main():
    result = await 
my_async_function
    print (result)
  
asyncio.run(main())

#Multi threading #multi trading is a technique that allows multiplex of execution to run with in a single process we can use threading process to implement multithreading 

import threading
def my_func():
    print ("Hello from thread", threading.current_thread().name)
thread = threading.Thread(target=my_func)
 
thread.start()
thread.join()

#multiprocessing # Multiprocessing it is a module That provides a single way to run multiple processes in parallel. it allows you to take advantage of multiple cores and processors on your system and can significantly improve the performance of your code
import multiprocessing
def my_func():
    print ("Hello from process", multiprocessing.current_process().name)
process = multiprocessing.process(target=my_func)

process.start()
process.join()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      