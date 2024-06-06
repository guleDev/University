/*
 Estrutura de Dados - STRUCT (registro; conjuntos de dados)
                      Ideia: Coletar e armazenar os dados de maneira ORGANIZADA (divis�es e subdivis�es)

 Elaborar um programa em linguagem C que implemente e mostre a FICHA CADASTRAL
 Permitir, via MENU, as op��es Cadastrar, Alterar, Consultar, Excluir e Sair.                    
                     
O que iremos usar?
- Usaremos alguma Estrutura de Dados? SIM
- Qual? struct
- Para que? Para organizar (estruturar os dados)
- Armazenar dados para quantas pessoas? Eu n�o sei; logo, projetar um n�mero razo�vel
- Estrutura de Repeti��o? SIM
- Qual a mais adequada? FOR
*/
  
#include <stdio.h>

void cadastrar_ficha()
{


	
	
	printf("\n           CPF: ");			scanf("%d", ficha.cpf); 	
	// Verificar se a ficha da pessoa J� EXISTE - Se existir, n�o poder� cadastrar	
	// la�o correndo todas as fichas j� cadastrar
	//  if (cpf) j� existir, mensagem de aviso - ESSE CPF j� EXISTE !!!
	
	printf("\n Nome Completo: ");			gets(ficha.nome_completo); 
	printf("\n            RG: ");			scanf("%d", ficha.rg); 		
	printf("\n Nacionalidade: ");			gets(ficha.nacionalidade); 		
	printf("\n    Natural de: ");			gets(ficha.natural); 		
	//...
		
}

void alterar_ficha()
{
	
} 

void consultar_ficha()
{
	
} 

void excluir_ficha()
{
	
} 

int main()
// Defini��o das estruturas da ficha cadastral
{
	struct DataNasc
	{
		int dia;
		int mes;
		int ano;
	};

	struct Endereco
	{
		char logradouro[20];  // Rua, Travessa, Avenida, ...
		char nome_ende[30];
		int num;
		char bairro[30];
		char cidade[45];
		char estado[25];
	};

	struct FichaCadastral
	{
		char nome_completo[90];
		int  rg;
		int cpf;
		char nacionalidade[50];
		char natural[80];
		struct DataNasc data;	// outra op��o: char  datanasc[8];				
		struct Endereco endereco;
		char telefone[12];		
		char casa_propria;	// 'S' ou 'N'	cuidado em validar MAI�SCULAS e min�sculas
		char nome_empresa[45]; 
		char secao[30];
		int tempo_trab;
		float renda_mensal;  
		char estado_civil;  									
	} ;
		
	struct FichaCadastral ficha;

	
	
	// construir o menu com as op��es
	// usar switch..case
	// cada case, chamar uma fun��o ( a ser criada, antes da fun��o main() )
	// desenvolver o conte�do de cada fun��o
	
	// Verificar se a ficha da pessoa J� EXISTE - 
	// Se a ficha existir ent�o permitir apenas consultar, alterar, excluir
	// Sen�o permitir apenas cadastrar
	// COMO fazer para verificar se a ficha EXISTE ou N�O?
	// usar um campo que seja UNICO (rg, cpf, ...)
	
	
	getch();
	
	return 0;

}


