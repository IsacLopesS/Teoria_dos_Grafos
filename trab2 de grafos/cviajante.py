import time
import copy
import random
def NEARESTNEIGHBORfr(listaAdj):
    r=time.time()
    u=0
    s=[]
    s.append(u)
    naoVisitados = [x for x in range(len(listaAdj))]
    naoVisitados.remove(0)
    while len(naoVisitados)!=0:
        min=100000
        for i in range(len(listaAdj[u])):
            if listaAdj[u][i][1]<min and listaAdj[u][i][0] in naoVisitados:
                min=listaAdj[u][i][1]
                v=listaAdj[u][i][0]
            
             
        s.append(v)
        naoVisitados.remove(v)
        u=v    
    s.append(s[0])
    rf=time.time()
    tempo=rf-r
    return [s,tempo]


def Avalia(s,matAdj):
    ti=time.time()
    custo=0
    for i in range(len(s)-1):
        u=s[i]
        v=s[i+1]
        if(matAdj[u][v]!=0):

            custo=custo + matAdj[u][v]
    tf=time.time()
    tf=tf-ti
    return [custo,tf]

def twoopt(s,matAdj):
    e=time.time()
    td = 60
    
    while td>0:
        ini = time.time()
        from random import randint
        i1 = randint(1,(len(s)-2))
        i2 = randint(1,(len(s)-2))
        if i1!=i2:
            sc = s.copy()
            aux = sc[i1]
            sc[i1]=sc[i2]
            sc[i2]=aux
            if Avalia(sc,matAdj) < Avalia(s,matAdj):
                s = sc
        fim = time.time()
        td = td - (fim-ini)
    ef = time.time()
    tempo = ef-e
    return [s,tempo]





        





        

                
                


