colunas = ['azul', 'preto', 'amarelo', 'vermelho']
struc = []

count = len(colunas)


for coluna in range(count):
    struc.append(f"<th>{colunas[coluna]}</th>")

struc.insert(0,'<tr>')
struc.append('</tr>')
                                               

resultado = ''.join(struc)
print(resultado)