#Dados peso e altura retorna o IMC
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura * altura)
print(imc)
if(imc < 18.5):
    print("Abaixo do peso")
elif(imc >= 18.5 and imc <= 25):
    print("Peso ideal")
else:
    print("Acima do peso")
