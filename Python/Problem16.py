#-------------------------------------------------------------------------------
# Name:        Problem16
# Purpose:
#
# Author:      volkc
#
# Created:     15/08/2013
# Copyright:   (c) volkc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

x = 2**1000;
A = str(x)

summ = 0;
for y in A:
    summ = summ + int(y);

print(summ)
# for 2^1000, summ = 1366
