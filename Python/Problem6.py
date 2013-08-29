#-------------------------------------------------------------------------------
# Name:        Problem 6
# Purpose:
#
# Author:      volkc
#
# Created:     08/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

lim = 100;
x = 1;
sum = 0;
ssum = 0;

while x<=lim:
    sum = x**2 + sum;
    ssum = x + ssum;
    x = x + 1;

ssum = ssum**2;

print(ssum-sum)
