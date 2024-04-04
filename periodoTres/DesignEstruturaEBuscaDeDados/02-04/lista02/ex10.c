#include <stdio.h>

int main() {
    int a, b, temp;

    printf("digite o primeiro valor inteiro: ");
    scanf("%d", &a);

    printf("digite o segundo valor inteiro: ");
    scanf("%d", &b);

    temp = a;
    a = b;
    b = temp;

    printf("o novo valor do primeiro inteiro e0: %d\n", a);
    printf("o novo valor do segundo inteiro e: %d\n", b);

    return 0;
}