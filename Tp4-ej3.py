################
# Juan Bautista Mangold Moro - @BautiMM
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio Grados Celsius a Grados Fahrenheit

def prueba():
    fahrenheit = float(input("Ingrese grados Fahrenheit: "))
    centrigrados = float(fahrenheit - 32) * (5/9)
    print("Los grados Fahrenheit anteriormente puestos se traducen a: ", (centrigrados), "en grados Celsius")
    centigrados = float(input("Ingrese grados Celsius: "))
    fahrenheit = float(centigrados * 9/5) + 32
    print("Los grados Celsius anteriormente puestos se traducen a: ", (fahrenheit), "en grados Fahrenheit")
if __name__ == "__main__":
    prueba()
