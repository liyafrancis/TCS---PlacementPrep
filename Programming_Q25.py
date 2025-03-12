# You will be given a list of integers, arr, and a single integer k. You must sort the numbers in ascending order and create an array of length k from elements of arr to minimize its unfairness.
# Call that array arr’. Unfairness of an array is calculated as = max(arr’) – min(arr’)
# Where:- max denotes the largest integer in arr’- min denotes the smallest integer in arr’

# Sample Input 0
# 1,4,7,2
# 2
# Sample Output 0
# 1 2

numbers=list(map(int,input().split(",")))
k=int(input())
numbers.sort()
min_val=float("inf")
res=[]

for i in range((len(numbers)-k)+1):
    window=numbers[i:i+k]
    unfair=max(window)-min(window)
    if unfair<min_val:
        min_val=unfair
        res=window
print(*res)
