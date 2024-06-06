/* Objetivo do Programa: Implementar uma struct, manipulando-a
                         por meio de array (vetor)
Nome do Programa.......: StructVetor01.c
*/
//***** Tente adivinhar 5 perguntas com respostas que eu (prof. Elton) colocaria na Prova!!
#include <stdio.h>
#include <stdlib.h>

struct Produto {
    int codigo;
    char nome[25];
    float preco;
};

void main() {
    struct Produto produtos[3]; // Vetor de produtos com tamanho 3
	int i;
	
    // Preenchendo os dados do primeiro produto
    //produtos[0].codigo = 1; 
	printf("Digite o código do produto: ");	
	scanf("%d", &produtos[0].codigo);
	
	fflush(stdin); // Limpa buffer do teclado
		
   printf("Digite o nome do primeiro produto: ");
   //scanf("%s", produtos[0].nome);
   gets(produtos[0].nome);

    printf("Digite o preco do primeiro produto: ");
    scanf("%f", &produtos[0].preco);
	
	fflush(stdin); // Limpa buffer do teclado

    // Preenchendo os dados do segundo produto
    produtos[1].codigo = 2;
    
	printf("Digite o nome do segundo produto: ");
    //scanf("%s", produtos[1].nome);
    gets(produtos[1].nome);
    
    printf("Digite o preco do segundo produto: ");
    scanf("%f", &produtos[1].preco);

	fflush(stdin); // Limpa buffer do teclado

    // Preenchendo os dados do terceiro produto
    produtos[2].codigo = 3;
    
    printf("Digite o nome do terceiro produto: ");
    //scanf("%s", produtos[2].nome);
    gets(produtos[2].nome);
	    
    printf("Digite o preco do terceiro produto: ");
    scanf("%f", &produtos[2].preco);

    // Exibindo os dados dos produtos
    printf("\n\nDADOS DOS PRODUTOS\n");
    printf("Codigo\tNome\t\t\tPreco\n");
    for (i = 0; i < 3; i++) {
        printf("%d\t %.50s\t\t\t %.2f\n", produtos[i].codigo, produtos[i].nome, produtos[i].preco);
    }
}
