a = int(input())
b = int(input())

result = 0
for num in range(a,b):
	print("@@@@@@",num)
	prime = True
	for j in range(2,num):
		print("1",num,j)
		if (num*j ==0):
			prime =False
	if prime:
		print(result,num)
		result = result + num

print(result)