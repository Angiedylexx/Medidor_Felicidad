def medidor_felicidad(archivo):
    data = open(archivo, "r") # abrir como lectura
    tamaño_matrices = list(map(int, data.readline().split()))
    n = list(map(int, data.readline().split()))
    a = set(map(int, data.readline().split()))
    b = set(map(int, data.readline().split()))
    
    medidor_inicial:int = 0
    print(tamaño_matrices)
    print(n)
    print(a)
    print(b)

    for i in n:
        if i in a:
            medidor_inicial +=1
        elif i in b:
            medidor_inicial -=1

    data.close()

    return medidor_inicial


resultado = medidor_felicidad("prueba.txt")
print("El índice de felicidad es:", resultado)


