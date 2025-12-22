# write a program that repeatedly prompts a user for interger numebers untill the user enters 'done'.
# once 'done' is entered, print out the largest and smallest of the numbers. if the user enters anything other than a valid number catch ti with a try/except and put
# out an an appropriate message and ignore the number
# Enter 7,2,bob,10 and 4 and match the output below.


largest=None # We need to start with None because we are comparing numbers. So its better to start with none than any other option
smallest=None
while True: # While is used for infinite loop. True is used with while (like telling python to running the loop forever, untill i manually break out of it)
    num=input('Enter a number: ') # it was asked to create a prompt
    if num=='done': # the code has to run untill we say done & == is used for equality as for assigning we would use =
        break # Break was used to break out of the forever loop
    try: # try and except is used to give an error message
        fval=float(num) #using float to convert into number
    except: 
        print('Invalid Input') # giving an error message
        continue # To jump to the top in case of an error message. That's why it is intended in the Try and except function
    if largest is None: # if is used for conditional
        largest = fval # This whole if function is saying that if largest is none (empty), then largest will become the value of fval we have determined above. Once a value is assigned here, i dont think this function never runs because its already has value and its not None
    elif fval > largest: # Elif is used in case of the above condition fails
        largest=fval
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        samllest=fval # Main thing all of these functions are within the Intendation of While

print('Maximum',largest)
print('Minimum',smallest)