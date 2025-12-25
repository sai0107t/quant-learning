# write a program that prompts for a file name, then opens that file and read throught he file, looking for lines of the form:
# X-DSPAM-Confidence: 0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# When you are testing below enter mbox-short.txt as the file name.

fname=input("Enter the file name: ")
fhand=open(fname)
count=0
total=0.0

for line in fhand:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    colonpos=line.find(":")
    number=float(line[colonpos+1:])
    total=total+number
print("Average spam confidence:", total/count)