################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ejercicio Maximo/Minimo

def prueba():
    print("Bienvenido")
    lista = list(range(1,10))
    print("La lista es: ",(lista))
    def minimo(lista):
        return (lista[0])
    def maximo(lista):
        return (lista[8])
    print("El minimo es: ",minimo(lista))
    print("El maximo es: ",maximo(lista))
if __name__ == "__main__":
    prueba()