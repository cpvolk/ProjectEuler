#-------------------------------------------------------------------------------
# Name:        Problem 11
# Purpose:
#
# Author:      volkc
#
# Created:     14/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fileName = 'C:/Users/volkc/Dropbox/Documents/Project Euler/Python/Problem11.txt'
f = open(fileName, 'r');
C = f.read()

row = 20;
col = 20;
prod = 4;

A = [[0 for x in range(0, row)] for x in range(0, col)];

# Create Array
for i in range(0, row):
    for j in range(0, col):
        ind = i*col*3 + 3*j;
        A[i][j] = (int(C[ind:ind+2]))

# Look for Horizontal Products
horz = [[1 for x in range(0, col-prod)] for x in range(0, row)];
for i in range(0, row):
    for j in range(0, col-prod):
        for k in range(0, prod):
            horz[i][j] = A[i][j+k] * horz[i][j]

# Look for Vertical Products
vert = [[1 for x in range(0, col)] for x in range(0, row-prod)];
for i in range(0, row-prod):
    for j in range(0, col):
        for k in range(0, prod):
            vert[i][j] = A[i+k][j] * vert[i][j]

# Look for Down-Diagonal Products
ddia = [[1 for x in range(0, col-prod)] for x in range(0, row-prod)];
for i in range(0, row-prod):
    for j in range(0, col-prod):
        for k in range(0, prod):
            ddia[i][j] = A[i+k][j+k] * ddia[i][j]

# Look for Up-Diagonal Products
udia = [[1 for x in range(0, col-prod)] for x in range(0, row-prod)];
for i in range(0, row-prod):
    ind = i+prod;
    for j in range(0, col-prod):
        for k in range(0, prod):
            udia[i][j] = A[ind-k][j+k] * udia[i][j]

B = [];
# Find Max
B.append(max(max(horz)));
B.append(max(max(vert)));
B.append(max(max(ddia)));
B.append(max(max(udia)));

print(max(B))






