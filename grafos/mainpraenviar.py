#Declaracoes de importacao
import caminho_minimo
#Leitura do arquivo fonte do grafo
fileName = input("Arquivo do grafo: ")
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

    #interação com o usuario
    op = input("Operacao: \n" + 
    "1 dijkstra\n" + 
    "2 Bellman-Ford\n"+
    "3 Floyd-Wrshall\n")
if(op == "1"):
    s=input("insira o vertice origem: ")
    t=input("insira o vertice destino: ")
    caminho_minimo.dijkstra(listaAdj,s,t)

'''elif(op == "2"):
    s=input("insira o vertice origem: ")
    t=input("insira o vertice destino: ")
    caminho_minimo.BellmanFord(listaAdj,s,t)
elif(op == "3"):
    s=input("insira o vertice origem: ")
    t=input("insira o vertice destino: ")
    caminho_minimo.FloydWarshall(matAdj,s,t)'''
else:
    print("aprete quanquer tecla pra sair...")
    