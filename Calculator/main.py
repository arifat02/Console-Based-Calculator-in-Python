import math
#Enter the type of Operation

operation = input("Enter operation: ")
if operation == "+":
    print(int(input("Enter first number: "))+ int(input("Enter second number: ")))
elif operation == "-":
    print(int(input("Enter first number: ")) - int(input("Enter second number: ")))
elif operation == "*":
    print(int(input("Enter first number: ")) * int(input("Enter second number: ")))

#For Division : Number/0 = Math Error

elif operation == "/":
     numerator=int(input("Enter First number : "))
     denominator=int(input("Enter Second number: "))
     if denominator!=0:
         print(numerator/denominator)
     else:
         print("Math Error")
elif operation == "^":
    print(int(input("Enter base : "))**int(input("Enter exponent : ")))

    #For SquareRoot : Squareroot Of (-)Negative number = Math error

elif operation == "sqrt":
      number=int(input("Enter number : "))
      if number>= 0:
          print(math.sqrt(number))
      elif number < 0:
          print ("Math Error")
else:
    print("Invalid operation")