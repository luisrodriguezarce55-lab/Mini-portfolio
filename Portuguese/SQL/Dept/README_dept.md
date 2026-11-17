# Banco de Dados Departamentos e Funcionários

Projeto de criação de um banco de dados relacional para o controle de departamentos e funcionários de uma empresa, desenvolvido para o **MySQL**.

## Sobre o projeto

O banco de dados armazena os departamentos da empresa, com sua localização e orçamento, e os funcionários, com cargo, gerente, data de admissão, salário e comissão. O script já inclui dados de exemplo para praticar consultas SQL.

## Estrutura do banco

### Tabela `dept`

| Campo | Tipo | Descrição |
|---|---|---|
| `DepNume` | int(4) | Número do departamento (chave primária) |
| `DepNome` | char(20) | Nome do departamento |
| `DepLoca` | char(20) | Cidade onde fica o departamento |
| `DepOrca` | int(12) | Orçamento do departamento |

### Tabela `emp`

| Campo | Tipo | Descrição |
|---|---|---|
| `EmpNume` | int(5) | Número do funcionário (chave primária) |
| `EmpNome` | char(30) | Nome do funcionário |
| `EmpGere` | int(5) | Número do gerente do funcionário |
| `EmpServ` | char(20) | Cargo (gerente, vendedor, analista, etc.) |
| `DepNume` | int(4) | Número do departamento onde trabalha |
| `EmpAdmi` | date | Data de admissão |
| `EmpSala` | int(10) | Salário |
| `EmpComi` | int(10) | Comissão |

## Relacionamentos

- Um **departamento** possui vários **funcionários** (`emp.DepNume` se refere a `dept.DepNume`).
- Um **funcionário** pode ter um **gerente**, que também é um funcionário (`emp.EmpGere` se refere a `emp.EmpNume`).

## Arquivos

- `Modelo_ER-dept.mwb` – modelo ER feito no MySQL Workbench.
- `Code_Dept.sql` – script SQL com a criação das tabelas e a inserção dos dados de exemplo.

## Como executar

1. Instale o **MySQL Server** e o **MySQL Workbench**.
2. Crie e selecione o banco de dados:
   ```sql
   create database empresa;
   use empresa;
   ```
3. Abra o arquivo `Code_Dept.sql` no MySQL Workbench.
4. Execute o script (`Ctrl + Shift + Enter`).
5. Confira as tabelas `dept` e `emp` no schema criado.

## Tecnologias

- MySQL
- MySQL Workbench

## Autor

Feito por **Luis Felipe Rodriguez Arce**
