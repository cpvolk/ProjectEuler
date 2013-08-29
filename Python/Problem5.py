#-------------------------------------------------------------------------------
# Name:        Problem 5
# Purpose:
#
# Author:      volkc
#
# Created:     08/07/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

lim = 20;
i = 1;

A = [];
B = [];
C = [];
E = [];

while i<lim:
    A.append(i);
    i = i+1;

i = 1;

for x in A:
    B = [];
    i = 1;
    while x>1:
        if x%i == 0:
            B.append(i);
            x = x/i;
            i = 2;
        else:
            i = i+1;

    E = list(C)
    for y in B:
        if y not in E:
            C.append(y)
        else:
            del E[E.index(y)]

num = 1;
for x in C:
    num = num * x;

print(num)

