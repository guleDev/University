#include <stdio.h>

int main() {
    float valor_produto, desconto, valor_com_desconto;

    printf("Digite o valor do produto: ");
    scanf("%f", &valor_produto);

    desconto = valor_produto * 0.3;

    valor_com_desconto = valor_produto - desconto;

    printf("O valor do produto com 30%% de desconto é: R$ %.2f\n", valor_com_desconto);

    return 0;
}