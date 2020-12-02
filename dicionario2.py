"""
Agora que sabemos como funciona um pouco da linguagem vamos aprofundar, vamos adicionar e remover dados do dicionário
através de perguntas, prontos???
"""

# Criando dicionario por perguntas

usuarios = {}
opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário:\n ").upper()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":

    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()

        usuarios[chave] = [nome, data, estacao]

    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário:\n ").upper()

"""
No código a cima temos as perguntas, porem percebe que esta faltando algo??

Lembra dos elifs? aqui temos várias decisões e vamos precisar deles para todas essas tomadas, também vemos uma variavel
que se repete em dois casos, podemos melhorar e refatorar isso certo?! Sim

Podemos mudar 5 linhas em duas diferentes, as perguntas ficariam assim:

obs: usar \n no código quebra a linha e vai para a próxima
"""

# Refatorando....

chave = input("Digite o login:\n ").upper()
usuarios[chave] = [input("Digite o nome:\n ").upper(),
                   input("Digite a última data de acesso:\n "),
                   input("Qual a última estação acessada: \n").upper()]

"""
Você deve estar se perguntando por que não substituir a chave direto por um input também, vou dizer, o python ele 
executa primeiro o que tem depois do =, e a chave se tornaria a última coisa a ser preenchida, então inicializei a variavel
antes, assim fica mais legível e fácil.
 
Porem vamos mostrar tudo em uma só, funciona, mas se sentir seguro pode criar com todas as variáveis, ou só uma ou
como quiser, não existe jeito exato. 
"""

usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                               input("Digite a última data de acesso: "),
                                               input("Qual a última estação acessada: ").upper()]

# Criando com funções, vai ficar melhor e mais bonito, se tivermos que reutilizae alguma parte é só chamar a função

def perguntar():
    resposta = input("O que deseja realizar?\n" +
                     "<I> - Para Inserir um usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para Listar um usuário:\n").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login:\n").upper()] = [input("Digite o nome:\n").upper(),
                                                      input("Digite a última data de acesso:\n"),
                                                      input("Qual a última estação acessada:\n").upper()]


"""
Aqui temos as perguntas dentro de cada função certo?! agora falta criarmos os dicionários utilizando as mesmas, não é 
complicado porem se quiser separar em outro script tudo bem, depois é só fazer um import como já vimos a pouco

Você verá um código mais limpo e enxuto, com pratica você irá criar já assim, porem eu ainda não consigo sem pensar e
desenhar (escrever) longo e mudar conforme vai indo, sem falar que ainda tenho erros e o google é meu melhor amigo kkkkk
"""

# Criando o dicionario

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = perguntar()

"""
Vamos para um desafio, você precisa criar funções para as outras opções que temos, que tal? topa essa???!!
Valendo em, se não conseguir tudo bem, estamos aprendendo, eu e você juntos.
"""

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)

    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)


"""
Nosso código ainda não está 100%, mas estamos no caminho certo.

O código acima é responsável por criar outras 3 funções:
- Na função pesquisar() precisamos receber o dicionário (onde se pretende pesquisar) e a chave(o dado que será 
pesquisado),
logo após vamos preencher uma lista com os resultados da pesquisa, usando a função get(); antes temos um if para ver se
a lista não está vazia, se for verdade ela mostra os dados, se não sai do if.

- Na função excluir() também recebemos o dicionário de onde o objeto será excluído e a chave do objeto a ser excluído,
antes de excluir verificamos também se a chave não está vazio, utilizando o get(), retornando algo diferente de vazio
ele irá excluir, usando o comando del mais o objeto por chave que excluímos

Não lembro se falei do del, mas ele é bem sugestivo por nome não é mesmo?!, del de delete, porem sempre temos que 
informar o que exatamente o que o del vai apagar

Agora vamos implementar todas as funções no nosso projeto:
"""
usuarios = {}

opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios, input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()

"""
Está tudo ai agora, bonito e funcionando, porem vamos ver alguns métodos para usar em dicionários:
- items() retorna os items do dicionário por lista separados por tuplas 
- valeus() retorna apenas os valores do dicionário sem as chaves
- keys() retorna as chaves do dicionário
- has_key() verifica se tem essa chave, voltando um True ou False
- clear() limpa o dicionário
- popitem() remove por um item
"""
