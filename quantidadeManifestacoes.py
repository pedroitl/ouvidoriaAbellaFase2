def quantidadeManifestacoes(conexao):
    consultarQuantidade = "select count(*) from manifestacoes"
    listagem = listarBancoDados(conexao,consultarQuantidade)
    quantidade = listagem[0][0]
    print("Atualmente temos", quantidade, "Manifestaçao(s)")