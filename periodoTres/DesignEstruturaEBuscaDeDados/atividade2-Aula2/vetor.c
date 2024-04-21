#include <stdio.h>

int main() {
    int *aponta;
    int valor1, valor2;

    valor1 = 5;
    aponta = &valor1;
    valor2 = *aponta;
    printf("%i\n", aponta);
    printf("%i\n", valor2);
}