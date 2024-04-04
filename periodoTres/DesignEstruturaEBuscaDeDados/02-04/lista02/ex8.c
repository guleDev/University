#include <stdio.h>

int main() {
    float valor_produto, valor_com_desconto;

    printf("digite o valor do produto: ");
    scanf("%f", &valor_produto);

    valor_com_desconto = valor_produto * 0.7;

    printf("o valor do produto com 30%% de desconto de e: R$ %.2f\n", valor_com_desconto);

    return 0;
}