#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      volkc
#
# Created:     14/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

divisors = 500;
j = 1;
n = 1;
x = 17907120;
x = 76576500; # Solutions?

while n < divisors:
    x = 0;
    for i in range(0, j):
        x = x + i;

    z = [];
    for y in range(1, int(round(x**.5, 0)+1)):
        if x%y == 0:
            z.append(y)

    j = j +1;
    n = 2*len(z);

print(x)