#-------------------------------------------------------------------------------
# Name:        Project 3
# Purpose:
#
# Author:      volkc
#
# Created:     06/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

A = [1, 2];
lim = 6501;
i = 3;

while i<lim+1:
    A.append(i)
    i = i + 2;

print(A)

j = 3;
while j<lim:
    for i in range(0, len(A)-1):
        if A[i]%j == 0 and j!=A[i]:
            del A[i]
    j = j+1

print(A)


