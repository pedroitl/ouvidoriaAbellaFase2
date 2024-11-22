def listarManifestacoes(conexao):

    lista = listarBancoDados(conexao, "select * from manifestacoes")

<<<<<<< HEAD:listarmanifestacoesportipo.py
    if len(lista) > 0:
            print("lista das manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("nao existem manifestacoes a serem exibidas!")
=======
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
>>>>>>> d65135ad0356eb30c4c6307fec50be4558f2a935:MetodosOuvidoria/listarManifestacoesPorTipo.py
