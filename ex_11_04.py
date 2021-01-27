import re
fhand=open("regex_sum_1091578.txt")
total = 0
for line in fhand:
        x=re.findall("[0-9]+",line)
        for number in x:
            total = total+int(number)
print (total)
