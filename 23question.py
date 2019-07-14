num3=int(input())
lst=list(map(int,input().split()))[:num3]
lst.sort()
print(*lst,end=" ")
