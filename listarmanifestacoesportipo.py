def listarManifestacoesPorTipo(conexao):

    tipomanifestacao = input("digite o tipo de manifestacao : ")
    consultalistagemtipo = "select * from manifestacoes where tipo = %s"
    tipo = [tipomanifestacao]
    lista = listarBancoDados(conexao, consultalistagemtipo, tipo)
    if len(lista) > 0:
        print("essas sao todas manifestacoes que temos nesse tipo:")
        for item in lista:
            print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
        print("nao temos nenhuma manifestacao nesse tipo!")