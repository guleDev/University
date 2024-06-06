#include <stdio.h>
#include <locale.h>
#include <windows.h>

void main()
{
	setlocale(LC_ALL, "portuguese");
	SetConsoleTitle("Exemplo 02 - Criando Arquivo em local específico");

	// Usando a função system
	system("mkdir C:\\testes");
	
	printf("\nPasta criada com sucesso!!!");
	
	FILE *ponteiro_para_arquivo;

	// Criando um arquivo em local específico
	// Em Windows: C:\\pasta\\subpasta\\arquivo
	ponteiro_para_arquivo = fopen("c:\\testes\\dados.txt", "w");
	printf("\nArquivo criado com sucesso!!!");

	// Fechando o arquivo
	fclose(ponteiro_para_arquivo);	
	printf("\nArquivo fechado com sucesso!!!");
}

