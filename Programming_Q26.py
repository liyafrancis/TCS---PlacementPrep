# Read the following input: an integer n representing the number of rows in the matrix, and an integer m representing the number of columns in the matrix and the values of the matrix (n rows and m columns).

# The matrix is sorted such that all elements in any row are sorted in increasing order from left to right, and all elements in any column are sorted in increasing order from top to bottom. 
# You should print the total number of negative numbers present in the matrix.

# The input will be provided as follows:

# The first line of input contains a single integer n, the number of rows in the matrix.
# The second line of input contains a single integer m, the number of columns in the matrix.
# The next n lines each contain m integers separated by spaces, representing the elements of the matrix.
# Solve this problem with a complexity less than m+n.

# Sample Input 0
# 3
# 4
# -4 -3 -1 1
# -2 -2 1 3
# -1 1 2 4
# Sample Output 0
# 6

r=int(input())
c=int(input())
A=[]
for i in range(r):
    row=list(map(int,input().split()))
    A.append(row)
i=0;count=0;j=i;limit=r*c;k=0
while k<limit:
    if A[i][j]<0:
        count=count+1
    j=j+1
    if j>=c:
        j=0
        i=i+1
    k=k+1
print(count)
