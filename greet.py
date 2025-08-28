greeting = input("Enter a message: ")
lower_greeting = greeting.lower()

list = lower_greeting.split(" ")

if list[0] == 'hello':
    output = 0
elif lower_greeting[0] == 'h':
    output = 20
else:
    output = 100

print("Output: $", output)