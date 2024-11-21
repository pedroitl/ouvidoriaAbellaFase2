def pesquisarManifestacoes(conexao):
    codigopesquisar = int(input("digite o codigo: "))
    consultapesquisar = "select * from manifestacoes where codigo = %s"
    valores = [codigopesquisar]
    manifestacoes = listarBancoDados(conexao, consultapesquisar, valores)
    if len(manifestacoes) > 0:
        print(manifestacoes[0][1], "-", manifestacoes[0][2], "-", manifestacoes[0][3])
    else:
        print("Atualmente nao temos manifestacoes nessa posicao!")