d,c=map(int,input().split())
for n in range(d+1,c):
  sum=0
  tem=n
  while tem>0:
    dig=tem%10
    sum+=dig**3
    tem//=10
  if n==sum:
    print(n,end=' ')
