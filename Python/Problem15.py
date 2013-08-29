#-------------------------------------------------------------------------------
# Name:        Problem15
# Purpose:
#
# Author:      volkc
#
# Created:     15/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

n = 21;
empty = [];
A = [];

for i in range(0, n):
    empty.append(1)

for i in range(0, n):
    A.append(empty[:])

for i in range(0, n):
    for j in range(0, n):
        if i == 0 and j == 0:
            A[i][j] = 1;
        if i == 0 and j != 0:
            A[i][j] = int(A[i][j-1]);
        if j == 0 and i != 0:
            A[i][j] = int(A[i-1][j]);
        if i != 0 and j != 0:
            A[i][j] = int(A[i][j-1]) + int(A[i-1][j]);
print(A[n-1][n-1])