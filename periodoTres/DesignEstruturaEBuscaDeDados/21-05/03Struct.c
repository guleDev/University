// Escreva um programa para ler e exibir as informa��es de todos os alunos de uma classe. 
// Em seguida, edite os detalhes do i� aluno e exiba novamente todas as informa��es.

#include <stdio.h>
#include <string.h>
#include <ncurses.h>

int main()
{
	struct estudante
	{
		int 	matricula;
		char 	nome_completo[85];
		float 	valor_mensalidade;
		char	data_nasc[8];
	};
	struct estudante stud[50];//01 - Qual o nome da vari�vel? Qual seu tipo? O que possibilitou que isso ocorresse?
//02 - Explique o que representa os [ ]'s 12, 14 e 16. Qual a rela��o entre eles?
	int n, i;
	
	printf("\n Entre com o numero de estudantes : ");
	scanf("%d", &n);
	
	fflush(stdin);
	for(i=0;i<n;i++)//03 - Qual a fun��o desse FOR?
	{
		printf("\n Nome       : ");			fgets(stud[i].nome_completo); 
		printf("\n Matricula  : ");			scanf("%d", &stud[i].matricula);//04 - Por que nesta linha tem o "&" e na anterior n�o?
		printf("\n Mensalidade: ");			scanf("%f", &stud[i].valor_mensalidade);
		printf("\n Data Nasc  : ");			scanf("%s", stud[i].data_nasc);
		fflush(stdin); // limpar buffer teclado
	}

	for(i=0;i<n;i++)//05 - Qual a fun��o desse FOR?
	{
		printf("\n ********DADOS DO ESTUDANTE %d *******",i+1);//06 - Explique o comando "i+1". No que ele difere do i++ no FOR?
		printf("\n Matricula   = %d", stud[i].matricula);	//07 - Explique essa linha.
		printf("\n Nome        = %s", stud[i].nome_completo);//08 - O que o "i" representa aqui?
		printf("\n Mensalidade = %0.2f", stud[i].valor_mensalidade);
		printf("\n Data Nasc   = %s", stud[i].data_nasc);	}

	getch();
	return 0;
}

