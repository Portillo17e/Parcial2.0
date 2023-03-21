numero1=int(input("Ingrese primer numero"))
numero2=int(input("Ingrese segundo numero"))

while numero1 != 0 :
    if numero1 > numero2:
        print("El numero mayor es",numero1)
        print("EL numero menor es",numero2)
    elif numero2 > numero1:
        print("El numero mayores",numero2)
        print("El numero menor es",numero1)
    break