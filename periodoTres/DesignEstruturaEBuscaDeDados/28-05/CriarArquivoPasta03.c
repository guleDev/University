#include <stdio.h>
#include <locale.h>
#include <windows.h>

void main()
{
	setlocale(LC_ALL, "portuguese");
	SetConsoleTitle("Exemplo 04 - Criando Arquivo em local específico");

	// Usando a função CreateFile
	// Createfile(nome_arquivo, tipo_acesso, compartilhamento, tipo_segurança, tipo_criacao_arquivo, atributos, template_arquivo)
	if (CreateFile("C:\\testes.txt", GENERIC_READ, 0, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL))
		printf("Arquivo criado com sucesso!!!");
	else
		printf("Erro ao criar o arquivo!!!");	
	
	
	FILE *ponteiro_para_arquivo;

	// Fechando o arquivo
	fclose(ponteiro_para_arquivo);	
	printf("\nArquivo fechado com sucesso!!!");
}

