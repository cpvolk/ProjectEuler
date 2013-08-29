#-------------------------------------------------------------------------------
# Name:        Problem 7
# Purpose:
#
# Author:      volkc
#
# Created:     08/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

lim = 10001;
A = [2];
x = 3;

while len(A)<lim:
    i = 0;
    y = 0;
    while y<=round(x**.5) and i<len(A)-1:
        y = A[i]
        if x%y == 0 :
            break
        i = i + 1;
    else:
        A.append(x)
    x = x + 2;

print(A)
print(A[len(A)-1])





