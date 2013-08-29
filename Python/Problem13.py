#-------------------------------------------------------------------------------
# Name:         Problem 13
# Purpose:
#
# Author:      volkc
#
# Created:     18/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fileName = 'C:/Users/volkc/Dropbox/Documents/Project Euler/Python/Problem13.txt'
f = open(fileName, 'r');
C = f.read()

rows = 100;
summ = 0;

for i in range(0, 100):
    strt = 50*(i) + i;
    end = strt + 50;

    summ = summ + int(C[strt:end])

ans = str(summ)
print(ans[0:10])