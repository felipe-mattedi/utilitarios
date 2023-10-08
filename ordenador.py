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
verificador_1 = 0
verificador_2 = 0
primeiros_itens = []
trilhas_globais = []

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
    primeiros_itens.append(trilha_ordenada.pop(0))
    total = len(trilha_ordenada)
    trilhas_globais.append(trilha_ordenada)
    verificador_1 += total
    i=0
print('*****************************************')
print(f'Termino do processamento, contagem final {verificador_1}')
print('*****************************************')
print(f'Verificar processamento dos itens abaixo')
print('*****************************************')
print(primeiros_itens)
print('*****************************************')

k = 0
maior_trilha = 0

for trilha in trilhas_globais:
    tamanho_trilha = len(trilha)
    if tamanho_trilha > maior_trilha:
        maior_trilha = tamanho_trilha

while k < maior_trilha:
    f = open(f'arquivo_{arquivo}',"w")
    for trilha in trilhas_globais:
        try:
            identificador = trilha[k]
            f.writelines(f'{identificador}\n')
            verificador_2 += 1
        except IndexError:
            continue
    arquivo+=1
    k+=1

print(f'Termino geracao arquivos, total {verificador_2}')
print('*****************************************')
