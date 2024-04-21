#include <stdio.h>

char *mensagem[] = {"arquivo não encontrado", "erro de leitura", "erro de escrita", "impossível criar arquivo"};

void escreverMensagemDeErro (int num) {
    printf("%s\n", mensagem[num]);
}

int main(){
    escreverMensagemDeErro( 3 );
}