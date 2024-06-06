#include <stdio.h>
#include <locale.h>
#include <windows.h>

void main()
{
	setlocale(LC_ALL, "portuguese");
	SetConsoleTitle("Exemplo 03 - Criando Arquivo em local espec�fico");

	// Usando a fun��o CreateDirectory
	// CreateDirectory(nome do arquivo, seguran�a)
	if (CreateDirectory("c:\\testes", NULL))
		printf("Pasta criada com sucesso!!!");
	else
		printf("A pasta j� existe!!!");	
	
	
	FILE *ponteiro_para_arquivo;

	// Criando um arquivo em local espec�fico
	// Em Windows: C:\\pasta\\subpasta\\arquivo
	ponteiro_para_arquivo = fopen("c:\\testes\\dados.txt", "w");
	printf("\nArquivo criado com sucesso!!!");

	// Fechando o arquivo
	fclose(ponteiro_para_arquivo);	
	printf("\nArquivo fechado com sucesso!!!");
}

