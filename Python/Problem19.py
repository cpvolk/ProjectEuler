#-------------------------------------------------------------------------------
# Name:        module2
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

year = 1900
x = 2 # Tuesday
z = 0

mos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

for year in range(1901, 2001):
    if (year%4 == 0 and (year%100 != 0 or year%400 == 0)):
        mos[1] = 29;
    else:
        mos[1] = 28;

    for y in mos:
        x = (x+y)%7;
        if x == 0:
            z = z + 1;

print(z)

