'''
Escreva uma função que receba três parâmetros (a, b e c) inteiros
e retorne o maior valor entre os argumentos passados
'''

def maiorValor(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    return c


def maiorValor2(a, b, c):
    l = [a,b,c]
    l.sort()
    return l[2]

'''
Escreva uma função que receba uma lista de números e retorne
uma tupla com duas listas, a primeira contendo todos os numeros
pares e a segunda contendo todos os numeros impares
ordenados
'''

def geraTuplas(l):
    par = []
    impar = []

    if (type(l) == list):
        for x in l:
            if (x % 2 == 0):
                par.append(x)
                par.sort()
            else:
                impar.append(x)
                impar.sort()
        return (par, impar)
    return "O parâmetro não é uma lista."

'''
Escreva uma função que receba dois valores inteiros positivos, e
retorne a soma da sequencia numérica inteira entre o primeiro e o
segundo parâmetros, inclusive
'''

def somaSequencia(a, b):
    c=0
    if (type(a) != int or type(b) != int):
        return "Os valores precisam ser números inteiros"
    else:
        if (a<0 or b<0):
            return "Os números precisam ser positivos"
        else:
            l = list(range(a,b+1))
            for x in l:
                c = c+x
            return c

'''
Dado um número inteiro não negativo (n), escreva duas funções
sendo a primeira usando estruturas de repetição FOR e a
segunda usando estruturas de repetição WHILE, que retornem o
fatorial de n (n!)
'''

def fatorialFor(a):
    c=1
    if (type(a) != int):
        return "O valor precisa ser número inteiro"
    else:
        if (a<0):
            return "O número precisa ser positivo"
        else:
            l = list(range(1, a))
            for x in l:
                c += c*x
            return c

def fatorialWhile(a):
    x = c = 1
    if (type(a) != int):
        return "O valor precisa ser número inteiro"
    else:
        if (a < 0):
            return "O número precisa ser positivo"
        else:
            l = list(range(1, a))
            while x < len(l)+1:
                c += c*x
                x += 1
            return c

if __name__ == '__main__':
    print(fatorialWhile(5))