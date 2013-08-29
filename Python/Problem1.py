#-------------------------------------------------------------------------------
# Name:        Problem 1
# Purpose:
#
# Author:      volkc
#
# Created:     18/06/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
x = 1000;
y = 1;
n = 0;

while 3*y < x:
    n = 3*y + n;
    y = y + 1;

y = 1
while 5*y < x:
    if y%3 != 0:
        n = 5*y + n;
    y = y + 1;

print(n)


