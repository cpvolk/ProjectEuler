#-------------------------------------------------------------------------------
# Name:        Problem 10
# Purpose:
#
# Author:      volkc
#
# Created:     09/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

lim = 2000000
A = [2]
x = 3

while x<=lim:
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

print(sum(A))
