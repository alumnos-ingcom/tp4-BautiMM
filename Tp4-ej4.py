################
# Juan Bautista Mangold Moro - @BautiMM
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 4. Comparación de números

def prueba():
    numero = int(input("Escriba un numero: " ))
    numerodos = int(input("Escriba un segundo numero: " ))
    if numero < numerodos : 
            print(-1)
    if numero == numerodos :
            print(0)
    if numero > numerodos :
            print(1)       
if __name__ == "__main__":
    prueba()