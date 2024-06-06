// Escreva um programa para ler e exibir as informações de um aluno usando uma estrutura aninhada

#include <stdio.h>

int main()
{
	struct DataNasc// 01 - Comente sobre o que é uma STRUCT e sua relação com DataNasc, dia, mes e ano.
	{
		int dia;
		int mes;
		int ano;
	};

	struct Estudante
	{
		int matricula;
		char nome[100];// 02 - o que representa essa linha?
		float mensalidade;
		struct DataNasc data;// 03 - e agora? explique essa linha, explique as relações existentes.
	};
		
	
	struct Estudante stud1;// 05 - O que faz essa linha?

	printf("\n Nome       : ");			gets(stud1.nome); // 06 - Qual a diferença entre gets, fgets e scanf.
	printf("\n Matricula  : ");			scanf("%d", &stud1.matricula);
	printf("\n Mensalidade: ");			scanf("%f", &stud1.mensalidade);
	printf("\n Data Nasc  : ");			scanf("%d %d %d", &stud1.data.dia, &stud1.data.mes, &stud1.data.ano);


	printf("\n ********DADOS DO ESTUDANTE *******");
	printf("\n Matricula   = %d", stud1.matricula);// 07 - o que faz essa linha?
	printf("\n Nome        = %s", stud1.nome);// 08 - explique a estrutura "stud1.nome"
	printf("\n Mensalidade = %0.2f", stud1.mensalidade);// 09 - Qual a função do "." nessa linha?
	printf("\n Data Nasc   = %d %d %d", stud1.data.dia, stud1.data.mes, stud1.data.ano);// 10 - Que "bagunça"... e agora? explique isso tudo.
	getch();// 11 - o que faz essa linha
	return 0;

}

