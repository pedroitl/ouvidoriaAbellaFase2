def excluirManifestacao(conexao):
    codigoremover = int(input('Digite o codigo para remover' ))

    consultarRemover = 'delete from manifestaçoes where cogigo = %s'
    valores = [codigoremover]
    linhasafetadas = excluirBancoDados(conexao,calsutaRemover,valores)

    if linhasafetadas > 0:
        print('manifestação removida com sucesso' )

    else:
        print('Não existe manifestações para o codigo informado ')
