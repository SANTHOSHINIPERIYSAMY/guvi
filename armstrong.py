b=int(input())
sum=0
a=b
while b>0:
	c=b%10
	sum=sum+c*c*c
	b=b//10
if a==sum:
	print("yes")
else:
	print("no")
