use escola;

create table turma_aluno (
    ano             int(4) not null,
    semestre        int(1) not null,
    cod_disciplina  int(3) not null,
    Matricula_aluno int(3) not null,
    primary key (ano, semestre, cod_disciplina, Matricula_aluno),
    constraint fk_turmaaluno_turma
        foreign key (ano, semestre, cod_disciplina)
        references turma (ano, semestre, cod_disciplina),
    constraint fk_turmaaluno_aluno
        foreign key (Matricula_aluno)
        references aluno (Matricula_aluno)
);

create table avaliacao (
    ano            int(4) not null,
    semestre       int(1) not null,
    cod_disciplina int(3) not null,
    Cod_avaliacao  int(3) not null,
    Peso           int(2),
    primary key (ano, semestre, cod_disciplina, Cod_avaliacao),
    constraint fk_avaliacao_turma
        foreign key (ano, semestre, cod_disciplina)
        references turma (ano, semestre, cod_disciplina)
);

create table nota (
    ano             int(4) not null,
    semestre        int(1) not null,
    cod_disciplina  int(3) not null,
    Cod_avaliacao   int(3) not null,
    Matricula_aluno int(3) not null,
    Nota            int(5),
    primary key (ano, semestre, cod_disciplina, Cod_avaliacao, Matricula_aluno),
    constraint fk_nota_avaliacao
        foreign key (ano, semestre, cod_disciplina, Cod_avaliacao)
        references avaliacao (ano, semestre, cod_disciplina, Cod_avaliacao),
    constraint fk_nota_aluno
        foreign key (Matricula_aluno)
        references aluno (Matricula_aluno)
);