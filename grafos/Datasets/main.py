#Declaracoes de importacao
import info

#Leitura do arquivo fonte do grafo
fileName = input("Arquivo do grafo: ");
file = open(fileName)

str = file.readline()
str = str.split(" ")
numVertices = int(str[0])
numArestas = int(str[1])

#Preenchimento das estruturas de dados
listaAdj = [[] for x in range(numVertices)]
matAdj = [[0 for x in range(numVertices)] for x in range(numVertices)] 
vertices = [x for x in range(numVertices)]
arestas = []

for i in range(0,numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int(str[0])
    destino = int(str[1])
    peso = int(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))

print(listaAdj)
print(matAdj)

#Interacao com o usuario
op = input("Operacao: \n" + 
    "1 Densidade\n" +
    "2 Complemento\n" +
    "3 Completo\n" +
    "4 Regular\n");
if(op == "1"):
    densidade = info.densidade(vertices, arestas)
    print("Densidade: %.2f" % densidade)
elif(op == "2"):
    complemento = info.complemento(matAdj)
    print("Complemento:", complemento)
    print("Original:   ", matAdj)
elif(op == "3"):
    if(info.completo(matAdj)):
        print("Grafo completo!")
    else:
        print("Grafo NAO completo")

input("Aperte qualquer tecla para sair...")
