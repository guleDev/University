#include <stdio.h>

int main() {
    int codigo_decimal;

    printf("digite o codigo decimal: ");
    scanf("%d", &codigo_decimal);


    printf("O caractere correspondente ao código decimal %d e: %c\n", codigo_decimal, codigo_decimal);

    return 0;
}