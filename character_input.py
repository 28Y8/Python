# Libraries
import datetime

# Variables
milestone = 100                     # Number as milestone for age
today = datetime.date.today()       # Get current date from today
year = today.year                   # Get the current year from today

# Functions
def create_space():
      print()

def create_division():
      division_string = "_______________________________________________________________________________________________________________________________________"
      
      create_space()
      print(f"{division_string}\n")
      create_space()

def calculate_age_milestone(milestoneAge, currentAge):
      # Simple argument datatype check
      if not isinstance(milestoneAge, int) or not isinstance(currentAge, int):
            print("One of the provided arguments were not the correct datatype!")
            
            print("Milestone: ", type(milestoneAge))
            print("Age: ", type(currentAge))
            
            return False
      
      # Calculate the year when you reach milestone
      year_milestone = (year + milestoneAge) - currentAge

      # Calculate how many years left until you reach milestone
      years_until_milestone = year_milestone - year

      # Return year until milestone and years left to reach the milestone
      return year_milestone, years_until_milestone

def get_age_milestone_string(name, age, milestoneAge):
      # Get the milestone
      age_milestone = calculate_age_milestone(milestoneAge, age)
      
      age_hundred = age_milestone[0]
      age_until_hundred = age_milestone[1]
      
      # Make sure the person is not already as old as the milestone
      if age == milestoneAge:
            return f"You fufilled {milestoneAge} years old this year, {name}. Congratulations for reaching this incredible milestone!"
      elif age > milestoneAge:
            return f"You are already {milestoneAge} years old and above, {name}. Congratulations for reaching this amazing milestone!"
      
      # Tell the result to the user and consider how many years left. Then return it
      if age_until_hundred == 1:
            return f"You, {str.capitalize(name)} will turn 100 in the year {age_hundred}. This means that in about {age_until_hundred} year, then you will achieve that incredible milestone!"
      else:
            return f"You, {str.capitalize(name)} will turn 100 in the year {age_hundred}. This means that in about {age_until_hundred} years, you will achieve that massive milestone soon!"

def print_string_extra(string, separate):
      try:
            num_copies = int(input("Enter the number of copies: "))
      except ValueError:
            print("The provided amount of tries is not a real number, please try again!")
            create_division()
            
            return print_string_extra(string)
      
      # Create an extra space
      create_space()
      
      # Print the text, separate or not. Based on the extra one and extra two tasks
      if not separate:
            print(string * num_copies)
            create_division()
      else:
            print("\n".join([string] * num_copies))
            create_division()

def main():
      create_division()
      
      # Get the person's name
      name = str(input("Enter your name: "))
      
      # Check if age is valid data type or not
      try:
            age = int(input("Enter your age: "))
      except ValueError:
            print("The provided age is not a valid age or number, please try again!")
            create_division()
            
            return main()
      
      # Create a space after answer
      create_space()
      
      # Get the answer
      milestone_string = get_age_milestone_string(name, age, milestone)
      
      # Do task one of the questions
      print(milestone_string)
      
      # Get ready for the next attempt
      create_division()
      
      # Do extra task one of the questions
      print_string_extra(milestone_string, False)
      
      # Do extra task two of the questions
      print_string_extra(milestone_string, True)

# Initialization
main()
