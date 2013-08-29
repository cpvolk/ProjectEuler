#-------------------------------------------------------------------------------
# Name:        Problem25
# Purpose:
#
# Author:      volkc
#
# Created:     18/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fib = [1, 1];
lim = 1000;
n = 1;
i = 0;

while n<lim:
    fib.append(fib[i] + fib[i+1]);
    i += 1;

    n = len(str(fib[i]));

print(fib[i])
