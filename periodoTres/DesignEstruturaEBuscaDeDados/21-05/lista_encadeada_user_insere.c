#include <stdio.h>
#include <stdlib.h>

/* Neste exemplo, o programa lê um valor do usuário e insere 
o valor no início da lista encadeada utilizando a função insertAtBeginning(). 
Em seguida, o programa pergunta ao usuário se ele deseja inserir mais um valor na lista. 
O programa continua a inserir valores na lista até que o usuário 
responda "N" ou "n". Por fim, o programa imprime a lista encadeada 
utilizando a função printList().*/

// Definição da struct Node
struct Node {
    int data;
    struct Node* next;
};

// Função para criar um novo nó
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Função para inserir um novo nó no início da lista encadeada
void insertAtBeginning(struct Node** headRef, int value) {
    struct Node* newNode = createNode(value);
    newNode->next = *headRef;
    *headRef = newNode;
}

// Função para imprimir a lista encadeada
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;
    int value;
    char option;

    do {
        // Lê o valor do usuário
        printf("Digite um valor: ");
        scanf("%d", &value);

        // Insere o valor no início da lista encadeada
        insertAtBeginning(&head, value);

        // Pergunta ao usuário se ele deseja inserir mais um valor
        printf("Deseja inserir mais um valor? (S/N) ");
        scanf(" %c", &option);
    } while (option == 'S' || option == 's');

    // Imprime a lista encadeada
    printf("Lista Encadeada: ");
    printList(head);

    return 0;
}

