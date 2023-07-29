import json
import re
import os

file_list = os.listdir(r"C:\Users\felip\desktop\dados")
for arquivo in file_list:
    f = open(f'dados/{arquivo}')
    f2 = open('dados/resultado.json', 'a')

    linha = f.readline()
    r = re.split('(\{.*?\})(?= *\{)', linha)
    for evento in r:
        if evento == '':
            continue
        else:
            data = json.loads(evento)
            if data['identificador'] == "123456789":
                f2.write(evento+'\n')
    f2.close()
