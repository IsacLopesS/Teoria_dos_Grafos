def GREEDYCOL(listaAdj):
    s = [i for i in range(len(listaAdj))]
    cores = [x for x in range(len(listaAdj))]
    for u in range(len(listaAdj)):
        coresP=cores.copy()
        for i in range(len(cores)):
            for v in range(len(listaAdj[u])):
                y=0
                for h in range(len(coresP)):
                    if coresP[h]==i:
                        y=1
                        h=len(coresP)+1

            if s[v]==i and y==1:
                coresP.remove(i)
        s[u]=coresP[0]
    return s

