# Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

# Sample Input 0
# 5
# -3 -1 0 1 2
# -2
# Sample Output 0
# Yes

# Sample Input 1
# 5
# -2 0 1 1 5
# 0
# Sample Output 1
# No

n=int(input())
ls=list(map(int,input().split(" ")))
s=int(input())
flag=0
first=0;last=n-1

while first<last:
    if ls[first]+ls[last] == s:
        flag=1;break
    elif ls[first]+ls[last]<s:
        first=first+1
    else:
        last=last-1

if flag==0:
    print("No")
else:
    print("Yes")
