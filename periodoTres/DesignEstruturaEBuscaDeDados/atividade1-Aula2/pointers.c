#include <stdio.h>
int main (void) {
    int x, *p, **q;
    x = 10;
    p = &x;
    q = &p;
    printf("%i\n", **q);    
}