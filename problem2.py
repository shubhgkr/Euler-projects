def fibonacci():
	a=1
	b=2
	sum=0
	while(b<=4000000):
		print("a=",a,"b=",b)
		if(b%2==0):
			sum+=b
		(a,b)=(b,a+b)
	return sum

print(fibonacci())