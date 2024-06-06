#include <stdio.h>
#include <locale.h>
#include <windows.h>

void main()
{
	setlocale(LC_ALL, "portuguese");
	SetConsoleTitle("Exemplo 01 - Criando Arquivo");
	
	FILE *ponteiro_para_arquivo;

	// Criando um arquivo
	ponteiro_para_arquivo = fopen("arquivo.txt", "w");
	if(ponteiro_para_arquivo==NULL)
		printf("Ocorreu um erro...");
	else
		printf("Arquivo criado com sucesso!!!");
	
	/* Observa��es:
 	   Perceba que o arquivo ser� criado no mesmo local
	   que o programa
	   O arquivo rec�m criado n�o possui conte�do
	*/

	// Fechando o arquivo
	fclose(ponteiro_para_arquivo);	
}

