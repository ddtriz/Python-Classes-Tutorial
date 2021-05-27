class firstClass():
  name = ""
  identification = 0
  
  print ("hello")


firstClass.name = "John"
firstClass.identification = 326536123
#If you print the firstClass you'll get something like <class  '__main__.firstClass>
#That's because you're printing the class and not any attribute of it.
print(firstClass)
#You can call them by using the [.] after firstClass
#if you have a print in your class and you call it
#(firstClass())
#it will act like a function. (In this case it will print #hello, as I wrote print("hello") in the class.)

firstClass() #OUTPUT: hello
print(firstClass)#Output: 




fC = firstClass()

