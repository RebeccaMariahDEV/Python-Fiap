from funcoesJSON import *

inventario = ler_arquivo("inventario_json.json")
opcao = chamarMenu()

while opcao > 0 and opcao < 3:
    if opcao == 1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao == 2:
        exibir("inventario_json.json")
    opcao = chamarMenu()
"""
Pronto, agora temos o nosso arquivo para usar as funções lindas que criamos, roda ele para você ver como criar, que tal
, podemos ver também que poderíamos passar o nome de qualquer arquivo que as funções se adaptariam. agora sim hein!!!

É muita coisa eu sei, ainda eu sou só uma estudante porem estamos aqui estudando juntos, se for necessário refaça os 
exemplos até entender a lógica e lembrar dos padrões e recursos para manipulação.

Tudo isso pode ser usado em vários ambientes, para segurança, criação de banco de dados, tabelas para clientes etc, 
suas ideias são o limite.
"""
