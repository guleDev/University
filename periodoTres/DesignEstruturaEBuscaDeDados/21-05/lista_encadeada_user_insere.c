#include <stdio.h>
#include <stdlib.h>

/* Neste exemplo, o programa l� um valor do usu�rio e insere 
o valor no in�cio da lista encadeada utilizando a fun��o insertAtBeginning(). 
Em seguida, o programa pergunta ao usu�rio se ele deseja inserir mais um valor na lista. 
O programa continua a inserir valores na lista at� que o usu�rio 
responda "N" ou "n". Por fim, o programa imprime a lista encadeada 
utilizando a fun��o printList().*/

// Defini��o da struct Node
struct Node {
    int data;
    struct Node* next;
};

// Fun��o para criar um novo n�
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Fun��o para inserir um novo n� no in�cio da lista encadeada
void insertAtBeginning(struct Node** headRef, int value) {
    struct Node* newNode = createNode(value);
    newNode->next = *headRef;
    *headRef = newNode;
}

// Fun��o para imprimir a lista encadeada
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
        // L� o valor do usu�rio
        printf("Digite um valor: ");
        scanf("%d", &value);

        // Insere o valor no in�cio da lista encadeada
        insertAtBeginning(&head, value);

        // Pergunta ao usu�rio se ele deseja inserir mais um valor
        printf("Deseja inserir mais um valor? (S/N) ");
        scanf(" %c", &option);
    } while (option == 'S' || option == 's');

    // Imprime a lista encadeada
    printf("Lista Encadeada: ");
    printList(head);

    return 0;
}

