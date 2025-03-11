# Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.

# Sample Input 0
# 4
# 1 2 3 1
# Sample Output 0
# true

# Sample Input 1
# 4
# 1 2 3 4
# Sample Output 1
# false

#method_1
n=int(input())
ls=[int(x) for x in input().split()]
count=0;res=[];flag=0
for i in ls:
    if i in res:
        flag=1
        print("true")
        break
    else:
        res.append(i)
        
if flag==0:
    print("false")

#method_2
n=int(input())
ls=list(map(int,input().split(" ")))
if n == len(set(ls)):
    print("false")
else:
    print("true")
    
    
