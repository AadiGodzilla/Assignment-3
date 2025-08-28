number = int(input("Enter a number: "))     #Prompt the user to enter a number

if number > 0 and number % 2 == 0:          # Check if the number is positive and even
    print("Number is a positive even number") 
elif number > 0 and number % 2 != 0:        # Check if the number is positive and odd
    print("Number is a positive odd number")
elif number < 0 and number % 2 == 0:        # Check if the number is negative and even
    print("Number is a negative even number")
elif number < 0 and number % 2 != 0:        # Check if the number is negative and odd
    print("Number is a negative odd number")
else:                                       # Otherwise, the number is zero
    print("Number is zero")
