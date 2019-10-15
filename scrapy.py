import re
import requests
import json
import csv

r = requests.get('https://www.pensador.com/autor/albert_einstein/')
site1 = r.text

s = requests.get('https://www.pensador.com/autor/roberto_shinyashiki/')
site2 = s.text

frase = re.findall(r'<p class="frase \w+" id=".+">.+</p>',site1)
autor = re.findall(r'<span class="autor">\n.+</span>',site1)
like = re.findall(r'<div class="total-shares">.+<span>',site1)

frase1 = re.findall(r'<p class="frase \w+" id=".+">.+</p>',site2)
autor1 = re.findall(r'<span class="autor">\n.+</span>',site2)
like1 = re.findall(r'<div class="total-shares">.+<span>',site2)

frase.extend(frase1)
autor.extend(autor1)
like.extend(like1)

lista = [[],[],[]]

for x in frase:
    for letra in range(len(x)):
        if x[letra] == '>':
            lista[0].append(x[letra+1:len(x)-4])
            break

for x in autor:
    for letra in range(len(x)):
        if x[letra:letra+1] == "\n":
            lista[1].append(x[letra+1:len(x)-7])
            break
for x in like:
    for letra in range(len(x)):
        if x[letra] == '>':
            lista[2].append(x[letra+1:len(x)-6])
            break
aux = []
for i in range(len(frase)):
    aux2 = {'frase':lista[0][i],'autor':lista[1][i],'like':lista[2][i]}
    aux.append(aux2)
aux3 = {'frases':aux}
            
#json
with open('arquivo.json' , 'w', encoding="utf8") as f:
    json.dump(aux3, f , ensure_ascii=False)

#csv
with open('dados_escrita.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['FRASE','AUTOR','QTD. DE COMPARTILHAMENTOS'])
    for x in range(len(frase)):
        spamwriter.writerow([lista[0][x],lista[1][x],lista[2][x]])

