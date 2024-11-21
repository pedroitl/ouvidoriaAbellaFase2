from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', 'root', 'ouvidoria_projeto_abella')

#listar normal

def listarManifestacoesPorTipo(conexao):

    tipomanifestacao = input("Digite o tipo de manifestacao a ser cadastrada: ")
    consultalistagemtipo = "select * from manifestacoes where tipo = %s"
    tipo = [tipomanifestacao]
    lista = listarBancoDados(conexao, consultalistagemtipo, tipo)
    if len(lista) > 0:
        print("Essas sao todas manifestacoes que temos nesse tipo:")
        for item in lista:
            print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
        print("Nao temos nenhuma manifestacao nesse tipo!")

#criar

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

