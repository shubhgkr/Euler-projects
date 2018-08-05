def sumOfFactors():
	num=1000
	sum=0
	i=3
	count=0
	myArr=[2,1,3,1,2,3]
	'''while(i<num):
		if (i%3==0 or i%5==0):
			sum+=i
		i+=1'''
	while(i<num):
		sum+=i
		i+=myArr[count]
		count+=1
		if(i%3==0 and i%5==0):
			sum+=i
			count=0
			i+=3
	return sum
print(sumOfFactors())