# Task 1 Student Result Calculator
def get_marks(subject):
    while True :
        try:
            marks = int(input(f"Enter {subject} marks :"))
            if(0 <= marks <=100):
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid whole number.")

english = get_marks("English")
maths = get_marks("Maths")
science = get_marks("Science")
social_science = get_marks("Social Science")
arts = get_marks("Arts")

total_marks = english + maths + science + social_science + arts

percentage_marks = (total_marks / 500) * 100
# Pass rule :
if english >=33 and maths >= 33 and science >= 33 and social_science >=33 and arts >=33 :
    print("The Student Got Pass ")
    if percentage_marks >= 90:
        print("Grade A : ")

    elif 80<=percentage_marks <90:
        print("Grade B")
    elif 70 <= percentage_marks < 80:
        print("Grade C") 
    elif 60 <= percentage_marks < 70:
        print("Grade D")
    elif 50 <= percentage_marks < 60:
        print("Grade E")
else:
    print("Result: FAIL")
    print("You must score at least 33 in every subject.")





