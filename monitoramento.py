def pega_periodo():
    '''
    Função que obtém o período de monitoramento das temperaturas 
    retorno: periodo -> lista contendo o número de dias(colunas) e de semanas(linhas) obtidos pelo usuário
    '''
    dias = int(input('Dias por semana: '))
    semanas = int(input('Semanas: '))
    periodo = [dias, semanas]
    return periodo

def pega_temp(periodo):
    '''
    Função que cria e popula uma matriz para armazenar as temperaturas obtidas pelo usuário
    parâmetro: periodo -> lista contendo o número de dias e de semanas
    retorno: temperaturas -> matriz contendo as temperaturas
    '''
    temperaturas = []
    for i in range(periodo[1]):
        semanas = []
        for j in range(periodo[0]):
            temperatura = float(input('Temperatura: '))
            semanas.append(temperatura)
        temperaturas.append(semanas)
    return temperaturas

def pega_menor_maior(temperaturas):
    '''
    Função que busca a menor e a maior temperatura em uma matriz de temperaturas
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: maior_menor -> Lista contendo a menor e a maior temperatura respectivamente
    '''
    menor = temperaturas[0][0]
    maior = temperaturas[0][0]
    for semana in temperaturas:
      for temperatura in semana:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
    menor_maior = [menor, maior]
    return menor_maior

def separa_negativas(temperaturas):
    '''
    Função que cria e popula uma lista contendo apenas temperaturas negativas
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: negativas -> Lista contendo apenas temperaturas negativas
    '''
    negativas = []
    for semana in temperaturas:
      for temperatura in semana:
        if temperatura < 0:
            negativas.append(temperatura)
    return negativas

def soma(temperaturas):
    '''
    Função que calcula a soma das temperaturas em uma Matriz
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: soma -> Soma das temperaturas
    '''
    soma = 0
    for semana in temperaturas:
      for temperatura in semana:
        soma += temperatura
    return soma

def media_temp(temperaturas):
    '''
    Função que calcula a média das temperaturas em uma Matriz
    parâmetro: temperaturas -> Matriz contendo temperaturas
    retorno: media -> Média das temperaturas
    '''
    media = soma(temperaturas) / (len(temperaturas) * len(temperaturas[0]))
    return media

def imprimir_resultador(temperaturas, menor_maior, negativas, media):
    '''
    Função que imprime os resultados obtidos
    parâmetro: temperaturas -> Matriz contendo temperaturas
               menor_maior -> Lista contendo a menor e a maior temperatura respectivamente
               negativas -> Lista contendo apenas temperaturas negativas
               media -> Média das temperaturas
    retorno: sem retornos
    '''
    print(f'\nTemperaturas:\n{temperaturas}\n')
    print(f'Menor temperatura: {menor_maior[0]}°C')
    print(f'Maior temperatura: {menor_maior[1]}°C\n')
    print(f'Temperaturas negativas: {negativas}\n')
    print(f'Média das temperaturas: {media:.1f}°C')
def principal():
    '''
    Função principal, responsável por chamar as demais funções
    parâmetro: sem parâmetros
    retorno: sem retornos
    '''
    periodo = pega_periodo()
    temperaturas = pega_temp(periodo)
    menor_maior = pega_menor_maior(temperaturas)
    negativas = separa_negativas(temperaturas)
    media = media_temp(temperaturas)
    imprimir_resultador(temperaturas, menor_maior, negativas, media)

principal()