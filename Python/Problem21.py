#-------------------------------------------------------------------------------
# Name:        Problem 12
# Purpose:
#
# Author:      volkc
#
# Created:     18/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def factor(num):
    factors = [1];
    for i in range(2, round(num**.5)+1):
        if num%i == 0:
            factors.append(i);
            if int(num/i) != i:
                factors.append(int(num/i));

    return factors

def d(num):
    factors = factor(num);
    summ = sum(factors);
    return summ

def amicable(num):
    b = d(num);
    a = d(b);

    if a == num and a!=b:
        return [a, b]

A = [];
for i in range(0, 10000):
    j = amicable(i);
    if j != None:
        A.append(j[1])

print(sum(A))