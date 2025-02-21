# Question 1

a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a) # output = 16



# Question 2

print((3+10**2/2) or 70.0) # output = 53



# Question 3

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a) # output = 7
print(b) # output = 6
c = a + b
print(c) # output = 13
d = "abc" * (c // 3)
print(d) # output = abcabcabcabc



# Question 4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("5485839837501070045005400701057389385845")) # output = True
print(palindrome("7489617719749244646336564429479177169847")) # output = False
print(palindrome("8025833559061079503003059701609553385208")) # output = True
print(palindrome("6593036601359343374664733439531066303956")) # output = True



# Question 5

## Write a function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
## The function takes 1 parameter: the text to look into and returns the number of matches.
##Use only the things we have learned in class. Give some explanations besides the code.

def find_pattern_occurrences(text):
    words = text.split()
    count = sum(1 for word in words if word.startswith("un") and word.endswith("an")) # This makes sure to take the parameter 1, that starts with “un” has unlimited number of letters and ends with “an”
    return count

text_to_search = "Unban is a pattern, Uncan is another, but not Cuncan or Unanb."
print("Number of matches:", find_pattern_occurrences(text_to_search))



# Question 6

# String = an ordered and immutable collection of characters, used to store and manipulate text (denoted by quotation marks)
# Immutable means you cannot change a string once it's created.
# List = an ordered, mutable collection that can hold items of any data type (denoted by square brackets [] with elements separated by commas)
# Lists are Mutable (Can Be Changed)

# Example of a string:
string1 = "Cat"
# string1[0] = "R" If I PUT this code it would give ERROR: Strings can't be changed, therefore proving strings are immutable.

# Example of a list;
list1 = [1, 3, 5, 7, 9]
print(list1)
list1[1] = 11  # I am able to change the item at index 1
print(list1)  # Output: [1, 11, 5, 7, 9] which shows that I was able to change ths list, and therefore proving it is mutable



# Question 7

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

modified_numbers = [] # create a new list to store the modified even numbers

for num in random_numbers:
    if num % 2 == 0:  # check if the number is even
        modified_numbers.append(num * 2)  # replace the even number with its double

# Print the modified list
print(modified_numbers)


# Question 8

def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False  # Invalid if it doesn't start with the correct prefix

    # Check if there is at least one dot (".") somewhere
    dot_found = False
    for char in url:
        if char == ".":
            dot_found = True
            break  # Stop checking after finding the first dot

    if not dot_found:
        return False  # Invalid if no dot is found

    # Check if the URL ends with a dot
    if url[-1] == ".":
        return False  # Invalid if it ends with a dot

    return True  # If all conditions are met, it's a valid URL

url = input("Enter a URL: ")  # Ask the user for a URL
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")

# Question 9
birth_date = input("Enter your birthday (DD-MM-YYYY): ")  # Ask for birthday

if "-" not in birth_date or birth_date.count("-") != 2:  # Validate format
    print("Wrong format, enter the right format (DD-MM-YYYY)")
else:
    parts = birth_date.split("-")  # Split input into parts

    year = parts[2]  # Extract year

    if year.isdigit():  # Ensure the year is a number
        year = int(year)  # Convert year to integer
        current_year = 2024  # Set the current year manually
        full_years = current_year - year - 1  # Exclude birth year and current year
        days_passed = full_years * 365  # Multiply by 365 (ignoring leap years)
        print("Total days passed (excluding birth year and current year):", days_passed)
    else:
        print("Wrong format, enter the right format (DD-MM-YYYY)")
