#-------------------------------------------------------------------------------
# Name:        Problem 20
# Purpose:
#
# Author:      volkc
#
# Created:     18/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def factorial(num):
    ans = 1;
    for i in range(1, num+1):
        ans = ans * i;

    return(ans)

A = str(factorial(100));

summ = 0;
for i in A:
    summ = summ + int(i)

print(summ)