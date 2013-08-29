#-------------------------------------------------------------------------------
# Name:        Problem 4
# Purpose:
#
# Author:      volkc
#
# Created:     06/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

i = 1;
x = 9999
B = []
lim = 100;

for i in range(9*lim, 10*lim):
    for j in range(9*lim, 10*lim):
        B.append(i*j)

while len(B) != 1:
    test = str(max(B))
    i = 0;
    sum = 0;
    while i<.5*len(test):
        if test[i] != test[len(test)-i-1]:
            sum = sum + 1;
        i = i + 1;

    if sum == 0:
        print(test)

    del B[B.index(max(B))]