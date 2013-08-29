#-------------------------------------------------------------------------------
# Name:        Problem 9
# Purpose:
#
# Author:      volkc
#
# Created:     09/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Using Euclid Formula for Pythogrean Triples
# Also using condition that a+b+c = 1000

lim = 1000;
m = round(.5*(lim**.5))-1;

print(m)

while m <= (lim/2)**.5:
    if lim%(2*m) == 0:
        n = lim/(2*m) - m;

        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2


        print(a*b*c)

    m = m + 1;


