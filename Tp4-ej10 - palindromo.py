################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Palindromo

def prueba():
    palindromos = [
        'AnitaLavaLaTina' ,
        'oso' ,
        'neuquen' ,
        'nada' ,
        123321,
        
    ]

    def es_palindromo(p):
        estandar = str(p).lower().replace('  ', ' ')
        return estandar == estandar [: : -1]
    if __name__ == "__main__":
        for p in palindromos:
            resultado = es_palindromo(p)
            print(resultado)

if __name__ == "__main__":
    prueba()
