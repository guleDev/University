public class cadastroAluno {
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Gustavo", "Eng. Soft.", 12345);
        Aluno aluno2 = new Aluno("Adrian", "Eng. Soft.", 23456);

        aluno1.apresentar();
        aluno2.apresentar();
    }
}

class Aluno {
    private String nome;    
    private String curso;
    private int matricula;   
    
    public Aluno(String nome, String curso, int matricula) {
        this.nome = nome;
        this.curso = curso;
        this.matricula = matricula;
    }

    public void apresentar() {
        System.out.println("Aluno: "+ nome + "\nCurso: " + curso + "\nNúmero de Matricula: " + matricula);
    }
}