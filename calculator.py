#  1.Function for operation
#  2.User input
#  3.print result

# Function to add numbers
def add(num1,num2):
    return num1+num2
# Function to subtract numbers
def subtract(num1,num2):
    return num1-num2
# Function to multiply numbers
def multiply(num1,num2):
    return num1*num2
# Function to divide numbers
def divide(num1,num2):
    return num1/num2
# Function to averge numbers
def avg(num1,num2):
    return( num1+num2)/2

# Step-2: user inpute
print("plese select a operation:\n"\
      "1.Addition\n"\
        "2.Subtract\n"\
            "3.Multiply\n"\
                "4.Divide\n"\
                    "5.Average\n")

select=int(input("select a operation from 1,2,3,4,5: ="))
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

# step-3  print the result
if select==1:
    print(number1,"+", number2,"=",\
          add(number1,number2))

elif select==2:
    print(number1,"-", number2,"=",\
              subtract(number1,number2))

elif select==3:
    print(number1,"*", number2,"=",\
              multiply(number1,number2))

elif select==4:
    print(number1,"/", number2,"=",\
              divide(number1,number2))
elif select==5:
    print("(",number1,"+",number2,")", "/","2", "=",\
         avg(number1,number2))
else:
    print("Invalid operation! pls select again!")    
     
    
        






