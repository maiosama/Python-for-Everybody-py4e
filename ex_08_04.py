fname = input("Enter file name: ")
fh = open(fname)

lst=[]
for word in fh:
    words=word.split()

    for words in words:
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)


#words.sort()
#print("first:",(words))
