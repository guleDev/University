/* Objetivo do Programa: Implementar uma struct, manipulando-a
                         por meio de ponteiros (alocação dinâmica)
Nome do Programa.......: Struct02.c
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

    // Lendo a quantidade de produtos do usuário
    printf("Digite a quantidade de produtos: ");
    scanf("%d", &n);

    // Alocando dinamicamente um vetor de produtos com tamanho n
    produtos = (struct Produto *) malloc(n * sizeof(struct Produto));
    if (produtos == NULL) {
    // Falha ao alocar memória
    exit(1);
}

    // Preenchendo os dados dos produtos
    for (i = 0; i < n; i++) {
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
    printf("Codigo\t Nome\t\t\t Preco\n");
    for (i = 0; i < n; i++) {
        printf("%d\t%s\t\t%.2f\n", produtos[i].codigo, produtos[i].nome, produtos[i].preco);
    }

    // Liberando a memória alocada
    free(produtos);
}
