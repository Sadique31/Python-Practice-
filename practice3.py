
# Task 3 - Multiplication Table

def get_number():
    while True:
        try:
            num = int(input("Enter a positive number: "))

            if num > 0:
                return num
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid integer.")


def print_table_for(number):
    print(f"\nTable of {number} using for loop:")

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


def print_table_while(number):
    print(f"\nTable of {number} using while loop:")

    i = 1

    while i <= 10:
        print(f"{number} * {i} = {number * i}")
        i += 1


# Main program
num = get_number()

print_table_for(num)
print_table_while(num)
