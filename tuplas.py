"""
Recapitulando tuplas:

Tuplas são delimitadas por (), são como listas, podem ter vários dados dentro, porem seu diferencial é que são imutáveis,
ou seja, não podemos alterar uma tupla; nem todos os métodos podem ser usados em tuplas, porem quando queremos um resultado
ele pode retornar em formas de tupla

Tuplas não aceitam alterações sobre os dados já inserido nela, mesmo não sendo muito utilizadas em programas devemos saber
como usar e manipular, por exemplo, tuplas podem ser chaves de um dicionário, pois as chaves não vão mudar; vou explicar
exemplo, se temos um dado na chave que são dois dados isso daria um erro, porem se for uma tupla contendo esses dados ai ok.

Confuso? mas vou tentar melhorar
"""

# utilizando tupas para respostas

ips = {}
resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octetos:\n "),
         input("Digite os dois últimos octetos:\n "))] = input("Nome da máquina:\n ")
    resp = input("Digite <S> para continuar:\n ").upper()

"""
Vamos ver o código, criamos um dicionário chamado ips. uma variavel chamada resp para controlar nosso laço e, 
dentro do laço de repetição, vamos preencher o nosso dicionário, porem na chave tem dois valores, a primeira parte do 
ip e a segunda dentro de uma tupla, e o dado do elemento que está sendo adicionado.

Agora vamos aproveitar esse código, printando ele
"""

print("Exibindo ip´s: ")

for ip in ips.keys():
    print(f"{ip[0]}.{ip[1]}")

"""
Unimos as duas partes através do indice, ele vai colocar exatamente cada dado nesses posições.

Agora vamos criar algo que só pegue os ip's de maquinas que estão no mesmo local e não os nomes das maquinas.
"""

print("Exibindo máquinas com o mesmo endereço:\n")

pesquisa = input("Digite os dois últimos octetos:\n")

for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if (ip[1] == pesquisa):
        print(nome)

"""
Veja que pegamos os dados através do .items(), já vimos o que ele faz em!, agora vamos ver quais maquinas compõem uma 
mesma rede, pra isso vamos nos basear nos dois primeiros octetos do ip, vamos tentar.
"""
print("Exibindo as máquinas que compõem uma mesma rede: ")

rede = input("Digite os dois primeiros octetos: ")

for ip, nome in ips.items():
    if (ip[0] == rede):
        print(nome)

"""
Até agora já conseguimos notar algumas coisas certo? já vimos como listas, tuplas e dicionários funcionam, o que devemos
fazer é saber o melhor momento de usar cada tipo de estrutura de dados, não devemos escolher um ou outro, temos que saber
tudo por um todo.

Outro exemplo é usarmos a função enumerete(), para listar cada dado dentro de algo, transformando eles em dicionários ou
em outras coisas 
"""
usuarios = {}
resp = "S"
emails = []

while resp == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

# Usando o método enumerate(), para cada email ter um numero e retornar o resultado tupla em lista

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível")]

# Transformando os dados atuais para o usuario final

for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])

"""
Até o momento a maior preocupação foi te mostrar as estruturas de dados básicas, como manipular e utilizar esses recursos,
com esse básico você desenvolve algo, mas agora vem o divisor de águas, aqui vai ser o momento de se tornar algo a mais,
então estude bastante, treine o que foi feito até agora, se precisar veja a documentação do python.

O próximo passo é banco de dados, aprender a mexer e manipular é mais complicado, porem nada é um bicho de 7 cabeças ok.
"""
