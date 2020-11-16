import os
os.system('cls')

def salvar_itens(lista):
    arquivo = open("ItensRPG.txt", "w", encoding="utf-8")

    for item in lista:
        arquivo.write("{},{},{},{}\n".format(item['Nome do Item'], item['Preço'], item['Página(DMG/MM)'], item['Raridade']))

    arquivo.close()

def carregar_itens():
    lista = []
    arquivo = open("ItensRPG.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        coluna = linha.strip().split(",")

        item = {
            "Nome do Item": coluna[0],
            "Preço": coluna[1],
            "Página(DMG/MM)": coluna[2],
            "Raridade": coluna[3]
        }
        lista.append(item)
        arquivo.close()
    return lista

def existe_item(lista, nome_item):
    if len(lista) > 0:
        for item in lista:
            if item['Nome do Item'] == nome_item:
                return True
    return False

def adicionar(lista):
    while True:
        nome_item = input("Digite o nome do Item: ")
        if not existe_item(lista, nome_item):
            break
        else:
            print("Item já adicionado.")
            print("Tente outro Item.")

    item = {
        "Nome do Item": nome_item,
        "Preço": float(input("Digite o preço: ")),
        "Página(DMG/MM)": float(input("Digite a página: ")),
        "Raridade": input("Digite o nível de raridade: ")
    }
    lista.append(item)
    print("O item {} foi adicionado com sucesso!\n".format(item['Nome do Item']))

def alterar(lista):
    print(" == Alterar Item ==")
    if len(lista) > 0:
        nome_item = input("Digite o nome do item a ser alterado:")
        if existe_item(lista, nome_item):
            print("O item foi encontrado, segue abaixo informações: ")
            for item in (lista):
                if item['Nome do Item'] == nome_item:
                    print("Nome do Item: {}".format(item['Nome do Item']))
                    print("Preço: {}".format(item['Preço']))
                    print("Página(DMG/MM): {}".format(item['Página(DMG/MM)']))
                    print("Raridade: {}".format(item['Raridade']))
                    print(32*"=")

                    item['Preço'] = float(input("Digite o novo preço: "))
                    item['Página(DMG/MM)'] = float(input("Digite o novo número da página:"))
                    item['Raridade'] = input("Digite a nova raridade:")
                    print("Os dados do item {} foram alterados com sucesso!"
                        .format(item['Nome do Item']))
                    break
        else:
            print("Não existe item com o nome: {}".format(nome_item))
    else:
        print("Não existe itens no sistema.")

def excluir(lista):
    print(" == Excluir Item ==")
    if len(lista) > 0:
        nome_item = input("Digite o nome do item a ser excluído:")
        if existe_item(lista, nome_item):
            print("O item foi encontrado, segue abaixo informações: ")
            for i, item in enumerate(lista):
                if item['Nome do Item'] == nome_item:
                    print("Nome do Item: {}".format(item['Nome do Item']))
                    print("Preço: {}".format(item['Preço']))
                    print("Página(DMG/MM): {}".format(item['Página(DMG/MM)']))
                    print("Raridade: {}".format(item['Raridade']))
                    print(32*"=")
                    del lista[i]
                    print("O item foi apagado com sucesso.")
                    break
        else:
            print("Não existe item com o nome: {}".format(nome_item))
    else:
        print("Não existe itens no sistema.\n")

def buscar(lista):
    print(" == Buscar Item ==")
    if len(lista) > 0:
        nome_item = input("Digite o nome do item a ser pesquisado:")
        if existe_item(lista, nome_item):
            print("O item foi encontrado, segue abaixo informações: ")
            for item in (lista):
                if item['Nome do Item'] == nome_item:
                    print("Nome do Item: {}".format(item['Nome do Item']))
                    print("Preço: {}".format(item['Preço']))
                    print("Página(DMG/MM): {}".format(item['Página(DMG/MM)']))
                    print("Raridade: {}".format(item['Raridade']))
                    print(32*"=")
                    break
        else:
            print("Não existe item com o nome: {}".format(nome_item))
    else:
        print("Não existe itens no sistema.")

def listar(lista):
    print(" == Listar Itens ==")
    if len(lista) > 0:
        for i, item in enumerate(lista):
            print("Item{}:".format(i+1))
            print("\tNome do Item: {}".format(item['Nome do Item']))
            print("\tPreço: {}".format(item['Preço']))
            print("\tPágina(DMG/MM): {}".format(item['Página(DMG/MM)']))
            print("\tRaridade: {}".format(item['Raridade']))
            print(32*"=")
        print("Quantidade de itens: {}\n".format((len(lista)-1)))
    else:
        print("Não existe itens no sistema.")

def principal():

    lista = carregar_itens()

    while True:
        print("===Lista de Itens c/ Preços===")
        print("=== Dungeon Master’s Guide ===")
        print(" 1 - Adicionar Item")
        print(" 2 - Alterar Item")
        print(" 3 - Excluir Itens")
        print(" 4 - Buscar Itens")
        print(" 5 - Listar Itens")
        print(" 6 - Ordenar")
        print(" 7 - Sair")
        
        opção = int(input(">"))

        if opção == 1:
            adicionar(lista)
            salvar_itens(lista)
        elif opção == 2:
            alterar(lista)
            salvar_itens(lista)
        elif opção == 3:
            excluir(lista)
            salvar_itens(lista)
        elif opção == 4:
            buscar(lista)
        elif opção == 5:
            listar(lista)
        elif opção == 6:
            def sort(dados, index, escolhe_ordem):
                if escolhe_ordem == 1:   #CRESCENTE
                    for i in range(len(dados)-1):
                        min = i
                        for j in range(i, len(dados)):
                            if dados.get(j)[index] < dados.get(min)[index]:
                                min = j
                        if dados.get(i)[index] > dados.get(min)[index]:
                            dados[i], dados[min] = dados[min], dados[i]

                elif escolhe_ordem == 2:  #DECRESCENTE
                    for i in range(len(dados)-1):
                        max = i
                        for j in range(i, len(dados)):
                            if dados.get(j)[index] > dados.get(max)[index]:
                                max = j
                        if dados.get(i)[index] < dados.get(max)[index]:
                            dados[i], dados[max] = dados[max], dados[i]

            def converte_float(dados, index):
                for i in dados:
                    dados.get(i)[index] = float(dados.get(i)[index])

            print('lendo arquivo...')
            dados = open('ItensRPG.txt', encoding="utf-8")
            linhas = dados.readlines()

            dados = {}

            contador = 0
            for linha in linhas:
                contador = contador+1
            print('o numero de itens é',contador)

            l = int(input("Digite quantos itens deseja:"))

            for i in range(l-1):
                dados[i] = linhas[i+1].replace('\n','').split(',')
            
            print('Escolha qual coluna deseja Ordenar:')
            print(36*'*')
            print('Digite 1 para Ordenar pelo Preço')
            print(' ')
            print('       2 para Ordenar pelo nº da Página.')
            print(36*'*')
            print(' ')
            escolhe_coluna = int(input('>'))

            print(' ')
            print(36*'*')
            print('Digite 1 para Ordenação Crescente')
            print(' ')
            print('       2 para Ordenação Decrescente.')
            print(36*'*')
            print(' ')
            escolhe_ordem = int(input('>'))

            converte_float(dados,escolhe_coluna)

            print('Ordenando...')

            sort(dados, escolhe_coluna, escolhe_ordem)

            saida = open('saida_ItensRPG.txt', 'w', encoding="utf-8")

            saida.write(linhas[0])

            for k, v in dados.items():
                saida.write(str(v).replace('[','').replace(']','') + "\n")

            saida.close()
            print('Programa Finalizado.')        
        elif opção == 7:
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

principal()