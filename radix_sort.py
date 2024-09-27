contador_operaciones = 0

# Función para hacer Counting Sort
def counting_sort(arr, exp, ascendente=True):
    global contador_operaciones
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar ocurrencias de dígitos
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        contador_operaciones += 1
    
    # Acumular el conteo
    if ascendente:
        for i in range(1, 10):
            count[i] += count[i - 1]
    else:
        for i in range(8, -1, -1):
            count[i] += count[i + 1]

    # Construir el array ordenado
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr

# Función principal de Radix Sort
def radix_sort(arr, ascendente=True):
    global contador_operaciones
    contador_operaciones = 0  # Reiniciar el contador al iniciar el ordenamiento
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp, ascendente)
        exp *= 10
    return arr, contador_operaciones