// Escreva um programa usando estruturas para ler e exibir as informações sobre um aluno

#include <stdio.h>

int main()
{
struct estudante
{
	int 	matricula;
	char 	nome_completo[85];
	float 	valor_mensalidade;
	char	data_nasc[8];
};
struct estudante stud1; // Criando um apelido (stud1) para manipular toda a estrutura estudante

printf("\n Nome		  : ");		scanf("%s", &stud1.nome_completo);
//printf("\n Nome		  : ");			gets(stud1.nome_completo); // alertar para scanf inteiro antes
printf("\n Matricula  : ");			scanf("%d", &stud1.matricula);
printf("\n Mensalidade: ");			scanf("%f", &stud1.valor_mensalidade);
printf("\n Data Nasc  : ");			scanf("%s", stud1.data_nasc);

printf("\n ********DADOS DO ESTUDANTE *******");
printf("\n Matricula   = %d", stud1.matricula);
printf("\n Nome        = %s", stud1.nome_completo);
printf("\n Mensalidade = %0.2f", stud1.valor_mensalidade);
printf("\n Data Nasc   = %s", stud1.data_nasc);
//getch();
return 0;
}

