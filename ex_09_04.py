fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
email = dict()
for line in fh:
    line=line.rstrip()
    if not line.startswith("From") or line.startswith("From:"):
        continue
    mail_list=line.split()

    #for word in mail_list:
    name=mail_list[1]
    #print(name)for name in name:
    if name not in email:
        email[name] = 1
    else:
        email[name] += 1
mailname=None
mailcount=None
for name, count in email.items():
    if mailcount is None or count > mailcount:
        mailcount=count
        mailname=name
print((mailname),(mailcount))

#print(email)
