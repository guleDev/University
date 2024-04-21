#include <stdio.h>
#include <locale.h>

int main() {
    char letra;
    setlocale (LC_ALL, "Portuguese");
    printf("\n Digite qualquer caractere: ");
    scanf("%c", &letra);
    switch(letra) {
        case 'A':
        case 'a':
            printf("\n %c é VOGAL", letra);
            break;
        case 'E':
        case 'e':
            printf("\n %c é VOGAL", letra);
            break;
        case 'I':
        case 'i':
            printf("\n %c é VOGAL", letra);
            break;
        case 'O':
        case 'o':
            printf("\n %c é VOGAL", letra);
            break;    
        case 'U':
        case 'u':
            printf("\n %c é VOGAL", letra);
            break;
        default: printf("\n %c não é uma vogal", letra);
    }
    return 0;
}
