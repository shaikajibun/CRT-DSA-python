#Time complexity is the rate at which the number of operations 
#performed by an algorithm grows with respect to the input size(n).
#it helps us analyse the efficiency of an algorithm 
#O(1)
#O(n)
#O(n^2)
#O(N!)

#factors
n=int(input())
c=0
for i in range(1,n//2+1):
    if n%i==0:
        c+=1
        print(i,c)
print(c)
#2,n**0.5+1 optimized solution  only 1 integration is enough
