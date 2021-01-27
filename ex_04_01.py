def computepay(h,r):
    hrs = input("Enter Hourse: ")
    h = float(hrs)
    rate = input("Enter Rate: ")
    r = float(rate)
    if h >= 40:
        wh = h-40
        overtime=r*1.5*wh
        normaltime=40*r
        P=normaltime+overtime
        return (print("Pay",P))
    else:
        P=h*r
        return (print("Pay",P))

computepay(10,20)
