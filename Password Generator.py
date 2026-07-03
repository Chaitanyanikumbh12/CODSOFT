import random
import string

# Ask the user for the password length
length = int(input("Enter the password length: "))

# Ask the user if numbers should be included
include_numbers = input("Include numbers? (yes/no): ").lower()

# Characters for the password
characters = string.ascii_letters + string.punctuation

# Add numbers if the user chooses "yes"
if include_numbers == "yes":
    characters += string.digits

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nGenerated Password:", password)
print("End of program")