#include <stdio.h>
#include <stdlib.h>

int main()
{
	// criando a vari�vel ponteiro para o arquivo
	FILE *pont_arq;
  
	//abrindo o arquivo 
	pont_arq = fopen("arquivo.txt", "a");
	
	if (pont_arq == NULL)
	    printf("\nERRO! O arquivo n�o foi aberto!\n");
	else
        printf("\nO arquivo foi criado com sucesso!\n");

	// fechando arquivo
  	fclose(pont_arq);
  
  	system("pause");
  	return(0);
}
