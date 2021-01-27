name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email = dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith("From") or line.startswith("From:"):
        continue
    mail_list=line.split()
    mail_time=mail_list[5]
    mail_time=mail_time.split(":")
    time=mail_time[0]
    email[time]=email.get(time,0)+1
lst=sorted([(k,v)for k,v in email.items()],reverse=False)

for k,v in lst:
    print(k,v)
