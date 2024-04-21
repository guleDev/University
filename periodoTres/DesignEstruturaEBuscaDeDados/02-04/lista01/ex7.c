#include <stdio.h>
#include <locale.h>

void main() {
    int endereco;
    int matricula = 1010;

    system("cls");
    setlocale(LC_ALL, "portuguese");
    printf ( "\nO conteúdo (valor) da variável matricula é: %d", matricula);
    printf ( "\nEndereço da variável matricula é..........: %p", &matricula);
    printf ( "\nEndereço da variável matricula é..........: %ls", &matricula);
    getchar();
}