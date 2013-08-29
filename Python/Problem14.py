#-------------------------------------------------------------------------------
# Name:        Problem14
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

x = 13;
seq = [x];
length = 1;

# 1 to 100000 was 77031 with 351 steps
# 1 to 1000000 was 837799 with 525 steps

for x in range(1, 1000000):
    seq = [x];
    y = x;
    n = 1;
    while x>1:
        if x%2 == 0:
            x = x/2;
        else:
            x = 3*x + 1;
        n = n+1;

    if n>length:
        xlong = y;
        length = n;

print(length)
print(xlong)
