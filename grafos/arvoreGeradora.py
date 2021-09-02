def Prim(listaAdj,s):
    custo=0
    A = []
    dist = [100000 for i in range(len(listaAdj))]
    pai = [0 for i in range(len(listaAdj))]
    dist[s] = 0
    Q = []
    for i in range(len(Q)):
        if Q[i]!=s:
            Q[i] = i 
    for v in range(len(listaAdj[s])):
        if dist[listaAdj[s][v][0]]>listaAdj[s][v][1]:
            dist[listaAdj[s][v][0]]=listaAdj[s][v][1]
            pai[listaAdj[s][v][0]]=listaAdj[s]
    while len(Q)!=0:
        min = 1000000
        for i in range(len(Q)):
            if min>dist[i]:
                min=dist[i]
                u=i
        Q.remove(u)
        for v in range(len(listaAdj[u])):
            if dist[listaAdj[u][v][0]]>listaAdj[u][v][1]:
                dist[listaAdj[u][v][0]]=listaAdj[u][v][1]
                pai[listaAdj[u][v][0]] = listaAdj[u]
        A.append((pai[u],u),dist[u])
        custo= custo + dist[u]
    return A


