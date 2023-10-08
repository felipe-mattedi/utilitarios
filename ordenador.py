import re

arquivo = open('linhas.txt')
linhas = arquivo.read().splitlines() 
trilha_geral = []
for linha in linhas:
    trilha_geral.append(re.split(',',linha))

elemento_1 = None
elemento_2 = None
tamanho = len(trilha_geral)
i = 0
arquivo = 1
contagem_prova = 0

while i < tamanho:
    trilha_ordenada = []
    elemento_1 = trilha_geral[0][0]
    elemento_2 = trilha_geral[0][1]
    trilha_ordenada.append(elemento_1)
    trilha_ordenada.insert(0, elemento_2)
    trilha_geral.remove(trilha_geral[0])
    tamanho-=1
    while i < tamanho:
        if trilha_ordenada[-1] == trilha_geral[i][1]:
            trilha_ordenada.append(trilha_geral[i][0])
            trilha_geral.remove(trilha_geral[i])
            tamanho-=1
            i=0
        else:
            i+=1
    i=0
    while i < tamanho:
        if trilha_ordenada[0] == trilha_geral[i][0]:
            trilha_ordenada.insert(0,trilha_geral[i][1])
            trilha_geral.remove(trilha_geral[i])
            tamanho-=1
            i=0
        else:
            i+=1
    total = len(trilha_ordenada)
    contagem_prova += total
    f = open(f'arquivo_{arquivo}',"w")
    for identificador in trilha_ordenada:
        f.writelines(f'{identificador}\n')
    i=0
    arquivo+=1
print(f'Termino do processamento, contagem final {contagem_prova}')

