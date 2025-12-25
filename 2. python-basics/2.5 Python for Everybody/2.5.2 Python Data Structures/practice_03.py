fname=input('Enter the file name:')
fhand=open(fname)
lst=list()
for line in fhand:
    line=line.rstrip() # remove trailing whitespace
    words=line.split() # split line into words
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)  
