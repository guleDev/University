#include <stdio.h>
#include <locale.h>

int main() {
    char letra;
    setlocale(LC_ALL, "Portuguese");
    printf("\nDigite qualquer caractere: ");
    scanf("%c", &letra);
    if ((letra == 'a') || (letra == 'A'))
        printf("\n%c é VOGAL", letra);
    else if ((letra == 'e') || (letra == 'E'))
        printf("\n%c é VOGAL", letra);
    else if ((letra == 'i') || (letra == 'I'))
        printf("\n%c é VOGAL", letra);
    else if ((letra == 'o') || (letra == 'O'))
        printf("\n%c é VOGAL", letra);
    else if ((letra == 'u') || (letra == 'U'))
        printf("\n%c é VOGAL", letra);
    else 
        printf("\n%c NÃO é VOGAL", letra);
    return 0;
}