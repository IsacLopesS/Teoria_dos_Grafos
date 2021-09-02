import time
def dijkstra(listaAdj,s,t):
    print("Origem: <%d>\nDestino: <%d>"%(s,t))
    print("Processando...")
    ini=time.time()
    dist = [100000 for x in range(len(listaAdj))]
    pred = [None for x in range(len(listaAdj))]
    dist[s]=0
    Q =[i for i in range(len(listaAdj))]
    #print(Q)
    while len(Q)!=0:
        min=100000
        for i in range(len(Q)):
            if min>dist[Q[i]]:
                min = dist[Q[i]]
                u=Q[i]
                p=i
        Q.pop(p)

        for v in range(len(listaAdj[u])):
            if dist[listaAdj[u][v][0]]>dist[u]+ listaAdj[u][v][1]:
                dist[listaAdj[u][v][0]]=dist[u]+ listaAdj[u][v][1]
                pred[listaAdj[u][v][0]]=u
           
    aux = t
    caminho = []
    caminho.append(t)
    while aux!=s:
        caminho.insert(0,pred[aux])
        aux=pred[aux]
    fim=time.time()
    print("Caminho: ",caminho)
    print("Custo: %d"%dist[t])
    print("tempo: ",fim-ini)       
            


    


def BellmanFord(listaAdj,arestas,s,t):
    print("Origem: <%d>\nDestino: <%d>"%(s,t))
    print("Processando...")
    ini=time.time()
    dist = [10000 for i in range(len(listaAdj))]
    pred = [None for i in range(len(listaAdj))]    
    dist[s]=0
    for i in range(len(listaAdj)):
        for j in range(len(arestas)):
            if dist[arestas[j][1]]>dist[arestas[j][0]] + arestas[j][2]:
               dist[arestas[j][1]]=dist[arestas[j][0]] + arestas[j][2]
               pred[arestas[j][1]]=arestas[j][0]
   
    
    for j in range(len(arestas)):
        if dist[arestas[j][1]]>dist[arestas[j][0]]+arestas[j][2]:
            return False
    aux = t
    caminho = []
    caminho.insert(0,aux)
    while aux!=s:
        caminho.insert(0,pred[aux])
        aux=pred[aux]
    fim=time.time()
    
    print("Caminho: ",caminho)
    print("Custo: %d"%dist[t])
    print("tempo: ",fim-ini)
    


def FloydWarshall(matAdj,s,t):
    print("Origem: <%d>\nDestino: <%d>"%(s,t))
    print("Processando...")
    inicio = time.time()
    dist = [[0 for i in range(len(matAdj))] for i in range(len(matAdj))]
    pred = [[None for i in range(len(matAdj))] for i in range(len(matAdj))]
    for i in range(len(matAdj)):
        for j in range(len(matAdj)):
            if i==j:
                dist[i][j]=0
            elif matAdj[i][j]!=0:
                dist[i][j]=matAdj[i][j]
                pred[i][j]= i
            else:
                dist[i][j]=100000
                pred[i][j]=None
    for k in range(len(matAdj)):
        for i in range(len(matAdj)):
            for j in range(len(matAdj)):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
                    pred[i][j]=pred[k][j]
    
    f=t
    caminho = []
    while(f!=s):
        caminho.insert(0,f)
        f=pred[s][f]
    caminho.insert(0,f)

    fimm = time.time()

    
    print("Custo: %d"%dist[s][t])
    print("tempo: ",fimm-inicio)
    print("caminho: ",caminho)

    
       
    



    


                





