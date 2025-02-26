# If-Else: Build a Student Grade Evaluator
# 1. Input a Grade
# Question: Ask the user to input a grade (0-100) and store it in a variable. Print the entered grade.

grade = int(input("Please enter your grade: "))
print(f"Your entered grade {grade}")


# 2. Determine Pass/Fail
# Question: Use an if-else statement to print "Pass" if the grade is 50 or above, and 
# "Fail" if it is below 50.

if grade >= 50:
    print("Pass")
else:
    print("Sorry, you've failed")

# 3. Assign Letter Grades
# Expand the evaluator to assign a letter grade. For example, 90 
# and above is "A", 80-89 is "B", 70-79 is "C", 60-69 is "D", and 
# below 60 is "F". Print the letter grade.

# def get_grade_letter(grade):

#     if grade >= 90:
#         letter="A"
#     elif grade >= 80:
#         letter="B"
#     elif grade >= 70:
#         letter="B"
#     elif grade >= 60:
#         letter="D"
#     else:
#         letter="F"
    
#     return letter

# gl = get_grade_letter(grade)
# print("For your grade, the letter is: ", gl)

# # 4. Provide Feedback Comments
# # Question: Based on the letter grade, use if-else statements to print a feedback 
# # comment. For example, if "A" print "Excellent work!", "B" print "Good job!", "C" 
# # print "You can improve.", "D" print "Needs more effort.", and "F" print "Please see 
# # your instructor.". Amedn the previous function to help you with this!


# if gl == "A":
#     feedback = "Excellent work!"
# elif gl == "B":
#    feedback = "Good job!"
# elif gl == "C":
#    feedback = "Your can improve!"
# elif gl == "D":
#    feedback = "Needs more effort!"
# else:
#     feedback = "Please see your instructor"
# print(f"Your feedback is: {feedback}")

# 5. Complete Grade Evaluator Function
# Question: Wrap the code into a function called grade_evaluator() that takes a 
# grade as input and prints both the letter grade and feedback. Then, test the 
# function by calling it with a sample grade.

def grade_evaluator(grade):

    if grade >= 90:
        letter="A"
        feedback = "Excellent work!"
    elif grade >= 80:
        letter="B"
        feedback = "Good job!"
    elif grade >= 70:
        letter="B"
        feedback = "Your can improve!"
    elif grade >= 60:
        letter="D"
        feedback = "Needs more effort!"
    else:
        letter="F"
        feedback = "Please see your instructor"
    
    return letter, feedback

x,y = grade_evaluator(grade)
print(f"Your grade is {x}, and your feedback is {y}")

# While Loops: Build a Number Guessing Game
# 1. Set a Secret Number and Prompt for a Guess
# Question: Set a secret number (e.g., 7 and prompt the user to guess it once. Print 
# the guess.
# 2. Check the Guess Once
# Question: Use an if-else statement to check if the guess is correct and print 
# "Correct!" if it is, otherwise print "Wrong!".
# 3. Loop Until the Correct Guess
# Question: Use a while loop to keep asking the user for a guess until they guess the 
# secret number.
# 4. Provide Hints for Each Guess
# Question: Modify the loop so that after each wrong guess, the program tells the 
# user if the guess was too high or too low.
# 5. Count the Number of Attempts
# Question: Enhance the game to count the number of guesses and, once the 
# correct number is guessed, print the total number of attempts made.
