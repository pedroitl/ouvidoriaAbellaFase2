def listarManifestacoes(conexao):

    lista = listarBancoDados(conexao, "select * from manifestacoes")

    if len(lista) > 0:
            print("Lista de manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("Nao existem manifestacoes cadastradas!")