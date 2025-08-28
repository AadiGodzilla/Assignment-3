greeting = input("Enter a message: ")   # Get greeting string from user
lower_greeting = greeting.lower()   # Convert the greeting string to lowercase 

# Separate string into a list of words with " " as separator
list = lower_greeting.split(" ")    

if list[0] == 'hello':  # if the first word in the greeting string start with 'hello', set output to 0
    output = 0
elif lower_greeting[0] == 'h':  # else if the first letter in the greeting string starts with letter 'h', set output to 20
    output = 20
else:
    output = 100       # else, set output to 100

# Display output
print("Output: $", output)