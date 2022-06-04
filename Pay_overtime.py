hrs = input("Enter Hours:")
rt = input("Enter Rate:")
h = float(hrs)
r = float(rt)

if h <= 40:
    pay = h * r
    print ("Pay:",pay)
elif h > 40:
    pay = (40*r)+((h-40)*r*1.5)
    print ("Pay:",pay)