lista = [10,20,30,40,50]
print (f'lista inicial é {lista}')

lista[1] = 200
print(f'lista depois de mudar o segundo elemento: {lista}')

lista.append(600)
print(f'lista depois de adicionar um ultimo valor: {lista}')

lista.insert(2, 300)
print(f'lista depois de inserir um novo valor: {lista}')

lista.remove(600)
print(f'lista depois de remover o ultimo valor: {lista}')

lista.pop(0)
print(f'ultima modificação na lista: {lista}')