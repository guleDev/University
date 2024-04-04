#include <stdio.h>

int main () {
    char nome[7] = {'G', 'u', 's', 't', 'a', 'v', 'o'};
    char sobrenome[5] = {'P', 'a', 'm', 'p', 'u'};

    printf("%c %c %c %c %c %c %c\n", nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6]);
    printf("%c %c %c %c %c\nf", sobrenome[0], sobrenome[1], sobrenome[2], sobrenome[3], sobrenome[4]);

    return 0;
};