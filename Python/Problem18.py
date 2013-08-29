#-------------------------------------------------------------------------------
# Name:        Problem 18
# Purpose:
#
# Author:      volkc
#
# Created:     18/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fileName = 'C:/Users/volkc/Dropbox/Documents/Project Euler/Python/Problem18.txt'
f = open(fileName, 'r');
C = f.read()
A = [];
i = 0;

while i<len(C):
    A.append(int(C[i:i+2]))
    i += 3;

i = 0;
j = len(A);
while j > 0:
    j = j - i;
    i += 1;

rows = i;

B = []
C = []
for i in range(0, rows-1):
    B.append(0);

for i in range(0, rows-1):
    C.append(list(B))

ind = 0;
for i in range(0, rows):
    for j in range(0, i):
        C[i-1][j] = A[ind];
        ind += 1;

for i in range(1, rows-1):
    row = rows - i;
    for j in range(0, row-1):
        C[row-2][j] = C[row-2][j] + max(C[rows-i-1][j:j+2])

print(C[0][0])