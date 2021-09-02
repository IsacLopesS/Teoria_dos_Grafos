#Dados os coeficientes a, b e c calcula as raizes
#de uma equacao do segundo grau
import math

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
c = float(input("Informe o coeficiente c: "))
delta = b * b - (4 * a * c)
if(delta > 0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("As raizes sao %f e %f" % (x1, x2))
elif(delta == 0):
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz e %f" % x1)
else:
    print("Nao ha raizes reais")
    
