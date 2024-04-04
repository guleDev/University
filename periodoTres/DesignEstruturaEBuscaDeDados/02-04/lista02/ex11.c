#include <stdio.h>

int main() {
    int valor_saque, notas200, notas100, notas50, notas20, notas10, notas5, notas2, notas1;

    printf("Digite o valor do saque: ");
    scanf("%d", &valor_saque);

    notas200 = valor_saque / 200;
    valor_saque %= 200;

    notas100 = valor_saque / 100;
    valor_saque %= 100;

    notas50 = valor_saque / 50;
    valor_saque %= 50;

    notas20 = valor_saque / 20;
    valor_saque %= 20;

    notas10 = valor_saque / 10;
    valor_saque %= 10;

    notas5 = valor_saque / 5;
    valor_saque %= 5;

    notas2 = valor_saque / 2;
    valor_saque %= 2;

    notas1 = valor_saque;

    printf("Notas de 200 reais: %d\n", notas200);
    printf("Notas de 100 reais: %d\n", notas100);
    printf("Notas de 50 reais: %d\n", notas50);
    printf("Notas de 20 reais: %d\n", notas20);
    printf("Notas de 10 reais: %d\n", notas10);
    printf("Notas de 5 reais: %d\n", notas5);
    printf("Notas de 2 reais: %d\n", notas2);
    printf("Notas de 1 real: %d\n", notas1);

    return 0;
}