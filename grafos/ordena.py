#Dada uma lista, realiza a ordenacao de seus
#elementos e imprime a lista ordenada
lista = [5, 10, 8, 6, 1, 7, 4]
#lista = sorted(lista) funcao nativa
print(lista)
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if(lista[i] > lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print(lista)
