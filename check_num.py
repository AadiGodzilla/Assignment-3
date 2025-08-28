#Prompt the user to enter a number
number = int(input("Enter a number: "))     

# Check if the number is positive and even
if number > 0 and number % 2 == 0:          
    print("Number is a positive even number") 
# Check if the number is positive and odd
elif number > 0 and number % 2 != 0:        
    print("Number is a positive odd number")
# Check if the number is negative and even
elif number < 0 and number % 2 == 0:        
    print("Number is a negative even number")
# Check if the number is negative and odd
elif number < 0 and number % 2 != 0:        
    print("Number is a negative odd number")
# Otherwise, the number is zero
else:                                       
    print("Number is zero")
