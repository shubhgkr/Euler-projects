def isPrime(num):
	count=0
	for i in range(2,num//2):
		if(num%i==0):
			count=1
			break
	return (count!=1)

def factor(number):
	for divisor in range(1,number):
		if (number%divisor==0):
			if (isPrime(number//divisor)):
				return number//divisor

print(factor(600851475143))