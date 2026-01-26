num=[3,0,0,-1,-2,0,1,2,-3]
result=[]
num.sort()
for i in range(len(num)-2):
    if i>0 and num[i]==num[i-1]:
        continue 
    left=i+1
    right=len(num)-1
    while left<right:
        total=num[i]+num[left]+num[right]
        if total<0:
            left+=1
        elif total>0:
            right-=1
        else:
            result.append([num[i],num[left],num[right]])
            while left<right and num[left]==num[left+1]:
                left+=1
            while left<right and num[right]==num[right-1]:
                right-=1
            left+=1
            right-=1
print(result)