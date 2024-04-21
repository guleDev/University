#include <stdio.h>
void main() {
    int flag = 0, i, num;
    printf("\nDigite um número: ");
    scanf("%d", &num);
    for (i = 2; i <= num / 2; i++)
        if ( num % i == 0 )
            flag = 1;
    if (flag = 1)
        printf("\n%d é um número COMPOSTO", num);
    else
        if ((num == 1)||(num == 0))
            printf("I número %d não é considerado primo", num);
        else
            printf("\n%d é um número PRIMO", num);
}