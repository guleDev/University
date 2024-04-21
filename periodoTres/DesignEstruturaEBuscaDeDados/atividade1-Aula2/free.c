#include <stdio.h>
#include <stdlib.h>

int main (void) {
    int *p;
    int a;

    p = (int *) malloc (a*sizeof(int));
    if (!p) {
        printf ("** Erro: Memoria Insuficiente **");
        exit;
    }
    
    free(p);
    return 0;
}