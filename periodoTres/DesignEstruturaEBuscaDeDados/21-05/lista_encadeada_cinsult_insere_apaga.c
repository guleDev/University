#include <stdio.h>
#include <stdlib.h>

typedef struct item {
    int valor;
    struct item* proximo;
} Item;


void inserir_item(Item** inicio, int valor) {
    Item* novo = (Item*) malloc(sizeof(Item));
    novo->valor = valor;
    novo->proximo = NULL;
    
    if (*inicio == NULL) {
        *inicio = novo;
    } else {
        Item* atual = *inicio;
        while (atual->proximo != NULL) {
            atual = atual->proximo;
        }
        atual->proximo = novo;
    }
}

void excluir_item(Item** inicio, int valor) {
    if (*inicio == NULL) {
        return;
    }
    
    if ((*inicio)->valor == valor) {
        Item* temp = *inicio;
        *inicio = (*inicio)->proximo;
        free(temp);
    } else {
        Item* atual = *inicio;
        while (atual->proximo != NULL && atual->proximo->valor != valor) {
            atual = atual->proximo;
        }
        if (atual->proximo != NULL) {
            Item* temp = atual->proximo;
            atual->proximo = atual->proximo->proximo;
            free(temp);
        }
    }
}

void imprimir_itens(Item* inicio) {
    Item* atual = inicio;
    printf("Itens:\n");
    while (atual != NULL) {
        printf("%d\n", atual->valor);
        atual = atual->proximo;
    }
    printf("\n");
}

int main() {
    Item* inicio = NULL;
    int opcao, valor;
    
    do {
        printf("1 - Inserir item\n");
        printf("2 - Consultar itens\n");
        printf("3 - Excluir item\n");
        printf("4 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", opcao);//&opcao
        
        switch(opcao) {
            case 1:
                printf("Digite o valor do item: ");
                scanf("%d", &valor);
                inserir_item(&inicio, valor);
                break;
            case 2:
                imprimir_itens(inicio);
                break;
            case 3:
                printf("Digite o valor do item a ser excluido: ");
                scanf("%d", &valor);
                excluir_item(&inicio, valor);
                break;
            case 4:
                printf("Encerrando o programa.\n");
                break;
            default:
                printf("Opcao invalida.\n");
        }
        
        printf("\n");
    } while (opcao != 4);
    
    return 0;
}
/* Explicação:

O programa começa definindo uma estrutura Item, que contém um valor inteiro 
e um ponteiro para o próximo item da lista encadeada. Em seguida, são declaradas 
as funções imprimir_itens, inserir_item e excluir_item.

A função imprimir_itens recebe o ponteiro para o primeiro item da lista 
encadeada e percorre a lista, imprimindo cada valor na tela.

A função inserir_item recebe o endereço do ponteiro para o primeiro item 
da lista encadeada e um valor inteiro. Ela cria um novo item e adiciona 
ao final da lista.

A função excluir_item recebe o endereço do ponteiro para o  */


