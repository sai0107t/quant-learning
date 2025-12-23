# slicing strings
s='Monty Python'
print(s[0:4])  # it starts from index 0 and goes up to index 4 but does not include index 4
# it will print Mont
print(s[6:7])  # it starts from index 6 and goes up to index 7 but does not include index 7
# it will print P
print(s[6:20]) # it starts from index 6 and goes up to index 20 but does not include index 20
# it will print Python as string is only of length 12, it will not give error even though we have given 20 as ending index  
print(s[:2])   # it starts from index 0 and goes up to index 2 but does not include index 2
# it will print Mont
print(s[8:])   # it starts from index 8 and goes up to      end of the string 
# it will print hon
print(s[:])    # it starts from index 0 and goes up to      end of the string 
# it will print Monty Python 