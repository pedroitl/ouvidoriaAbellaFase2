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