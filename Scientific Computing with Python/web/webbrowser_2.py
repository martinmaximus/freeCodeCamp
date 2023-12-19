import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand: 
    words = line.decode().strip()
    #print(words)
    for word in words.split():
        counts[word] = counts.get(word, 0) + 1
#print(counts)

sort = sorted([(v, k) for k, v in counts.items()], reverse=True)
print(sort)



fhand1 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand1:
    print(line.decode().strip())

