def split(teste):
    return [char for char in teste]

teste = 'Mateus'
lista = split(teste)

listas = [18, 9, 19, 99]


print(''.join([str(mat) + eus for mat, eus in zip(listas, lista)]))
print(''.join([str(mat) + eus for mat, eus in zip(lista, lista)]))
