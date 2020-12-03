"""
Imagine que temos uma aplicação e a mesma terá que se conectar com outras, como a PF, bancos, correios etc, como será
possível estabelecer uma comunicação entre a sua aplicação e qualquer outra aplicação no mundo que queira trocar dados?
Simples: utilizando um padrão de comunicação. Um padrão muito comum é o XML, que permite a troca de dados entre
plataformas distintas, um exemplo é a nota fiscal, ela roda em todo o país e não importa se usa Windows, Linux, IOS ou
qualquer outra, também não importa a linguagem usada para desenvolver a ferramenta. O único fator que importar é que os
dados sejam criados dentro do padrão, mas não vamos falar dele e sim o padrão JSON; é a sigla de:
JavaScriot Object Notation, é um padrão de armazenamento de dados, vamos a um exemplo prático:
"""
# Ex JSON
import json

inventario = {}
opcao = int(input("Digite:\n"
                  "< 1 > para registrar ativo\n"
                  "< 2 > para exibir ativos armazenados:\n"))
while opcao > 0 and opcao < 3:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial:\n")] = [
                input("Digite a data da última atualização:\n"),
                input("Digite a descrição:\n"),
                input("Digite o departamento:\n")]
            resp = input("Digite <S> para continuar ou <N> para sair\n").upper()

        with open("inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json)
        print("JSON gerado!!!!")

    elif opcao == 2:
        with open("inventario_json.json", "r") as arq_json:
            resultado = json.load(arq_json)

            for chave, dado in resultado.items():
                print(f"Data.........:{dado[0]}")
                print(f"Descrição....: {dado[1]}")
                print(f"Departamento.: {dado[2]}")
    opcao = int(input("Digite:\n"
                      "< 1 > para registrar ativo\n"
                      "< 2 > para exibir ativos armazenados\n"
                      "< 3 > Para sair:\n"))

"""
JSON gerado com sucesso, apenas o nosso arquivo e agora temos mais alguns passos, percebe que mudamos algumas coisas? 
aqui temos um import diferente, essa é uma biblioteca pronta para mexer com JSON em python, também mudamos o menu, e a 
persistência de dados foi feita logo após inserir os dados ele está no nosso dicionário em formato JSON.
Para gravarmos o dicionário 'inventario' no arquivo utilizamos o método dump(), que pertence ao objeto 'json'; esse 
método é formado por dois parâmetros, caso o arquivo não exista será criado, caso já tenha será sobrescrito  então cuidado

Por que não usar o método para concatenar então?!, porque quando o método dump() fosse chamado, após a primeira vez, ele
não iria adicionar as informações do dicionário ao arquivo, mas criar uma nova estrutura dentro do arquivo.

Na opção 2 abrimos o nosso arquivo apenas para leitura certo, então chamamos o método load(), que também é da biblioteca
json, ele carrega o arquivo informando o parametro para uma variavel, em seguida montamos um laço que irá trazer a chave
e os dados, finalizando com o menu novamente; agora precisamos saber como colocar dados sem sobrescrever certo?!

Então vamos adicionar mais algumas coisas ao nosso código ok:
"""
# Refatorando para adicionar dados e não sobrescrever

with open("inventario_json.json", "r") as arq_json:
    inventario = json.load(arq_json)

opcao = int(input("Digite\n"
                  "< 1 > para registrar ativo\n"
                  "< 2 > para exibir ativos armazenados:\n"))

while opcao > 0 and opcao < 3:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial:\n")] = [
                input("Digite a data da última atualização:\n"),
                input("Digite a descrição:\n"),
                input("Digite o departamento:\n")]
            resp = input("Digite <S> para continuar ou <N> para sair\n").upper()

        with open("inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json)
        print("JSON gerado!!!!")

    elif opcao == 2:
        for chave, dado in resultado.items():
            print(f"Data.........:{dado[0]}")
            print(f"Descrição....: {dado[1]}")
            print(f"Departamento.: {dado[2]}")
    opcao = int(input("Digite:\n"
                      "< 1 > para registrar ativo\n"
                      "< 2 > para exibir ativos armazenados\n"
                      "< 3 > Para sair:\n"))

"""
Mas e se o arquivo não existir ou já existir, não queremos sobrescrever dados importantes certo?? então teremos que 
importar outra biblioteca, "os" (Operation System), que permite acessar objetos e funções referentes ao sistema 
operacional, uma dessas funções é o path.exists(), que retorna um true caso encontre o arquivo especificado como parametro,
ou false se não for encontrado, vamos colocar: 
"""
# os para verificar arquivos
import os


if os.path.exists("inventario_json.json"):
    with open("inventario_json.json", "r") as arq_json:
        inventario = json.load(arq_json)
else:
    inventario = {}
opcao = int(input("Digite:\n"
                  "< 1 > para registrar ativo\n"
                  "< 2 > para exibir ativos armazenados\n"
                  "< 3 > Para sair:\n"))
"""
Foi tranquilo, é uma verificação como as que já vimos antes certo, apenas com objetivos diferentes, agora vamos criar as
funções para facilitar nossas vidas, então vamos criar um arquivo que vou chamar de funcoesJSON.py
"""
