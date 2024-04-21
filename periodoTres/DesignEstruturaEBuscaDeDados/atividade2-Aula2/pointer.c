#include <stdio.h>

int *vetor[3];
int a = 1, b = 2, c = 3;


int main() {
    vetor[0] = &a;
    vetor[1] = &b;
    vetor[2] = &c;

    printf("a: %i, b: %i", *vetor[0], *vetor[1]);
}