#include <stdio.h>

void main() {
    int numero;

    printf("\nDigite um número: ");
    scanf("%d", &numero);

    if (numero % 2 == 0)
        printf("\nO valor %d é PAR", numero);
    else
        printf("\nO valor %d é IMPAR", numero);
    
    printf("\nO resto da divisão de %d por 2 = %d", numero, numero % 2);

    switch ((numero % 2)){
    case 0:
        printf("\n%c é PAR", numero);
        break;
    case 1:
        printf("\n%c é IMPAR", numero);
        break;
    }
}