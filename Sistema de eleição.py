import pickle
chapas = {}

#Criando as chapas
def CriarChapa(chapas):
    while True:
        print("\n\nAdicionando chapa!")
        nome_chapa = str(input("Digite o nome da chapa que deseja cadastrar: "))
        if nome_chapa in chapas.keys():
            print("Essa chapa já foi cadastrada!\n Caso deseja alterar o nome dos candidatos ou excluir tal chapa, selecione a opção correta no menu!")
            break
        chapas[nome_chapa] = []
        chapas[nome_chapa].append(str(input(f"Digite o nome do Reitor da chapa {nome_chapa}: ")))
        chapas[nome_chapa].append((input(f"Digite o nome do Vice-Reitor da chapa {nome_chapa}: ")))
        print("CHAPA CADASTRADA!")
        break

#Alterar nome dos candidatos de alguma chapa
def AlterarNome(chapas):
    while True:
        print("\n\nAlterando nome dos candidatos!")
        nome_chapa = str(input("Digite o nome da chapa que deseja alterar o nome dos candidatos: "))
        if nome_chapa not in chapas.keys():
            print("Essa chapa não foi cadastrada!\n Caso deseja adicionar uma nova chapa, selecione a opção correta no menu!")
            break
        chapas[nome_chapa].clear()
        chapas[nome_chapa].append(str(input(f"Digite o nome do Reitor da chapa {nome_chapa}: ")))
        chapas[nome_chapa].append((input(f"Digite o nome do Vice-Reitor da chapa {nome_chapa}: ")))
        print("CHAPA CORRIGIDA!")
        break

#Excluir chapa adicionada
def ExcluirChapa(chapas):
    while True:
        print("\n\nExcluindo alguma chapa!")
        nome_chapa = str(input("Digite o nome da chapa que deseja excluir: "))
        if nome_chapa not in chapas.keys():
            print("Não tem como excluir uma chapa não cadastrada!\n Caso deseja adicionar uma nova chapa, selecione a opção correta no menu!")
            break
        chapas.pop(nome_chapa)
        print("CHAPA EXCLUÍDA!")
        break
print("- Sistema de Controle de Votos -")
while True:
    menu = str(input("""
Digite um número do menu a seguir:
1) Adicionar chapa
2) Consultar chapas
3) Alterar o nome dos candidatos de alguma chapa
4) Exclusão de alguma chapa
5) Finalizar o cadastro de chapas
"""))

    if menu == "1":
        CriarChapa(chapas)
    elif menu == "2":
        print("\nChapas cadastradas:\n", chapas)
    elif menu == "3":
        AlterarNome(chapas)
    elif menu == "4":
        ExcluirChapa(chapas)
    elif menu == "5":
        break

#Cadastro dos números totais de possíveis votantes
print("Ok, chapas cadastradas!!\nA partir de agora não poderão mais ser alteradas!\n")
print("\nAgora é preciso cadastrar o número total de possíveis votantes!\nPor favor, digite a quantidade de")
discentes = int(input("Discentes: "))
docentes = int(input("Docentes: "))
tecnico = int(input("Servidores técnicos: "))
print("Tudo cadastrado!!")

#Início dos votos
#Junção de todas as urnas do dia para adicionar no arquivo
todas_urnas = []


print("\n\n\n\n - COMEÇANDO A VOTAÇÃO! - ")
print("Chapas concorrentes: ")
qtd_chapas = 0 #Contando quantidade de chapas cadastradas
for c in chapas.keys():
    qtd_chapas += 1
    print(f"{qtd_chapas}) {c}")

#Cadastro do voto
def votacao(num_urna):
    while True:
        votante = int(input("""Digite o número de sua categoria:
0) Número pertencente ao mesário, caso deseje mudar de urna. (Se estiver na urna 4 e for selecionado, pulará para o próximo dia!)
1) Discente;
2) Docente;
3) Servidor técnico;
"""))
        if votante == 0:
            todas_urnas.append(num_urna)
            break
        elif votante == 1 or votante == 2 or votante == 3:
            voto = int(input("\nCaso deseje votar branco/ nulo, digite qualquer número de uma chapa inexistente!\nDigite o número do seu voto: "))
            num_urna[votante].append(voto)
        else:
            print("\n\nPor favor, digite um número que esteja no menu.")
        

def chamada_votos(dia):
    #Dicionário das urnas de cada módulo, as quais os valores
    #são os números das chapas selecionadas como voto.
    urna1 = {1: [], 2: [], 3: []} #1 = Discente; 2 = Docente; 3 = Servidor técnico
    urna2 = {1: [], 2: [], 3: []}
    urna3 = {1: [], 2: [], 3: []}
    urna4 = {1: [], 2: [], 3: []}
    #Primeira urna de votação
    print("Votação MÓDULO 1(URNA 1), candidatos com nomes iniciados com as letras A, B, C, D.")
    votacao(urna1)

    #Segunda urna de votação
    print("\n\n\nVotação MÓDULO 3(URNA 2), candidatos com nomes iniciados com as letras E, F, G, H, I, J.")
    votacao(urna2)

    #Terceiro urna de votação
    print("\n\n\nVotação MÓDULO 5(URNA 3), candidatos com nomes iniciados com as letras K, L, M, N, O.")
    votacao(urna3)

    #Quarta urna de votação
    print("\n\n\nVotação MÓDULO 7(URNA 4), candidatos com nomes iniciados com as letras P, Q, R, S, T, U, V, W, X, Y, Z.")
    votacao(urna4)

    #Criando e adicionando valores aos arquivos
    dia = open(f"{dia}.bin", "wb")
    pickle.dump(todas_urnas, dia)
    todas_urnas.clear()
    dia.close()


