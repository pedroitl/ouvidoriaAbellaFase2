<<<<<<< HEAD
def listarManifestacoesPorTipo(conexao):
=======
def listarManifestacoes(conexao):

    lista = listarBancoDados(conexao, "select * from manifestacoes")

    if len(lista) > 0:
            print("lista das manifestacoes:")
            for item in lista:
                print(item[0], "-", item[1], "-", item[2], "-", item[3])
    else:
            print("nao existem manifestacoes a serem exibidas!")
>>>>>>> 8e4aa866582898326c95e88a08bf5269a953fe51
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
<<<<<<< HEAD

=======
>>>>>>> 8e4aa866582898326c95e88a08bf5269a953fe51
