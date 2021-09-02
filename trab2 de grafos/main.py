#Declaracoes de importacao
import cviajante
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
    peso = float(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))

#Interacao com o usuario
op = input("Operacao: \n" + 
    "1 NEARESTNEIGHBOR\n" + 
    "2 TWOOPT\n")
if(op =="1"):
    tempo=0
    s = cviajante.NEARESTNEIGHBORfr(listaAdj)
    custo = cviajante.Avalia(s[0],matAdj)
    tempo+=s[1]
    tempo+=custo[1]
    print("Grafo: "+ fileName)
    print("Distancia: ")
    print(custo[0]) 
    print("Processando...")
    sf=cviajante.twoopt(s[0],matAdj)
    custof=cviajante.Avalia(sf[0],matAdj)
    tempo+=sf[1]
    tempo+=custof[1]
    print("Distancia: ")
    print(custof[0])
    print("Rota: ")
    print(sf[0])
    print("tempo: %fs "%tempo)
    
    
elif(op=="2"):
    s=int(input("insira o vertice inicial"))
    
    print("\n")
else:
    print("saindo...")