a=1
while a<=100:
    if a%3==0:
        print("nav")
    elif a%7==0:
        print("gurukul")
    elif a%3==0 or a%7==0:
        print("navgurukul")
    a=a+1
        