# Write a program to promt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours
# use 45 hours and a rate of 10.5 per hour to test program (the pay should be 498.75).
# you sould use input to read a string and float() to convert the string to a number.

hours=input('Enter hours') # Enter hours in inverted commas are letters nothing but a string
rate=input('Enter rate')
h=float(hours) # using float function to convert string into integer
r=float(rate)
if h<=40: # here we need to use semi colon for Intendention
    print(h*r)
else: # here i have used else because, there is only one condition exists in the question. otherwise we can use If as well
    print((40*r)+(h-40)*1.5*r)
