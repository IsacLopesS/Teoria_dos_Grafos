def Prim(lisaAdj,s):
    A = []
    dist = [100000 for i in range(len(listaAdj))]
    pai = [0 for i in range(len(listaAdj))]
    interligado = [False for i in range(len(listaAdj))]
    dist[s] = 0
    Q = []
    for i in range(len(listaAdj)):
        if Q[i]!=s:
            Q[i] = i 
    for v in range(len(listaAdj[s])):
        if dist[listaAdj[s][0]]>listaAdj[s][1]:
            dist[listaAdj[s][0]]=listaAdj[s][1]
            pai[listaAdj[s][0]]=listaAdj[s]
    while len(Q)!=0:
        u = 1000000
        for i in range(len(Q)):
            if u>dist[i]:
                u=dist[i]
        for v in range(lestaAdj[u]):
            if dist[listaAdj[u][0]]>listaAdj[u][1]:
                dist[listaAdj[u][0]]=listaAdj[u][1]
                pai[listaAdj[u][0]] = listaAdj[u]
        A.append(pai[u],u)



