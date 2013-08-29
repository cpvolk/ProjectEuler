#-------------------------------------------------------------------------------
# Name:        Problem 23
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

A = [];
B = [];
C = [];
n = 0;
lim = 28123;

for i in range(2, lim):
    B.append(i)

for i in B:
    if d(i) > i:
        A.append(i);

for i in A:
    strt = A.index(i);
    for j in A[strt:len(A)]:
        n += 1;
        try:
            B.remove(i+j);
        except:
            pass;

print(sum(B))


