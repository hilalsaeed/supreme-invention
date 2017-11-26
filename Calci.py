from math import *
from mpmath import *
while True:
   print("Your Choices: ")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'pow' to calculate power of a number")
   print("Enter 'fact' to calculate factorial")
   print("Enter 'exp' to calculate exponential power")
   print("Enter 'log' to calculate log")
   print("Enter 'Sin' for Sine value")
   print("Enter 'Cos' for Cosine value")
   print("Enter 'Tan' for Tangent value")
   print("Enter 'Sec' for Sec value")
   print("Enter 'Cosec' for Cosec value")
   print("Enter 'Cot' for 'Cot value")
   print("Enter 'quit' to end the program")
   i=input('Enter your choice fella')
   if i == "quit":
      break
   elif i == "add":
      x=float(input('Enter 1st number'))
      y=float(input('Enter 2nd number'))
      print('Addition of numbers entered: '+str(2+3))
   elif i == "subtract":
      x=float(input('Enter 1st number'))
      y=float(input('Enter 2nd number'))
      print('Difference of numbers entered: '+str(x-y))
   elif i == "multiply":
      x=float(input('Enter 1st number'))
      y=float(input('Enter 2nd number'))
      print('Product of numbers added: '+str(x*y)) 
   elif i == "divide":
      x=float(input('Enter 1st number'))
      y=float(input('Enter 2nd number'))
      print('Division of numbers entered: '+(x/y))
      print('Remainder after division: '+str(x%y))
   elif i=='pow':
      x=float(input('Enter power value'))
      y=float(input('Enter number'))
      print('Result: '+str(x**y))
   elif i=="log":
      x=int(input("Enter base"))
      y=float(input("Enter value"))
      print("Result of log base",x,y,":",log(y,x))
   elif i=='fact':
      x=int(input("Enter value"))
      print("Factorial of number",x,":",factorial(x))
   elif i=='exp':
      x=float(input("Enter power of exponent"))
      print("Exponent of power",x,":",exp(x))
   elif i=='Sin':
      x=radians(float(input("Enter value")))
      print("Sine(",degrees(x),")",sin(x))
   elif i=='Cos':
      x=radians(float(input("Enter value")))
      print("Cosine(",degrees(x),")",cos(x))
   elif i=='Tan':
      x=radians(float(input("Enter value")))
      print("Tan(",degrees(x),")",tan(x))
   elif i=='Sec':
      x=radians(float(input("Enter value")))
      print("Sec(",degrees(x),")",sec(x))
   elif i=='Cot':
      x=radians(float(input("Enter value")))
      print("Cot(",degrees(x),")",cot(x))
   elif i=='Cosec':
      x=radians(float(input("Enter value")))
      print("Cosec(",degrees(x),")",csc(x))
   else:
      print("Unknown input")
