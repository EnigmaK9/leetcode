def numeros_impares():
    numero = int(input("Teclea el número: "))

    if numero == 0:
        print("No es un número primo")
    elif numero == 1:
        print("No es un número primo")
    else:
        contador = 1
        while True:
            contador += 1
            if numero % contador == 0:
                break
        if numero == contador:
            print("Es un número primo")
        else:
            print("No es un número primo")

numeros_impares()

