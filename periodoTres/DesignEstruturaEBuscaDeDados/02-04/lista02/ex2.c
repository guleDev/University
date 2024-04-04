#include <stdio.h>

int main() {
    float base, altura, area;

    printf("digite a base do retangulo: ");
    scanf("%f", &base);

    printf("digite a altura do retangulo: ");
    scanf("%f", &altura);

    area = base * altura;

    printf("A area do retangulo com base %.2f e altura %.2f e: %.2f\n", base, altura, area);

    return 0;
}