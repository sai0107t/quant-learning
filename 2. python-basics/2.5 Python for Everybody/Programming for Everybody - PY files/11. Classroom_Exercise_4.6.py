# write a program to prompt the use rfor hours and rate per hour suing input to compute gross pay.
# Pay should be the normal rate or hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours
# put the logic to do the computation of pay in a function called Computepay() and use the function to do teh computation
# the function should retrun a value. Use 45 hours and a rate of 10.5 per hour to test the program (the pay should be 498.75)
# you should use input to read a string and float() to convert teh string to a number 
# dont worry about error checking the user inpyt unless you want to - you can assume the user types number properly.
# Do not name you variable sum or use the sum() function



hours=input('Enter no. of hours: ')
rate=input('Enter rate per hour')
h=float(hours)
r=float(rate)
def computepay(h,r):
    if h<=40:
        return (h*r)
    else:
        return (((h-40)*1.5*r)+(40*r))

p=computepay(h,r)
print('Pay',p)

