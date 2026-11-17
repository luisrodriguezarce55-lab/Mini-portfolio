# Banco de Dados Música

Projeto de modelagem e criação de um banco de dados relacional para o controle de CDs, músicas, autores e gravadoras, desenvolvido no **MySQL Workbench** a partir de um diagrama entidade-relacionamento (ER).

## Sobre o projeto

O banco de dados organiza o catálogo de uma loja de CDs: cada CD pertence a uma gravadora, possui várias faixas (músicas) e cada música pode ter um ou mais autores. Também permite classificar os CDs por faixa de preço e indicar outro CD relacionado.

## Estrutura do banco

| Tabela | Descrição |
|---|---|
| `gravadora` | Gravadoras, com endereço, telefone, contato e site |
| `cd` | CDs com preço de venda, data de lançamento, estilo, vendas e CD indicado |
| `musica` | Músicas com nome e duração |
| `autor` | Autores das músicas |
| `musica_autor` | Relaciona as músicas aos seus autores |
| `faixa` | Relaciona as músicas aos CDs e guarda o número da faixa |
| `cd_categoria` | Categorias de CD por faixa de preço (menor e maior preço) |

## Relacionamentos principais

- Uma **gravadora** pode ter vários **CDs**.
- Um **CD** pode indicar outro CD (auto relacionamento em `cd_indicado`).
- Um **CD** possui várias **músicas** e uma música pode estar em vários CDs (`faixa`).
- Uma **música** pode ter vários **autores** e um autor pode ter várias músicas (`musica_autor`).

## Arquivos

- `musica_modelo_er.mwb` – modelo ER feito no MySQL Workbench.
- `Code.txt` – script SQL com a criação das tabelas e a inserção dos dados de exemplo.

## Como executar

1. Instale o **MySQL Server** e o **MySQL Workbench**.
2. Crie e selecione o banco de dados:
   ```sql
   create database musica;
   use musica;
   ```
3. Abra o conteúdo de `Code.txt` no MySQL Workbench.
4. Execute o script (`Ctrl + Shift + Enter`).
5. Confira as tabelas criadas no schema `musica`.

## Tecnologias

- MySQL
- MySQL Workbench

## Autor

Feito por **Luis Felipe Rodriguez Arce**
