#Declaracoes de importacao
import caminho_minimo
import time
#Leitura do arquivo fonte do grafo
fileName = input("arquivo do grafo: ")
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

#Interacao com o usuario
op = input("Operacao: \n" + 
    "1 dijkstra\n" + 
    "2 Bellman-Ford\n"+
    "3 FloydWarshall")
if(op =="1"):
    s=int(input("insira o vertice inicial"))
    t=int(input("insira o vertice destino"))
    caminho_minimo.dijkstra(listaAdj,s,t)
    print("\n")
elif(op=="2"):
    s=int(input("insira o vertice inicial"))
    t=int(input("insira o vertice destino"))
    caminho_minimo.BellmanFord(listaAdj,arestas,s,t)
    print("\n")
elif(op=="3"):
    s=int(input("insira o vertice inicial"))
    t=int(input("insira o vertice destino"))
    caminho_minimo.FloydWarshall(matAdj,s,t)
    print("\n")
else:
    print("saindo...")