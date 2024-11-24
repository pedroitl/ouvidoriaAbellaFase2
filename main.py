from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '12345', 'ouvidoria_projeto_abella')

def listarManifestacoes(conexao):
    lista = listarBancoDados(conexao, "select * from manifestacoes")

    if len(lista) > 0:
            print("Lista de manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("Nao existem manifestacoes cadastradas!")

def listarManifestacoesPorTipo(conexao):

    categoria = input("Digite o tipo de manifestacao a ser pesquisada: ")
    consultaListarPorTipo = "select * from manifestacoes where categoria = %s"
    tipo = [categoria]

    lista = listarBancoDados(conexao, consultaListarPorTipo, tipo)

    if len(lista) > 0:
        print("Essas sao todas as manifestacoes que temos nesse tipo:")
        for item in lista:
            print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
        print("Nao temos nenhuma manifestacao nesse tipo!")

def criarManifestacoes(conexao):
    print('Criar Manifestação')
    autor = input('Digite seu nome: ')

    while True:
        categoria = int(input('\n1) Reclamaçoes''\n2) Sugestoes''\n3) Elogios\n'
        '\nDigite a opçao com o tipo de manifestaçao : '))
        if categoria == 1:
            categoria = 'Reclamaçao'
            break
        elif categoria == 2:
            categoria = 'Sugestao'
            break
        elif categoria == 3:
            categoria = 'Elogio'
            break
        else:
            print('Opçao invalida! Tente novamente.')

    descricao = input('Digite sua manifestaçao: ')

    consultaInserir = 'insert into manifestacoes (descricao, categoria, autor) values (%s,%s,%s)'
    valores = [descricao, categoria, autor]

    insertNoBancoDados(conexao,consultaInserir,valores)

    print('Manifestacao inserida com sucesso!')

def quantidadeManifestacoes(conexao):
    consultarQuantidade = "select count(*) from manifestacoes"
    listagem = listarBancoDados(conexao,consultarQuantidade)
    quantidade = listagem[0][0]
    print("Atualmente temos um total de", quantidade, "manifestaçao(s)")

def pesquisarManifestacoes(conexao):
    codigoPesquisar = int(input("digite o codigo: "))
    consultaPesquisar = "select * from manifestacoes where codigo = %s"
    valores = [codigoPesquisar]
    manifestacoes = listarBancoDados(conexao, consultaPesquisar, valores)
    if len(manifestacoes) > 0:
        print(manifestacoes[0][1], "-", manifestacoes[0][2], "-", manifestacoes[0][3])
    else:
        print("Atualmente não temos manifestaçoes nessa posiçao!")

def excluirManifestacoes(conexao):
    codigoRemover = int(input('Digite o codigo da manifestaçao que deseja remover: '))
    consultaRemover = 'delete from manifestacoes where codigo = %s'
    valores = [codigoRemover]
    linhasAfetadas = excluirBancoDados(conexao, consultaRemover, valores)

    if linhasAfetadas > 0:
        print('Manifestação removida com sucesso')

    else:
        print('Não existe manifestações para o codigo informado ')

