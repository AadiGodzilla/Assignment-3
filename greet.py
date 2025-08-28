# Get greeting string from user
greeting = input("Enter a message: ")   
# Convert the greeting string to lowercase
lower_greeting = greeting.lower()        

# Separate string into a list of words with " " as separator
list = lower_greeting.split(" ")    

# if the first word in the greeting string start with 'hello', set output to 0
if list[0] == 'hello':          
    output = 0
# else if the first letter in the greeting string starts with letter 'h', set output to 20
elif lower_greeting[0] == 'h':  
    output = 20
# else, set output to 100
else:                           
    output = 100      

# Display the output price
print("Output: $", output)