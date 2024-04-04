#include <stdio.h>

int main() {
    float num1, num2, media;

    printf("digite o primeiro número: ");
    scanf("%f", &num1);

    printf("digite o segundo número: ");
    scanf("%f", &num2);

    media = (num1 + num2) / 2;

    printf("a media entre %.2f e %.2f é: %.2f\n", num1, num2, media);
    return 0;
}