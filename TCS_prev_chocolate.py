# A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

# Input :
# 8  – Value of N
# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline
# Output:
# 4 5 1 9 5 0 0 0

# method_1
n=int(input())
chocos=[int(x) for x in input().split(",")]
for i in chocos:
    if i==0:
        chocos.remove(i)
        chocos.append(i)
print(*chocos)

#method_2
n=int(input())
chocos=[int(x) for x in input().split(",")]
ls=[0]*n

for i in range(n):
    if chocos[i]!=0:
        ls[i]=chocos[i]
print(*ls)
