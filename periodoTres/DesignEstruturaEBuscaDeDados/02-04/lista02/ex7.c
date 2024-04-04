#include <stdio.h>
#define PI 3.14

int main() {
    float raio, area;

    printf("digite o raio do circulo: ");
    scanf("%f", &raio);

    area = PI * raio * raio;

    printf("a area do circulo com raio %.2f e: %.2f\n", raio, area);

    return 0;
}