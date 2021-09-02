#Dada uma lista busca um determinado elemento
#se ele for encontrado seu indice e imprimido
#caso contrario imprime que o elemento nao foi encontrado
lista = [5, 3, 7, 9, 4, 6]
print(lista)
elem = int(input("Informe o elemento a ser buscado: "))
encontrado = 0
for i in range(len(lista)):
    if(lista[i] == elem):
        print("%d esta na posicao %d" % (elem, i))
        encontrado = 1
        break
if(encontrado == 0):
    print("%d nao esta na lista" % elem)
