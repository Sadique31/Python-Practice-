# Task 2 - Number Analyzer

def get_number():
    while True:
        try:
            num = int(input("Enter a number:"))
            return num
        except ValueError:
            print("Please Enter a valid number")



# Check number is postive negative or zero 

def check_property(num):
    if(num == 0):
        print("Number is Zero")
        
    elif num > 0 :
        print("Number is Positive")
        total = 0
        for i in range(1, num + 1):
          total = total + i
          
        print("Sum:", total)
    else:
        print("Number is Nagative")

# check number is even or odd 

def check_evenOrOdd(num):
    if num % 2 ==0 :
        print("Number is Even ")
    else:
        print("Number is Odd")

number = get_number()

check_property(number)
check_evenOrOdd(number)