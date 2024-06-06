/*
 Estrutura de Dados - STRUCT (registro; conjuntos de dados)
                      Ideia: Coletar e armazenar os dados de maneira ORGANIZADA (divisões e subdivisões)

 Elaborar um programa em linguagem C que implemente e mostre a FICHA CADASTRAL
 Permitir, via MENU, as opções Cadastrar, Alterar, Consultar, Excluir e Sair.                    
                     
O que iremos usar?
- Usaremos alguma Estrutura de Dados? SIM
- Qual? struct
- Para que? Para organizar (estruturar os dados)
- Armazenar dados para quantas pessoas? Eu não sei; logo, projetar um número razoável
- Estrutura de Repetição? SIM
- Qual a mais adequada? FOR
*/
  
#include <stdio.h>

void cadastrar_ficha()
{


	
	
	printf("\n           CPF: ");			scanf("%d", ficha.cpf); 	
	// Verificar se a ficha da pessoa JÁ EXISTE - Se existir, não poderá cadastrar	
	// laço correndo todas as fichas já cadastrar
	//  if (cpf) já existir, mensagem de aviso - ESSE CPF já EXISTE !!!
	
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
// Definição das estruturas da ficha cadastral
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
		struct DataNasc data;	// outra opção: char  datanasc[8];				
		struct Endereco endereco;
		char telefone[12];		
		char casa_propria;	// 'S' ou 'N'	cuidado em validar MAIÚSCULAS e minúsculas
		char nome_empresa[45]; 
		char secao[30];
		int tempo_trab;
		float renda_mensal;  
		char estado_civil;  									
	} ;
		
	struct FichaCadastral ficha;

	
	
	// construir o menu com as opções
	// usar switch..case
	// cada case, chamar uma função ( a ser criada, antes da função main() )
	// desenvolver o conteúdo de cada função
	
	// Verificar se a ficha da pessoa JÁ EXISTE - 
	// Se a ficha existir então permitir apenas consultar, alterar, excluir
	// Senão permitir apenas cadastrar
	// COMO fazer para verificar se a ficha EXISTE ou NÃO?
	// usar um campo que seja UNICO (rg, cpf, ...)
	
	
	getch();
	
	return 0;

}


