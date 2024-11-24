from main import *

conexao = criarConexao('127.0.0.1', 'root', 'root', 'ouvidoria_projeto_abella')

opcao = 1

while opcao != 7:
    print('\n=====SISTEMA DE OUVIDORIA=====\n'
        '\n1) Lista de Manifestaçoes \n'
          '2) Listar manifestaçoes por tipo\n'
          '3) Criar uma nova manifestação \n'
          '4) Exibir quantidade de manifestaçoes  \n'
          '5) Pesquisar uma manifestaçao por codigo \n'
          '6) Excluir uma manifestação por codigo \n'
          '7) Sair')

    opcao = int(input('\nDigite a opcao a ser realizada: '))

    if opcao == 1:
        listarManifestacoes(conexao)
    elif opcao == 2:
        listarManifestacoesPorTipo(conexao)
    elif opcao == 3:
        criarManifestacoes(conexao)
    elif opcao == 4:
        quantidadeManifestacoes(conexao)
    elif opcao == 5:
        pesquisarManifestacoes(conexao)
    elif opcao == 6:
        excluirManifestacoes(conexao)
    elif opcao != 7:
        print('Opção Inválida!')
    else:
        print('...')

encerrarConexao(conexao)
print('Sistema finalizado! Obrigado por utilizar nossos serviços.')

