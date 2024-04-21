#include <stdio.h>
#include <stdlib.h>
char *p;
int *q; 

int main () {
    p = (char *) malloc (1000);
    q = (int *) malloc (50*sizeof(int));
}