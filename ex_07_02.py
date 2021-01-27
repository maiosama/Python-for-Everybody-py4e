fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    if line.startswith("X-DSPAM-Confidence:"):
       count=count+1
       x= line[20 : ]
       n=float(x)
       total=total+n
       average=(total/count)
print("Average spam confidence: ",average)
