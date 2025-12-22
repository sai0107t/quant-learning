# Write code using find() and string slicing(see section 6.10) to extract the number at the end of the line below. 
# convert the extracted value to a floating poing nymber and print it out

text='X-DSPAM-Confidence:   0.8475'
aptos=text.find('0')
sppos=text.find('5')
host=text[aptos:sppos+1]
finalhost=float(host)
print(finalhost)