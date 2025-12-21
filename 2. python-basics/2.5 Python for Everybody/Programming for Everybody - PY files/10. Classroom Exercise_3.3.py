# Write a program to prompt for a score between 0.0 and 1.0. if the score is out of rante, print an error.
# if the score is between 0.0 and 1.0, print a grade using the followin tabe:
# score grade >=0.9 A; >=0.8 B; >0.7 C; >=0.6 D; <0.6 F
# if the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85

score=input('Enter a score: ')
try: # we used this function to eliminate any possibility of input which is not an number
    x=float(score)
    if x>1.0 or x<0.0: # "Or" function can be used to indicate range. to use elif function, we need to use if function first
        print('Please enter a score within the range')
    elif x>=0.9: # elif function to be used for where we want exclusive results like a grade (wehere in we need only 1 case to be true)
        print('A')
    elif x>=0.8:
        print('B')
    elif x>=0.7:
        print('C')
    elif x>=0.6:
        print('D')
    else: # else function can be used at the last 
        print ('F')
except:
    print('Error, Please enter a numeric value')