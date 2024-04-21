#include <stdio.h>

int main() {
    int n, m, i, soma = 0;

    printf("\nDigite o valor do número m: ");
    scanf("%d", &m);

    printf("\nDigite o valor do número n: ");
    scanf("%d", &n);

    i = m;
    while (i <= n){
        soma += i;
        i++;
    }

    printf("\nA soma dos números %d até %d é = %d\n", m, n, soma);
    
}