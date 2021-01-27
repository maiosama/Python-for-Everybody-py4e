hrs = input("Enter Hourse: ")
h = float(hrs)
rate = input("Enter Rate: ")
rt = float(rate)
if h >= 40:
    wh = h-40
    overtime=rt*1.5*wh
    normaltime=40*rt
    Pay=normaltime+overtime
    print(Pay)
else:
    pay=h*rt
    print(pay)
