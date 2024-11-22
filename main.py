from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', 'root', 'ouvidoria_projeto_abella')

def listarManifestacoes(conexao):
    lista = listarBancoDados(conexao, "select * from manifestacoes")

    if len(lista) > 0:
            print("Lista de manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("Nao existem manifestacoes cadastradas!")

def listarManifestacoesPorTipo(conexao):

    categoria = input("Digite o tipo de manifestacao a ser cadastrada: ")
    consultaListarPorTipo = "select * from manifestacoes where tipo = %s"
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
    nome = input('Digite seu nome: ')

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

    manifestacao = input('Digite sua manifestaçao: ')

    consultaInserir = 'insert into manifestacoes (nome,tipoManifestacao,manifestacao) values (%s,%s,%s)'
    valores = [nome, categoria, manifestacao]

    insertNoBancoDados(conexao,consultaInserir,valores)

    print('Filme inserido com sucesso!')

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

def excluirManifestacao(conexao):
    codigoRemover = int(input('Digite o codigo da manifestaçao que deseja remover: '))
    consultaRemover = 'delete from manifestaçoes where cogigo = %s'
    valores = [codigoRemover]
    linhasAfetadas = excluirBancoDados(conexao, consultaRemover, valores)

    if linhasAfetadas > 0:
        print('manifestação removida com sucesso')

    else:
        print('Não existe manifestações para o codigo informado ')

