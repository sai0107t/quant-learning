fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1 # count the lines that start with 'From '
print('There were', count, 'lines that started with From ')