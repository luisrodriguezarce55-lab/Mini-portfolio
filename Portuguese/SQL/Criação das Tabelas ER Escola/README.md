# Banco de Dados Escola

Projeto de modelagem e criação de um banco de dados relacional para o controle acadêmico de uma escola, desenvolvido no **MySQL Workbench** a partir de um diagrama entidade-relacionamento (ER).

## Sobre o projeto

O banco de dados `escola` organiza informações de disciplinas, professores, alunos, turmas, avaliações e notas, permitindo acompanhar a matrícula dos alunos nas turmas e o desempenho em cada avaliação.

## Estrutura do banco

| Tabela | Descrição |
|---|---|
| `disciplina` | Disciplinas oferecidas |
| `professor` | Professores responsáveis |
| `aluno` | Alunos cadastrados |
| `turma` | Turmas por ano, semestre e disciplina |
| `turma_aluno` | Relaciona os alunos às turmas em que estão matriculados |
| `avaliacao` | Avaliações de cada turma, com seu peso |
| `nota` | Nota obtida por cada aluno em cada avaliação |

## Relacionamentos principais

- Uma **turma** é identificada por `ano`, `semestre` e `cod_disciplina`.
- Um **aluno** pode estar matriculado em várias turmas (`turma_aluno`).
- Cada **turma** possui várias **avaliações**.
- Cada **nota** pertence a um aluno e a uma avaliação.

## Arquivos

- `Model_ER-Escola.mwb` – modelo ER feito no MySQL Workbench.
- `Escola.sql` – script SQL com a criação das tabelas.

## Como executar

1. Instale o **MySQL Server** e o **MySQL Workbench**.
2. Crie o banco de dados:
   ```sql
   create database escola;
   ```
3. Abra o arquivo `Escola.sql` no MySQL Workbench.
4. Execute o script (`Ctrl + Shift + Enter`).
5. Confira as tabelas criadas no schema `escola`.

> **Observação:** execute o script na ordem correta. As tabelas `turma` e `aluno` precisam existir antes de `turma_aluno`, `avaliacao` e `nota`, pois elas possuem chaves estrangeiras.

## Tecnologias

- MySQL
- MySQL Workbench

## Autor

Feito por **Luis Felipe Rodriguez Arce**