#Propondo os dias de votação
print("\n\n\nPRIMEIRO DIA DE ELEIÇÃO DO ANO DE 2023!")
chamada_votos("dia1")

print("\n\n\nSEGUNDO DIA DE ELEIÇÃO DO ANO DE 2023!")
chamada_votos("dia2")

print("\n\n\nTERCEIRO E ÚLTIMO DIA DE ELEIÇÃO DO ANO DE 2023!")
chamada_votos("dia3")

#Relatório
#Função para chamar relatório de votantes por dia/ categoria
def relatorio(arquivo):
    votantes_total = 0
    cat1 = 0
    cat2 = 0
    cat3 = 0

    for valores in arquivo:
        for c, v in valores.items():
            votantes_total += len(v)
            if c == 1:
                cat1 += len(v)
            elif c == 2:
                cat2 += len(v)
            elif c == 3:
                cat3 += len(v)
    return votantes_total, cat1, cat2, cat3

#Votos totais em cada urna
def num_urna(qual_dia, qual_urna):
    total = 0
    for urna in qual_dia[qual_urna].values():
        total += len(urna)
    return total

v_dia1, v_dia2, v_dia3 = 0, 0, 0 # Votantes total por dia
v1_cat1, v1_cat2, v1_cat3 = 0, 0, 0 # Votantes total de cada categoria do dia 1
v2_cat1, v2_cat2, v2_cat3 = 0, 0, 0 # Votantes total de cada categoria do dia 2
v3_cat1, v3_cat2, v3_cat3 = 0, 0, 0 # Votantes total de cada categoria do dia 3

#Votos nulos/ brancos
nulo_dia1, nulo_dia2, nulo_dia3 = 0, 0, 0
nulo_dia1_cat1, nulo_dia1_cat2, nulo_dia1_cat3 = 0, 0, 0
nulo_dia2_cat1, nulo_dia2_cat2, nulo_dia2_cat3 = 0, 0, 0
nulo_dia3_cat1, nulo_dia3_cat2, nulo_dia3_cat3 = 0, 0, 0
total_urna1, total_urna2, total_urna3, total_urna4 = 0, 0, 0, 0 #Votos totais em cada urna

#Nome de cada chapa
nome_chapas = []
for c in chapas.keys():
    nome_chapas.append(str(c))

# Abrindo arquivos
votantes_dia1 = pickle.load(open("dia1.bin", "rb"))
votantes_dia2 = pickle.load(open("dia2.bin", "rb"))
votantes_dia3 = pickle.load(open("dia3.bin", "rb"))

#Chamando relatório de votantes por dia/ categoria
v_dia1, v1_cat1, v1_cat2, v1_cat3 = relatorio(votantes_dia1)
v_dia2, v2_cat1, v2_cat2, v2_cat3 = relatorio(votantes_dia2)
v_dia3, v3_cat1, v3_cat2, v3_cat3 = relatorio(votantes_dia3)

# Chamando função de votos totais em cada urna:
total_urna1 = num_urna(votantes_dia1, 0) + num_urna(votantes_dia2, 0) + num_urna(votantes_dia3, 0)
total_urna2 = num_urna(votantes_dia1, 1) + num_urna(votantes_dia2, 1) + num_urna(votantes_dia3, 1)
total_urna3 = num_urna(votantes_dia1, 2) + num_urna(votantes_dia2, 2) + num_urna(votantes_dia3, 2)
total_urna4 = num_urna(votantes_dia1, 3) + num_urna(votantes_dia2, 3) + num_urna(votantes_dia3, 3)

#Votos nulos dia 1/ votos de cada categoria nas chapas
votos_chapas = {}
for i in range(qtd_chapas):
    #NVD, NVSD, NVST respectivamente
    votos_chapas[i] = [0, 0, 0] #Discente, docente e servidor técnico

for valores in votantes_dia1:
    for c, v in valores.items():
        for voto in v:
            #Contando a quantidade de votos em cada chapa de acordo com a categoria do votante
            for i in range(qtd_chapas):
                if voto == i+1:
                    for k, p in votos_chapas.items():
                        if k == i:
                            p[c-1] += 1

            #Verificando se é um voto nulo/branco
            if voto > qtd_chapas or voto < qtd_chapas:
                nulo_dia1 += 1
                if c == 1:
                    nulo_dia1_cat1 += 1
                elif c == 2:
                    nulo_dia1_cat2 += 1
                elif c == 3:
                    nulo_dia1_cat3 += 1

