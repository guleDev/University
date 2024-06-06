#include <stdio.h>
#include <conio.h>
#include <local.h>

main() {
    int i, n;
    float peso[20];

    setlocale(LC_ALL, "portuguese");

    printf("%d bytes já ocupados.", sizeof(peso)); //int

    printf("\n Peso para quantas pessoas? ");
    scanf("%d", &n);

    for(i=0; i<n; i++){
        printf("\n O peso da %da pessoa é: ", i+1);
        scanf("%f", &peso[i]);
    }
    printf("\n Peso(s) digitado(s): ");

    for(i=0; i<n; i++){
        printf("\n %.2f", peso[i]);
    }
}