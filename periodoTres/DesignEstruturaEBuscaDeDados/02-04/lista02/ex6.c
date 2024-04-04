#include <stdio.h>

int main() {
    int numero;

    printf("digite um número inteiro: ");
    scanf("%d", &numero);

    if (numero % 5 == 0) {
        printf("o numero %d é divisivel por 5.\n", numero);
    } else {
        printf("o numero %d não é divisível por 5.\n", numero);
    }

    return 0;
}