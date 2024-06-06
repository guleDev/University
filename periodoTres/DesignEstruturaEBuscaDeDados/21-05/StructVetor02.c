/* Objetivo do Programa: Implementar uma struct, manipulando-a
                         por meio de array (vetor)
Nome do Programa.......: StructVetor02.c
*/
// 01 - Faça 5 perguntas com respostas (corretas) que você NÃO QUER QUE CAIA NA PROVA!!!!  (escolha as difíceis rsrs...)
#include <stdio.h>
#include <stdlib.h>

struct Produto {
    int codigo;
    char nome[25];
    float preco;
};

void main() {
    struct Produto produtos[50]; // Vetor de produtos com tamanho 50
	int i,n;
	
    
	printf("Digite a quantidade de produtos a serem cadastradas: ");	
	scanf("%d", &n);
	
	for(i=0;i<n;i++){
		//system("cls");
		printf("Digite o codigo do produto: ");
		scanf("%d",&produtos[i].codigo);
		fflush(stdin); // Limpa buffer do teclado
    	printf("Digite o nome do segundo produto: ");
      gets(produtos[i].nome);
     	printf("Digite o preco do segundo produto: ");
    	scanf("%f", &produtos[i].preco);
	
	}
	
	 // Exibindo os dados dos produtos
    printf("\n\nDADOS DOS PRODUTOS\n");
    printf("Codigo\t\tNome \t\t\t\tPreco\n");
    for (i = 0; i < n; i++) {
        printf("%10d\t%-25s\t%10.2f\n", produtos[i].codigo, produtos[i].nome, produtos[i].preco);
    }
}
