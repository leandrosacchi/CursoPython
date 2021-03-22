from datetime import datetime

def abrirArquivo(a):
    registro = []
    with open(a) as file:
        for line in file:
            registro.append([line[0:5].strip(), line[5:13].strip(), line[13:25].strip()])
        return registro

def converteBytesData(nomeArquivo):
    l = abrirArquivo(nomeArquivo)
    r = []

    for i in l:
        i[2] = datetime.strptime(i[2], '%d %b %Y').date().toordinal()
        if (i[1].__contains__("K")):
            i[1] = int(float(i[1].replace("K",""))*1024)
            r.append(i)
        elif (i[1].__contains__("M")):
            i[1] = int(float(i[1].replace("M",""))*1024*1024)
            r.append(i)
        else:
            i[1] = int(float(i[1]))
            r.append(i)
    return r

def filtraRegistros(nomeArquivo, tamanho, data):
    data = datetime.strptime(data, '%d %b %Y').date().toordinal()
    l = converteBytesData(nomeArquivo)
    nomes = []

    for x in l:
        if (x[1] < tamanho and int(x[2]) < data):
            nomes.append(x[0])

    print ("A quantidade de registros é: " + str(len(set(nomes))))

if __name__ == '__main__':
        filtraRegistros(nomeArquivo="files.txt", tamanho=2*(pow(2,20)), data="28 Feb 2000")