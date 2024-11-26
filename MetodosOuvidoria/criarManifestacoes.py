def criarManifestacoes(conexao):
    print('Criar Manifestação')
    nome = input('Digite seu nome: ')

    while True:
        categoria = int(input('\n1) Reclamaçoes''\n2) Sugestoes''\n3) Elogios\n'
        '\nDigite a opçao com o tipo de manifestaçao : '))
        if categoria == 1:
            categoria = 'Reclamaçao'
            break
        elif categoria == 2:
            categoria = 'Sugestao'
            break
        elif categoria == 3:
            categoria = 'Elogio'
            break
        else:
            print('Opçao invalida! Tente novamente.')

    manifestacao = input('Digite sua manifestaçao: ')

    consultaInserir = 'insert into manifestacoes (nome,tipoManifestacao,manifestacao) values (%s,%s,%s)'
    valores = [nome, categoria, manifestacao]

    insertNoBancoDados(conexao,consultaInserir,valores)

    print('Manifestacao inserida com sucesso!')
