'''
Crie uma função com o nome para verificar ser um número é primo ou não.
- A função deverá verificar se trata-se de um número inteiro e maior que zero, caso contrário deverá retornar a
mensagem "invalid argument"
- Caso o argumento recebido seja válido, a função deverá verificar se trata-se de um número retornando a
mensagem "prime number", caso contrário "not a prime number"
- O valor máximo que a função calculará é de 5,5 * 10^7. Caso o número passado como argumento seja maior, retornar a
mensagem "argument out of range"
'''

def verificaNumeroPrimo(a):
    count = 0
    if (type(a) != int or a <= 0):
        return "invalid argument"
    elif (a > 5.5*10E7):
        return "argument out of range"
    else:
        for x in range(1,a+1,1):
            if(a%x == 0):
                count += 1
        if (count == 2):
            return "prime number"
        else:
            return "not a prime number"

'''
Crie uma função com o nome sum_of_products que:
- Receba duas listas numéricas como argumento.
- Verifique todo o conteúdo das duas listas e retorne a mensagem de erro "wrong number" caso algum elemento 
não seja um número.
- A função deverá retornar a soma dos produtos de elementos de mesmo indice de cada lista
- Caso uma das listas tenha mais elementos que a outra, considere 1 para o produto com cada elemento da lista 
com maior número de elementos
- Caso as duas listas estejam vazias, retornar -1.
'''

def calc(l1, l2):
    r=0
    for x,y in zip(l1,l2):
        r += x*y
    return r

def sum_of_products(l1, l2):
    count = 0
    len_l1 = len(l1)
    len_l2 = len(l2)

    #verifica tipos dos elementos das listas
    for x in l1:
        if (type(x) != int and type(x) != float):
            count += 1
    for x in l2:
        if (type(x) != int and type(x) != float):
            count += 1

    if (count == 0):
        if (len_l1 == 0 and len_l2 == 0):
            return -1
        elif (len_l1 > len_l2):
            d = len_l1 - len_l2
            l2 += ([1] * d)
            return calc(l1, l2)
        elif (len_l1 < len_l2):
            d = len_l2 - len_l1
            l1 += ([1] * d)
            return calc(l1, l2)
        else:
            return calc(l1, l2)

    else:
        return 'wrong number'

if __name__ == '__main__':
    print(sum_of_products([1,2,3,4,5,6,4,5,6],[2,2,2,1,1]))