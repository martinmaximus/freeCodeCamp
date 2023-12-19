fname = input("Enter file name: ")
try:
    fhand = open(fname) # open file
except:
    print('File cannot be opened:', fname)
    quit()



# Search through every line of the file
for line in fhand:
    if line.startswith('Subject:'): continue # skip lines that don't start with "Subject:"
    line = line.rstrip() # remove extra spaces at the right of the line
    words = line.split() # split the line into words
    print(line)
    print(words)
