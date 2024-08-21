# Simulador de Escalonador de Processos
Repositório com o código de um simulador de escalonador de processos em python.

Feito para a disciplina de Sistemas Operacionais do curso de Ciência da Computação do IFCE - Campus Iguatu

## Como rodar o projeto:
Este projeto usa a versão `3.12.*` do Python.

O projeto usa o [Poetry](https://python-poetry.org/) para gerenciar as dependências. Para instalar as dependências, execute:
```bash
poetry install
```

Para rodar os comando do projeto, você precisa ativar o ambiente virtual do Poetry com o comando:
```bash
poetry shell
```

### Sobre os comandos:
Os comandos para executar funções do projeto são feitos com o [taskipy](https://github.com/taskipy/taskipy):
```bash
task --list # Lista os comandos disponíveis
task main   # Roda as simulações e printa em tabela
task gui    # Executa um GUI para visualizar as simulações
task xlsx   # Executas as simulaçoes e salva em um arquivo xlsx
```
