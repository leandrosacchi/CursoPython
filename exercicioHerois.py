import csv
'''
    ## Exercício 2

    ### Considere um arquivo CSV (comma separated values) com informações demográficas sobre super heróis
    (heroes_information.csv):
    - id - Numero da linha
    - name - Nome
    - Gender - Gênero
    - Eye color - Cor dos olhos
    - Race - Raça
    - Hair color - Cor do cabelo
    - Height - Altura em centimetros
    - Publisher - Estúdio
    - Skin color - Cor da pele
    - Alignment - Vilão ou herói
    - Weight - Peso em libras

    ### Pede-se
    * Crie uma função que efetue a leitura do arquivo e crie:
        - Um arquivo de saida (heroes_male.csv) com todos os heróis do gênero masculino (id, name)
        - Um arquivo de saida (heroes_female.csv) com todos os heróis do gênero feminino (id, name)
        - Um arquivo de saida (heroes_no_gender.csv) com todos os heróis sem gênero defindo (id, name)
        - Um arquivo de saida (heroes_mavel_comics.txt) com o nome de todos os heróis dos estúdios Marvel Comics
        e DC Comics (um nome por linha)
        - Um arquivo de saida (heroes_cheater_blue_skin.txt) com o nome de todos os heróis que tenham
        cor de pele azul e que sejam vilões (uma única linha com os nomes separados por #)
'''


def abrirArquivo(input):
    l = []

    with open(input, 'r') as file:
        for line in file:
            l.append(line.strip().split(','))
        listMale(l, 'heroes_male.csv')
        listFemale(l, 'heroes_female.csv')
        listNoGender(l, 'heroes_no_gender.csv')
        listMarvelDC(l, 'heroes_mavel_comics.txt')
        listBlueVilain(l, 'heroes_cheater_blue_skin.txt')

def listMale(l, output):
    with open(output, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id","name"])
        for x in l:
            if (x[2] == 'Male'):
                writer.writerow([x[0], x[1]])

def listFemale(l, output):
    with open(output, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id","name"])
        for x in l:
            if (x[2] == 'Female'):
                writer.writerow([x[0], x[1]])

def listNoGender(l, output):
    with open(output, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id","name"])
        for x in l:
            if (x[2] == '-'):
                writer.writerow([x[0], x[1]])

def listMarvelDC(l, output):
    with open(output, 'w', newline='', encoding='UTF-8') as file:
        for x in l:
            if (x[7] == 'Marvel Comics' or x[7] == 'DC Comics'):
                file.write(x[1]+"\n")

def listBlueVilain(l, output):
    with open(output, 'w', newline='', encoding='UTF-8') as file:
        for x in l:
            if (x[8] == 'blue' and x[9] == 'bad'):
                file.write(x[1]+"#")

if __name__ == '__main__':
    abrirArquivo("heroes_information.csv")

