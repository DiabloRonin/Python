a=0
b=1
n=int(input("enter the number you need"))
print(a,b,end=" ")
while(n-1):
	x=a+b
	a=b
	b=x
	print(x,end=" ")
	n=n-1