#Votos nulos dia 2/ votos de cada categoria nas chapas
for valores in votantes_dia2:
    for c, v in valores.items():
        for voto in v:
            #Contando a quantidade de votos em cada chapa de acordo com a categoria do votante
            for i in range(qtd_chapas):
                if voto == i+1:
                    for k, p in votos_chapas.items():
                        if k == i:
                            p[c-1] += 1

            #Verificando se é um voto nulo ou branco
            if voto > qtd_chapas or voto < qtd_chapas:
                nulo_dia2 += 1
                if c == 1:
                    nulo_dia2_cat1 += 1
                elif c == 2:
                    nulo_dia2_cat2 += 1
                elif c == 3:
                    nulo_dia2_cat3 += 1

#Votos nulos dia 3/ votos de cada categoria nas chapas
for valores in votantes_dia3:
    for c, v in valores.items():
        for voto in v:
            #Contando a quantidade de votos em cada chapa de acordo com a categoria do votante
            for i in range(qtd_chapas):
                if voto == i+1:
                    for k, p in votos_chapas.items():
                        if k == i:
                            p[c-1] += 1

            #Verificando se é um voto nulo ou branco
            if voto > qtd_chapas or voto < qtd_chapas:
                nulo_dia3 += 1
                if c == 1:
                    nulo_dia3_cat1 += 1
                elif c == 2:
                    nulo_dia3_cat2 += 1
                elif c == 3:
                    nulo_dia3_cat3 += 1

print("\n\n\n- Relatório- ")
print(f"Votos totais dos dias 1, 2 e 3, respectivamente: {v_dia1}, {v_dia2}, {v_dia3}")
print(f"Votos totais do dia 1 das categorias discente, docente e servidor técnico, respectivamente: {v1_cat1}, {v1_cat2}, {v1_cat3}")
print(f"Votos totais do dia 2 das categorias discente, docente e servidor técnico, respectivamente: {v2_cat1}, {v2_cat2}, {v2_cat3}")
print(f"Votos totais do dia 3 das categorias discente, docente e servidor técnico, respectivamente: {v3_cat1}, {v3_cat2}, {v3_cat3}")

print("\nNúmero total de votos nulos/ brancos:", nulo_dia1 + nulo_dia2 + nulo_dia3)
print(f"Número total de votos nulos nos dias 1, 2 e 3, respectivamente: {nulo_dia1}, {nulo_dia2}, {nulo_dia3}")
print(f"Votos brancos/nulos totais do dia 1 das categorias discente, docente e servidor técnico, respectivamente: {nulo_dia1_cat1}, {nulo_dia1_cat2}, {nulo_dia1_cat3}")
print(f"Votos brancos/nulos totais do dia 2 das categorias discente, docente e servidor técnico, respectivamente: {nulo_dia2_cat1}, {nulo_dia2_cat2}, {nulo_dia2_cat3}")
print(f"Votos brancos/nulos totais do dia 3 das categorias discente, docente e servidor técnico, respectivamente: {nulo_dia3_cat1}, {nulo_dia3_cat2}, {nulo_dia3_cat3}")

print(f"\nVotos totais computados, respectivamente, nas urnas 1, 2, 3 e 4: {total_urna1}, {total_urna2}, {total_urna3}, {total_urna4}.\n")

for i in range(qtd_chapas):
    print(f"A chapa -{nome_chapas[i]}- teve um total de votos das categorias discente, docente e servidor técnico, respectivamente, de: {votos_chapas[i]}")

#Para facilitar na a equação da obtenção da porcentagem
total_votos_categoria1 = v1_cat1 + v2_cat1 + v3_cat1
total_votos_categoria2 = v1_cat2 + v2_cat2 + v3_cat2
total_votos_categoria3 = v1_cat3 + v2_cat3 + v3_cat3

print(f"\nA procentagem de ausência de discentes, docentes e servidores técnicos foi, respectivamente, de: {100-(total_votos_categoria1 * 100/discentes)}%, {100-(total_votos_categoria2 * 100/docentes)}%, {100-(total_votos_categoria3 * 100/tecnico)}%\n")

#Escore
# Lembrando: NVD 0, NVSD 1, NVST 2 respectivamente
# NTD = discentes, NTSD = docentes, NTST = tecnico
maior_escore = -1000000000000000 #Para atribuir o primeiro escore a esta variável
qual_chapa = 0
NV = total_votos_categoria1 + total_votos_categoria2 + total_votos_categoria3
escore_chapas = []
for i in range(qtd_chapas):
    e = (votos_chapas[i][1] * 1 / docentes * 3) + (votos_chapas[i][2] * 1 / tecnico * 3) + (votos_chapas[i][0] * 1 / discentes * 3) * NV
    escore_chapas.append(e)
    if maior_escore < e:
        maior_escore = e
        qual_chapa = nome_chapas[i]
    print(f"O escore da chapa -{nome_chapas[i]}- foi de: {e}")

for c, v in chapas.items():
    if c == qual_chapa:
        print(f"\n\nOs candidatos {v} ganharam esta eleição!!\nSendo a chapa -{c}- a vencedora!")