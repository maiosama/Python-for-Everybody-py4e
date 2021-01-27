largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        new = num
        largest = new
    elif num > new:
        new=num
        largest = new

    if smallest is None:
        snew = num
        smallest = snew
    elif snew > num:
        snew=num
        smallest = snew

print("Maximum is", largest)
print("Minimum is", smallest)
