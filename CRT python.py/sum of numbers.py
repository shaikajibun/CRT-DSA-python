nums=[1,1,1,2,3,4,5]
#sum of all numbers

nums= input()
s=0
for i in nums:
    if i.isdigit():
        s+=int(i)
print(s) 
