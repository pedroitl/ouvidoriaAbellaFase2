def listarManifestacoes(conexao):

    lista = listarBancoDados(conexao, "select * from manifestacoes")

    if len(lista) > 0:
            print("lista das manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("nao existem manifestacoes a serem exibidas!")
