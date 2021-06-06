
################
# Juan Bautista Mangold Moro - @BautiMM
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio Suma Lenta

def suma_lenta(numero, otro_numero):
    print("Ingrese el valor para el primer numero")
numero = int(input())
print("Ingrese el valor para el segundo numero")
otro_numero = int(input())
while otro_numero > 0:
    numero = numero + 1
    otro_numero = otro_numero - 1
    print(numero)
print("El resultado de su operacion es: " + str(numero))
