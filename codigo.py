n= int(input("\ndigite un numero entero positivo : "))
while n<0:
    print("ES un digito negativo")
    n = int(input("\ndigite un numero entero positivo : "))
calculo =n ; inverso =0 ;contador=0
while calculo//10**contador != 0:
    contador=contador+1


while contador != 0:
    digito=(calculo%10)*10**contador
    calculo=(calculo-digito)//10
    inverso=digito+inverso
    contador=contador-1
print("\n\nEl inverso es  : "+str(inverso//10)+ "  Del numero : "+str(n))