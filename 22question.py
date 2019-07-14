num2=int(input())
lst=list(map(int,input().split()))[:num2]
lst.sort()
print(lst[-1])
