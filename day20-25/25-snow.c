#include <stdio.h>

int main() {
    const int TARGETROW=2981;
    const int TARGETCOL=3075;

    const unsigned long long FIRSTCODE=20151125;
    const unsigned long long MULTIPLIER=252533;
    const unsigned long long DIVIDER=33554393;

    int row=1;
    int col=1;
    unsigned long long newcode=FIRSTCODE;
    while (1) {
        if (row>1) {
            row-=1;
            col+=1;
        }
        else {
            row=col+1;
            col=1;
        }
        newcode=(newcode*MULTIPLIER)%DIVIDER;
        if (row==TARGETROW && col==TARGETCOL)
            break;
     }
    printf("Part 1: code %llu\n", newcode);

}