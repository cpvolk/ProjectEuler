#-------------------------------------------------------------------------------
# Name:        Problem 8
# Purpose:
#
# Author:      volkc
#
# Created:     09/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fileName = 'C:/Users/volkc/Dropbox/Documents/Project Euler/Python/Problem8.txt'
f = open(fileName, 'r');
C = f.read()

lim = len(C)
i = 1;
maxProd = 0;

while i<=len(C)-5:
    prod = 1;
    for j in range(0,5):
        prod = int(C[i+j]) * prod;

    if prod > maxProd:
        maxProd = prod;

    i = i+1;

print(maxProd)

