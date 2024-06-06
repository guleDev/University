#include <stdio.h>

int main() {
    int matriz[3][3];
    int i,j;

    printf("Insira os valores para a matriz 3x3: \n");
    for(i=0; i<3; i++){
        for(j = 0; j<3; j++){
            printf("Elemento [%d][%d]", i, j);
        }
    }
}