#-------------------------------------------------------------------------------
# Name:        Problem 2
# Purpose:
#
# Author:      volkc
#
# Created:     18/06/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

y = 0;
x = 10;
n = 0;
A = list();
lim = 4000000;

fib = [];
fib.append(1);
fib.append(2);
ind = 1;

while fib[ind] < lim:
    if fib[ind-1] + fib[ind] > lim:
        break
    else:
        fib.append(fib[ind-1] + fib[ind]);

    ind = ind + 1;

for ind in range(1, len(fib)):
    if fib[ind]%2 == 0:
        n = n + fib[ind];

print(n)


