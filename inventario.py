"""
Bem antes vamos explicar como criar a partir de tudo que vimos até agora, com uma aplicação pratica que, com certeza
fará parte das nossas vidas no futuro. Vamos começar armazenando os seguintes dados: o número patrimonial do ativo,
a descrição do ativo, data da última atualização e o nome do departamento em que está localizado. Primeiro vamos definir
uma estrutura de dados para armazená-los; eles serão recebidos pelo colaborador responsável por catalogar os ativos e
então, persistiremos os dados para um arquivo, para que possam ser recuperados, 'backupeados', alterados, excluídos e
estejam disponíveis para qualquer outra consulta.

Utilizaremos uma estrutura de dicionário para armazená-los enquanto estiverem na condição de dados voláteis, em que o
número patrimonial será único, sobre essa chave teremos uma lista do departamento, data de atualização e descrição;
após a gerencia dos dados, iremos persistir em um arquivo CSV (representa um padrão que pode ser aberto em um Excel ou
em outros programas, garantindo uma maior flexibilidade e portabilidade sobre os dados), vamos pro código:
"""

# inventario
inventario = {}
opcao = int(input("Digite:\n"
                  "<1> para registrar ativo\n"
                  "<2> para persistir em arquivo\n"
                  "<3> para exibir ativos armazenados\n"
                  "<4> para sair:\n"))
while opcao > 0 and opcao < 4:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial:\n")] = [
                input("Digite a data da última atualização:\n"),
                input("Digite a descrição:\n"),
                input("Digite o departamento:\n")]
            resp = input("Digite <S> para continuar ou <N> para sair.\n").upper()

    elif opcao == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(f"{chave}; {valor[0]}; {valor[1]}; {valor[2]}" + "\n")
                print("Persistido com sucesso!")

    elif opcao == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())
    opcao = int(input("Digite:\n"
                      "<1> para registrar ativo\n"
                      "<2> para persistir em arquivo\n"
                      "<3> para exibir ativos armazenados\n"
                      "<4> para sair:\n"))

print("Fim do programa")

"""
Aqui criamos um dicionário,  nele montamos um menu de escolhas, enquanto o usuario digitar algo o programa continuar até 
ele digitar 4, se o valor for 1 iremos colocar o usuário em uma laço while, enquanto for S será permitido adicionar
itens, valor 2 abriremos o arquivo inventario.csv em modo de concatenação, então para cada objeto encontrado no nosso 
dicionário, iremos adicionar uma linha no arquivo, nessa linha terá a chave e os valores dessa chave separados por ';' ,
valor for 3, então abriremos o arquivo em modo de leitura e utilizaremos o método readlines() para exibir todo conteúdo.

Podemos melhorar o código, colocar validações, criar funções apara partes de códigos repetido, criar classes e por ai 
vai, tenta abrir depois em um Excel também, para ver como os dados foram persistido; vamos criar outros dois scripts, um
será o principal e o outro com as nossas funções, eu criei o funcoesInventario.py para as funções e vou usar aqui como 
principal para chamar as funções, lembrando que tem que importar
"""

from funcoesInventario import *

inventario = {}
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)

    elif opcao == 3:
        print(exibir())
    opcao = chamarMenu()

"""
Agora o nosso código se tornou mais simples e de fácil manuseio, uma atenção para a linha do método exibir(), esta 
dentro de um print para mostrar o que tem nela, podemos melhorar, aprimorar e modificar o código conforme a nossa 
necessidade, agora vai de cada um.

Até breve. 
"""
