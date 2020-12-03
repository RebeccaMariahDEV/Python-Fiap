"""
As vezes temos que recuperar dados de terceiros, que podem ser gerados por logs de sistemas, arquivos de configuração e
outros equipamentos.

Vamos tentar fazer com outros arquivos, entre nesse link e faça o download do primeiro arquivo CSV:
https://data.boston.gov/dataset/economic-indicators-legacy-portal
após isso coloque esse arquivo na sua pasta de desenvolvimento.

No cabeçalho do arquivo temos os:
- Year
- Month
- logan_passengers
- logan_intl_flights
- hotel_occup_rate
- hotel_avg_daily_rate
- total_jobs, unemp_rate
entre outros que não convem.

Bem devemos responder as seguintes respostas:
- Qual o total de voos internacionais que partiram do aeroporto de Logan em 2014?
- Quando (mês/ano) ocorreu o maior transito de passageiros em Logan?
- Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for especificado pelo usuário?
- Qual o mês que possui a maior média da diária de um hotel, com base no ano especificado pelo usuário?

Para responder isso devemos criar uma coisa de cada vez, vamos lá.
"""
# Abrindo o arquivo

with open("economic-indicators.csv", "r") as boston:
    total = 0
    for linha in boston.readlines()[1:-1]:
        total = total + float(linha.split(",")[3])
    print(f"O total de voos é: {total}")
"""
Vamos detalhar o código:
- Na primeira linha, abrimos o arquivo de modo leitura, já vimos isso em
- Criamos uma variavel para armazenar o total de voos
- Montamos um loop para percorrermos somente a linha 1 até a última linha valida, descartando a linha 0 que é o cabeçalho
- Atribuímos na variavel total o valor do terceiro elemento da lista que foi criado por meio do split(), separando os
elementos por virgula(',')
- Imprimimos o conteúdo da variável, quando o loop for encerrado e a variavel total tiver acumulado todos os valores do 
arquivo.

Vamos completar o código:
"""
# complementando

with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input("Qual ano deseja pesquisar?\n")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
    print(f"O total de voos é: {total_voos}")
    print(f"O mês/ano de maior movimento no aeroporto foi: {str(mes)}/{str(ano)}")
    print(f"O total de passageiros do ano {ano_usuario} foi de { total_passageiros}")
    print(f"O mês do ano {ano_usuario} com maior média para diária de hotel foi {mes_maior_diaria}")
