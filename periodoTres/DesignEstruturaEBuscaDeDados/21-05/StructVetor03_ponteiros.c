/* Objetivo do Programa: Implementar uma struct, manipulando-a
                         por meio de ponteiros (aloca��o din�mica)
Nome do Programa.......: StructVetor03_ponteiros.c
*/

#include <stdio.h>
#include <stdlib.h>

struct Produto {
    int codigo;
    char nome[50];
    float preco;
};

void main() {
    struct Produto *produtos; // Ponteiro para a struct Produto
    int n; // Quantidade de produtos
    int i; 

    // Lendo a quantidade de produtos do usu�rio
    printf("Digite a quantidade de produtos: ");
    scanf("%d", &n);

    // Alocando dinamicamente para "n" struct's.
    produtos =  malloc(n * sizeof(struct Produto));
    

    // Preenchendo os dados dos produtos
    for (i = 0; i < n; i++) {
    	//produtos =  malloc(sizeof(struct Produto)); //espa�o reservado para UMA struct.
	     produtos[i].codigo = i + 1;
        
		fflush(stdin); // Limpa buffer do teclado
		
		printf("Digite o nome do produto %d: ", i + 1);
        //scanf("%s", produtos[i].nome);
        gets(produtos[i].nome);
        
        printf("Digite o preco do produto %d: ", i + 1);
        scanf("%f", &produtos[i].preco);
    }

  // Exibindo os dados dos produtos
    printf("\n\nDADOS DOS PRODUTOS\n");
    printf("Codigo\t\tNome \t\t\t\tPreco\n");
    for (i = 0; i < n; i++) {
        printf("%10d\t%-25s\t%10.2f\n", produtos[i].codigo, produtos[i].nome, produtos[i].preco);
    }

    // Liberando a mem�ria alocada
    free(produtos);
}


