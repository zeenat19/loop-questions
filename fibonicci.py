# i=0
# a=0
# b=1
# print(a)
# while i<10:
# 	c=a+b
# 	a=b
# 	b=c
# 	i=i+1
# 	print(a)



i = 1
while i < 100:
    n = 2
    while 2<n and n!=i:
        if n % i==0:
            print (n,"not prime number")
            break
       	i=i+1
       	else:
       		print (n,"prime")
    	n = n+1    