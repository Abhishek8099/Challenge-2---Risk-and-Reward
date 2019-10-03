n=int(input())
trader=list(map(int,input().split()))
risk=list(map(int,input().split()))
bonus=list(map(int,input().split()))
result=0
for i in range(0,n):
    max_bonus=0
    for j in range(0,n):
        if trader[i]>=risk[j]:
            if bonus[j]>=max_bonus:
                max_bonus=bonus[j]
    result=result+max_bonus
print(result)
