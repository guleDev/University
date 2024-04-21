#include <stdio.h>

int main() {
    int n, i = 0, soma = 0;
    float media = 0.0;
    
    printf("\nDigite o valor do numero n: ");
    scanf("%d", &n);
    do {
        soma += i;
        i++;
    } while ( i <= n);
    media = (float)soma / n;
    printf("\nA soma dos primeiros %d números = %d", n, soma);
    printf("\nA média dos primeiros %d números = %.2f\n", n, media);
    return 0;
}