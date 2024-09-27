import tkinter as tk
from tkinter import messagebox
from radix_sort import radix_sort  
def procesar_ascendente():
    try:
        lista = list(map(int, entrada_lista.get().split(',')))
        lista_ordenada, operaciones = radix_sort(lista, ascendente=True)
        messagebox.showinfo("Resultado", f"Lista ordenada ascendente: {lista_ordenada}")
        proceso_texto.insert(tk.END, f'Lista ordenada ascendente: {lista_ordenada}\n')
        proceso_texto.insert(tk.END, f'Total de operaciones: {operaciones}\n')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una lista válida de números separados por comas.")

def procesar_descendente():
    try:
        lista = list(map(int, entrada_lista.get().split(',')))
        lista_ordenada, operaciones = radix_sort(lista, ascendente=False)
        messagebox.showinfo("Resultado", f"Lista ordenada descendente: {lista_ordenada}")
        proceso_texto.insert(tk.END, f'Lista ordenada descendente: {lista_ordenada}\n')
        proceso_texto.insert(tk.END, f'Total de operaciones: {operaciones}\n')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una lista válida de números separados por comas.")

def pantalla_inicio():
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Equipo de Ordenamiento")
    
    label_bienvenida = tk.Label(ventana_inicio, text="Bienvenido al Ordenador Radix Sort", font=("Arial", 16))
    label_bienvenida.pack(pady=10)
    
    label_equipo = tk.Label(ventana_inicio, text="Equipo: \n- Negron Salazar Danna\n- Patiño Tun Hugo Alberto\n- Rios Fuentes Sebastian Eligio", font=("Arial", 12))
    label_equipo.pack(pady=10)

    descripcion_radix = (
        "Radix Sort es un algoritmo de ordenamiento no comparativo que organiza los números "
        "basándose en sus dígitos. Comienza ordenando los números desde el dígito menos "
        "significativo hasta el más significativo. Este método es especialmente eficaz "
        "para ordenar enteros y se utiliza frecuentemente en situaciones donde los números "
        "a ordenar tienen un rango limitado."
    )
    
    label_descripcion = tk.Label(ventana_inicio, text=descripcion_radix, wraplength=300)
    label_descripcion.pack(pady=10)

    boton_iniciar = tk.Button(ventana_inicio, text="Iniciar", command=lambda: [ventana_inicio.destroy(), iniciar_programa()])
    boton_iniciar.pack(pady=10)

    ventana_inicio.mainloop()

def iniciar_programa():
    global entrada_lista, proceso_texto
    
    ventana = tk.Tk()
    ventana.title("Ordenamiento Radix Sort")
    
    label_lista = tk.Label(ventana, text="Ingresa una lista de números separados por comas:")
    label_lista.pack(pady=5)
    
    entrada_lista = tk.Entry(ventana, width=50)
    entrada_lista.pack(pady=5)
    
    boton_ascendente = tk.Button(ventana, text="Orden Ascendente", command=procesar_ascendente)
    boton_ascendente.pack(pady=5)
    
    boton_descendente = tk.Button(ventana, text="Orden Descendente", command=procesar_descendente)
    boton_descendente.pack(pady=5)
    
    proceso_texto = tk.Text(ventana, height=20, width=70) 
    proceso_texto.pack(pady=10)
    
    ventana.mainloop()

pantalla_inicio()