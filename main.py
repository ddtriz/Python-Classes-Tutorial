#BASIC KNOWLDEGE ABOUT CLASSES



#What is a class?

class firstClass():#Determine a class in the code by using [class]
  name = ""
  identification = 0
  
  print ("hello")


firstClass.name = "John"
firstClass.identification = 326536123
#If you print the firstClass you'll get something like <class  '__main__.firstClass>
#That's because you're printing the class and not any attribute of it.
#You can call them by using the [.] after firstClass
#if you have a print in your class and you call it
#(firstClass())
#it will act like a function. (In this case it will print #hello, as I wrote print("hello") in the class.)

firstClass() #OUTPUT:[ hello ]
print(firstClass)#OUTPUT:[ <class '__main__.firstClass> ]
#Output using Attributes! :D
print(firstClass.name)#OUTPUT:[ Jhon ]
print(firstClass.identification)#OUTPUT:[ 326536123 ]

#You can also create objects to use better classes.
#It's like importing something as something. Example:
#import pyaudio as pA
#pA.listen() bla bla bla
#You can do the same with classes. Just assign a name to the class:
fC = firstClass()
fC.name = "Rose"
fC.identification = 112233445566

#That's all the basics about the classes, at least I think.


#hope you like it and understood it.