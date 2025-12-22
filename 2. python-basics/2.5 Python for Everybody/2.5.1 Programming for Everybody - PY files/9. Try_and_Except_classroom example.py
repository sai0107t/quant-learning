# This is the same example as program 8: Pay_Rate_Determination_2.py file but just by using try and except function
# Also, its in more detailed way


sh=input('Enter Hours:')
sr=input('Enter Rate: ')
try:
    fh=float(sh)
    fr=float(sr)
except:
    print('Error, please enter numeric input') # here instead of traceback error or syntax error, we are giving this message
    quit() # if we dont use quit, after give the above message, its again giving traceback error message in terminal

print(fh,fr)
if fh>40:
    reg=fr*fh
    otp=(fh-40)
    xp=reg+otp
else:
    xp=fh*fr
print("pay:",xp)