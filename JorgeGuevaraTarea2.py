#Fecha de creacion 28/08/10:00
#Creado por Jorge Guevara
#Ultima modificacion 29/08/2022
#Version 3.10.6
def parImpar(num):
#Ver los numeros pares e impares de un digito.
    num=abs(num)
    if type(num)==int:
        if num==0:
            print("No hay digitos pares")
        else:
            contPar=0
            contImpar=0
            while num!=0:
                digito=num%10
                if digito%2==0:
                    contPar+=1
                else:
                    contImpar+=1
                num=num//10
        print("Pares=",contPar,"Impares=",contImpar)
    else:
        print('Parametro incorrecto')
parImpar(234571)
#################################################################################################################################################################
def parElevacionImparMulti(num):
#Multiplicar y elevar a la tres los numeros Pares.
#Sumar y elevar a la dos los nuemros Impares.
    num=abs(num)
    if type(num)==int:
        if num==0:
            print("No hay digitos")
        else:
            numPar=1
            numImpar=0
            while num!=0:
                digito=num%10
                if digito%2==0:
                    numPar*=digito**3
                else:
                    numImpar+=digito**2
                num=num//10
        print("Pares=",numPar,"Impares=",numImpar)
    else:
        print('Parametro incorrecto')
parElevacionImparMulti(234571)



    