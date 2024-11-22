# Ouvidoria Abella Fase 2

Sistema de Ouvidoria com fins didaticos para o Projeto Competencia 2 da cadeira de Programação estruturada  em Python

## Colaboradores

Pedro Italo Gomes Ferreira Pereira - 2423080036
Andrey Savinir Nascimento Araújo - 2423081007
Iann Maia Lima - 2423081004
João Vitor da Silva Cabral - 2423081006
Luiz Fernando Lopes dos Anjos - 2423080011
Pedro Leonardo costa de Assis filho -2423080055
Luís Felipe Gomes Morais Pinheiro -2423080046

## Funcionalidades
O sistema oferece as seguintes opções de menu:

#### Listagem das Manifestações
Exibe uma lista de todas as manifestações registradas no sistema.

#### Listagem de Manifestações por Tipo
Permite ao usuário selecionar um tipo específico de manifestação (reclamação, elogio ou sugestão) para exibir somente as manifestações desse tipo.

#### Criar uma Nova Manifestação
O usuário pode registrar uma nova manifestação, fornecendo todas as informações necessárias, como tipo de manifestação, descrição, etc.

#### Exibir Quantidade de Manifestações
Exibe o número total de manifestações registradas no sistema.

#### Pesquisar uma Manifestação por Código
Permite ao usuário buscar uma manifestação utilizando um código único, exibindo as informações detalhadas da manifestação correspondente.

#### Excluir uma Manifestação pelo Código
Permite ao usuário excluir uma manifestação registrada, fornecendo o código da manifestação a ser excluída.

#### Sair do Sistema
Finaliza a execução do sistema.

## Estrutura do Sistema
O sistema foi desenvolvido para ser simples e eficiente, oferecendo uma interface de menu fácil de usar. Ele armazena as manifestações em um banco de dados (que pode ser um arquivo local ou um banco de dados relacional, dependendo da implementação). As manifestações são armazenadas com os seguintes campos:

#### Código: 
identificador único da manifestação.
#### Descrição: 
conteúdo da manifestação.
#### Categoria: 
tipo da manifestação (reclamação, elogio, sugestão).
#### Autor:
nome de quem está fazendo a manifestação.

## Tecnologias Utilizadas
O sistema pode ser implementado em:

#### Backend:
Python
#### Banco de Dados:
MySQL

## Como Executar
Clone ou baixe o repositório para sua máquina local.
Instale as dependências necessárias (caso haja algum requisito específico).
Execute o arquivo principal (exemplo: main.py para uma implementação em Python).
O sistema irá exibir o menu com as opções descritas acima.
Considerações Finais
Este sistema visa facilitar o gerenciamento de manifestações em qualquer organização ou instituição, fornecendo uma maneira organizada de registrar e visualizar reclamações, elogios e sugestões dos usuários. Ele pode ser expandido e adaptado conforme as necessidades da empresa ou do projeto.
