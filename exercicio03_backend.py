altura =  float(input("Informe a altura da pessoa: "))
sexo = input("Informe o sexo da pessoa (M/F):")

peso = 0.0
#if sexo == 'M' or sexo =='m':
   if sexo.lower() == 'm':
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print(f"O peso ideal é: {peso:.2f} Kg")

