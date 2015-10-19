def mandatos(x, y): 
    mascara_ordem=list(y)
    p = list(y)
    lostt3=[]
    list2 = []
    e = 2
    while e <=x:
        for g in range(0, len(y)):                                                        
            p.append(p[g]/e) 
        e = e+1
    last = sorted(range(len(p)), key=lambda i:p[i])
    mascara_ordem = sorted(range(len(mascara_ordem)), key=lambda i:mascara_ordem[i])
    lostt2 = sorted(range(len(p)), key=lambda i:p[i])
    mascara_ordem = mascara_ordem[::-1]
    lostt2 = lostt2[::-1]
    last2 = last[-x:]
    last2 = last2[::-1]                                                                     
    last3=[]
    last4=[]
    indices = [i for i, k in enumerate(y1) if k == sorted(p)[x-1]]
    del p
    for i in last2:
        if i >= len(y):
            i = i%len(y)
            last3.append(i)
        else:
            last3.append(i)
    del last2
    for i in lostt2:
        if i >= len(y):
            i = i%len(y)
            lostt3.append(i)
        else:
            lostt3.append(i)
    del lostt2
    for i in indices:
        list2.append(lostt3[i])
    minimum = sorted(list2,key=lambda x: mascara_ordem[::-1].index(x))
    del mascara_ordem
    del list2
    for i in range(0, len(minimum)-1):
        last3[indices[i]] = minimum[i]  
    for f in range(0,len(y)):
        last4.append(last3.count(f))
    del last3
    return tuple(last4)
def assembleia(votacoes):
    deputados = (16, 3, 19, 3, 4, 9, 3, 9, 4, 10, 47, 2, 39, 9, 18, 6, 5, 9, 5, 6, 2, 2)        #Deputados dos circulos elitorais na ordem da Tabela 1
    soma_man = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    k = 0
    for votos in votacoes:
        man_dev = mandatos(deputados[k], votos)                                                 #Mandatos do circulo elitoral a ser iterado
        agrup = zip (man_dev, soma_man)                                                         
        soma_man = tuple(sum(x) for x in agrup)                                                 #Soma dos mandados dos circulos elitorais
        k = k + 1
    return soma_man

def max_mandatos(votacoes):
    partido = ('PDR\tPartido Democratico Republicano',\
               'PCP-PEV\tCDU - Coligacao Democratica Unitaria',\
               'PPD/PSD-CDS/PP\tPortugal a Frente',\
               'MPT\tPartido da Terra',\
               'L/TDA\tLIVRE7Tempo de Avancar',\
               'PAN\tPessoas-Animais-Natureza',\
               'PTP-MAS\tAgir',\
               'JPP\tJuntos Pelo Povo',\
               'PNR\tPartido Nacional Renovador',\
               'PPM\tPartido Popular Monarquico',\
               'NC\tNos, Cidadaos!',\
               'PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses',\
               'PS\tPartido Socialista',\
               'B.E.\tBloco de Esquerda',\
               'PURP\tPartido Unido dos Reformados e Pensionistas')
    assemb = assembleia(votacoes)
    maior, s_maior, posicao = ps_maior(assemb)
    if maior == s_maior:
        return 'Empate tecnico'
    else:
        return partido[posicao]
#funcao auxiliar
def ps_maior(assemb):
    iter = 1
    if assemb[0] > assemb[1]:
        posicao = 0
        maior, s_maior = assemb[0], assemb[1]
    else:
        posicao = 1
        maior, s_maior = assemb[1], assemb[0]
    
    for x in assemb[2:]:
        iter = iter + 1
        if x > s_maior:
            if x > maior:
                posicao = iter
                s_maior, maior = maior, x
            else:
                s_maior = x
    return (maior, s_maior, posicao)
