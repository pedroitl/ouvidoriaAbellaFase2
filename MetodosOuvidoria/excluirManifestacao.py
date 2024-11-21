def excluirManifestacao(conexao):

    codigoremover = int(input('Digite o codigo para remover: ' ))
    consultaRemover = 'delete from manifestaçoes where cogigo = %s'
    valores = [codigoremover]
    linhasAfetadas = excluirBancoDados(conexao,calsutaRemover,valores)

    if linhasAfetadas > 0:
        print('manifestação removida com sucesso' )

    else:
        print('Não existe manifestações para o codigo informado ')
