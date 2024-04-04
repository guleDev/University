/* programa que lê um número e imprime seu fatorial */
#include <stdio.h>
int fat (int n);
int main(void) {
   int n, r;
    printf("Digite um número não negativo: ");
    scanf("%d", &n);
    r = fat(n);
    printf("Fatorial - %d\n", r);
    return 0;
}

/* função para calcular o valor do fatorial */
int fat (int n) {
    int i;
    int f = 1;
    for (i = 1; i <= n; i++)
        f *= i;
    return f;
}
