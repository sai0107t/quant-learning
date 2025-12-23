# we are learning String Concatenation in Python
a = "Hello"
b = a + 'There' # we are concatenating two strings here
print(b)  # it will print HelloThere (without space between Hello and There)
c = a + ' ' + 'There' # we are concatenating two strings here with space in between
print(c)  # it will print Hello There (with space between Hello and There)  


# Using in as a logical operator
fruit = 'banana'
'n' in fruit  # it will return True as n is present in banana (Its kind of similar to == operator)
'm' in fruit  # it will return False as m is not present in banana                              
if 'a' in fruit:  # it will return True as a is present in banana
    print('Found it!')  # it will print Found it!   

# Using String Comparisons
word = 'banana'
if word == 'banana':  # it will return True as word is equal to banana
    print('All right, bananas.')  # it will print All right, bananas.
if word < 'banana':  # it will return False as word is not less than banana
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':  # it will return False as word is not greater than banana
    print('Your word,' + word + ', comes after banana.')
else:  # as both above conditions are False, it will come to else part
    print('All right, bananas.')  # it will print All right, bananas.   

# String Library Functions
greet = 'Hello Bob'
zap = greet.lower()  # it will convert all characters to lower case
print(zap)  # it will print hello bob
print(greet)  # it will print Hello Bob (original string will not be changed)
print('Hi There'.lower())  # it will print hi there 

# Searching a string
fruit = 'banana'
pos = fruit.find('na')  # it will return the index of first occurrence of na 
print(pos)  # it will print 2
aa = fruit.find('z')  # it will return -1 as z is not present in banana
print(aa)  # it will print -1

# Make everything Upper case
greet = 'Hello Bob'
nnn = greet.upper()  # it will convert all characters to upper case
print(nnn)  # it will print HELLO BOB
www=greet.lower().upper()  # it will first convert all characters to lower case and then to upper case
print(www)  # it will print HELLO BOB

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')  # it will replace Bob with Jane
print(nstr)  # it will print Hello Jane 
nstr1 = greet.replace('o', 'X')  # it will replace all o with X
print(nstr1)  # it will print HellX BXb 

# Stripping whitespace
greet = '   Hello Bob   '
greet.lstrip()  # it will remove leading whitespace
print(greet.lstrip())  # it will print 'Hello Bob   '
greet.rstrip()  # it will remove trailing whitespace     
print(greet.rstrip())  # it will print '   Hello Bob' 
greet.strip()  # it will remove both leading and trailing whitespace
print(greet.strip())  # it will print 'Hello Bob'

# Prefixing Strings
line = 'Please have a nice day'
line.startswith('Please')  # it will return True as line starts with Please
print(line.startswith('Please'))  # it will print True
line.startswith('plea')  # it will return False as line does not start with plea
print(line.startswith('plea'))  # it will print False       


# Parsing and Extracting Data
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'   
atpos = data.find('@')  # it will return the index of first occurrence of @
print(atpos)  # it will print 21
sppos = data.find(' ', atpos)  # it will return the index of first occurrence of space after atpos
print(sppos)  # it will print 31
host = data[atpos+1 : sppos]  # it will extract the string between atpos+1 and sppos
print(host)  # it will print uct.ac.za  

