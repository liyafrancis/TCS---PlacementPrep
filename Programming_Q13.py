# matrix addition

# Sample Input 0
# 2 2
# 1 2
# 3 4
# 5 6
# 7 8

# Sample Output 0
# First Matrix:
# 1 2 
# 3 4 
# Second Matrix:
# 5 6 
# 7 8 
# Sum of the two matrices is:
# 6 8 
# 10 12

r,c=map(int,input().split(" "))
A=[[int(x) for x in input().split()]for i in range(c)]
B=[[int(x) for x in input().split()]for i in range(c)]

print("First Matrix:")
for i in range(r):
    for j in range(c):
        print(A[i][j],end=" ")
    print()
print("Second Matrix:")
for i in range(r):
    for j in range(c):
        print(B[i][j],end=" ")
    print()
print("Sum of the two matrices is:")
for i in range(r):
    for j in range(c):
        print(A[i][j]+B[i][j],end=" ")
    print()
