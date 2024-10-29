# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.
'''
def check_letter():
    # Your control flow logic goes here
    #enter letter input for terminal
    letter = input("Enter a letter: ")
        #check if letter is alphabetical and only one letter
    if not letter.isalpha() or len(letter) != 1:
        print('Please enter a single letter')
        return
        #check if letter is a vowel and convert to lowercase
    letter.lower() in letter
    vowel = {'a', 'e', 'i', 'o', 'u'}
        #constant = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
        #else print if letter is a consonant
        #else print for invalid input
        
    if letter == vowel:
         print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a constant.')    

# Call the function
check_letter()
'''

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

'''
def check_voting_eligibility():
    # Your control flow logic goes here
        
#input to add your age
    age = input("Please enter your age: ")
    #if statement for no negative numbers
    try:
        age = int(age)
        if age < 0:
            print('Age cannot be a negative number. Please enter valid age.')
            return
    except ValueError:    
        print("Invalid input please enter a number for age.")
        return
    
    if age < 18:
        print(f'Your {age} years old, sorry too young to vote.')
    else:
        print(f'Your {age} years old, please proceed with your vote!')    


#if statement for age eligibility to vote

# Call the function
check_voting_eligibility()
'''


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

'''
def calculate_dog_years():
    # Your control flow logic goes here

    #input logic for number dog years
    human_years = input('Please enter your dogs age in human years: ')

    #convert to int from string
    try:
        human_years = int(human_years)

         #statement saying 1 year = 10, 2 years = 20, every year after that is +7
        if human_years < 0:
            print('Age cant be a negative number please input a number.')
        elif human_years == 1:  
            dog_years = 10
        elif human_years == 2:  
            dog_years = 20
        elif human_years >= 3:
            dog_years = 20 + (human_years - 2) * 7

            # print the dogs age
        print(f'The Dog\'s age in dog years is {dog_years}')

    except ValueError:
        print('Invalid input. Please your dogs age in regular years.')    
            
    
   
    

# Call the function
calculate_dog_years()
'''


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.
'''
def weather_advice():
    # Your control flow logic goes here

#input for todays weather- is it cold? yes or no: is it raining? yes or no
    cold = input('For today\'s weather, is it cold outside?: ')
    rain = input('Is it raining outside?: ')

#conditional statement for cold AND raining, print wear waterproof coat    
    if cold == 'yes' and rain == 'yes':
        print('Please wear a waterproof coat')
#elif statement it is cold but not raining, print wear a warm coat
    elif cold == 'yes' and rain == 'no':
        print('Please wear a warm coat.')
#elif statement not cold but raining, print carry umbrella
    elif cold == 'no' and rain == 'yes':
        print('Please bring an umbrella.')
    elif cold == 'no' and rain == 'no': 
        print('Wear light clothing')
    else:
        print("Invalid input, please put 'yes' or 'no'.")    

#else statement not cold, not raining, pring wear light clothing


# Call the function
weather_advice()
'''