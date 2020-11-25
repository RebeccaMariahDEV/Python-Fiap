"""
Variavel nada mais é que o nome dado para receber um valor, dado ou dados.
Em python é nome = o dado que quer

Tipos de dados:

- int (numeros inteiros)
- str (string são dados entre aspas simples ou duplas
- float (numeros com casa decimal)
Esses são os tipos basícos em qualquer lugar

"""

# Variaveis com atribuição de dados simples

nome = "Humberto Delgado"
empresa = 'FIAP'
qtde_funcionarios = 500
mediaMensalidade = 856.50

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

"""
Input() metodo interno do python para pedir um dado ao usuario, esse input é atribuido a uma variavel sempre

Na hora do printe podemos converter um dado para str, mas não é algo muito utilizado, tem outros meios de imprimir 
a variavel junto a str, porem tem outros meios para isso tambem

"""
# Dados atraves de inputs

nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

"""
Quando não sabemos exatamente que tipo de dado é o que temos usamos o type() para nos ajudar nessa missão
"""
# Type, mostra o tipo de dado que esta usando, ou o que é um dado x

nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))

"""
IF é uma pergunta literamente, ex: se uma maça for igual a uma maça faça um suco
Ele tambem pode ser composto de outras varias decições ex: se fruta for igual a maça como, 
e se fruta for igual a melancia faça suco, se não (não é fruta) não coma

"""

# IF condicional simples, usado para tomada de decisões diferentes

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "NÃO"

if idade >= 65:
    prioridade = "SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

# composta, o else não é obrigatorio porem fica explicito o que quer dizer no código

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")

"""
Não utilizar assim, sempre melhor criar ações compostas

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
if idade < 65:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
"""

"""
Verdadeiro ou falso, o famoso True ou False em programação, nada mais é que uma comparação booleana (bool)

O que é verdadeiro em booleano:
- str com qualquer coisa dentro
- int com o valor acima de 0
- float maior que 0.0
- algo igual a outro
- * algo maior ou maior igual a algo, caso seja verdade se não é Falso
- * algo menor ou menor igual a algo, caso seja verdade se não é Falso
- * algo diferente ou diferente igual a algo, caso seja verdade se não é Falso

O que é Falso em booleano:
- str vazia
- int com o valor 0
- float 0.0

"""

# Verdade ou Falso com condicionais

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")

# Não expliquei mas o .upper() coloca todas as letras que o usuario digitar em Maiúsculas

"""
And e Or são para comparar, verificar, ele retorna um True ou False o que faz as verificações das condicionais

ex: se banana = fruta e(and) banana = fruta faça isso
    retorna um verdadeiro e ai vai entrar no if/elif
    
    se banana = fruta ou(or) banana = gato, ele vai ver, um ou o outro tem que ser verdadeiro
    retorna um verdadeiro e ai vai entrar no if/elif
    
    Falso ele não entra e vai para o proximo if/ elif/ else
    
"""

# utilizando AND ou OR

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# Decisões Encadeadas: nada mais são que if's dentro de if's e por ai vai

'''
# Meio ok de usar porem

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")'''

# Porem tem um meio melhor de ser feito :

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")

elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para sala BRANCA")

else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()

    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()

        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")

"""
Podemos usar dentro de um if um input, pois caso a decisão seja x ele executa algo certo? até uma pergunta nova
"""

# Exemplo de decições com if e input dentro dele

nivel = input("Digite o nível de acesso: ").upper()

if nivel == "ADM" or nivel == "USR":
    genero = input("Digite o seu gênero: ").upper()

    if nivel == "ADM":

        if genero == "FEMININO":
            print("Olá administradora")

        else:
            print("Olá administrador")

    else:

        if genero == "FEMININO":
            print("Olá usuária")

        else:
            print("Olá usuário")

elif nivel == "GUEST":
    print("Olá visitante")

else:
    print("Olá desconhecido(a)")

"""
LOOP
São laços de repetições para executar n coisas ou 1
função interna do python que se repete N vezes ou até ser falsa

Temos dois tipos de loops:
- for
    ele roda por vezes limitadas, tem começo e fim
- while
    ele vai rodar enquanto a condição for verdadeira, se tornou falsa ele para
    
* AVISO:
  mas cuidado para não criar um loop infinitos com ele, ele vai acaabar com a memoria da sua maquina e travar o sistema

"""

# usando while

numero = int(input("Digite um numero: "))

while numero < 100:
    print("	" + str(numero))
    numero = numero + 1
    # podemos subistituir po numero += 1, porem o exemplo a cima fica mais explicito para o inicio de aprendizagem
print("Laço encerrado....")

# While com if, verificação de respostas

resposta = "SIM"

while resposta == "SIM":
    nivel = input("Digite o nível de acesso: ").upper()

    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu gênero: ").upper()

        if nivel == "ADM":
            if genero == "FEMININO":
                print("Olá administradora")

            else:
                print("Olá administrador")

        else:
            if genero == "FEMININO":
                print("Olá usuária")

            else:
                print("Olá usuario")

    elif nivel == "GUEST":
        print("Olá visitante")

    else:
        print("Olá desconhecido(a)")

    resposta = input("Digite SIM para continuar: ").upper()

# para o while parar é a resposta no final, se for não ele para, se for sim ele repete todas as perguntas novamente

# Operador diferente, ele é uma condição para ver se algo é diferente ou igual ao que se quer saber:

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")

else:
    genero = input("Digite o gênero do paciente: ").upper()

    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()

        if gravidez == "SIM":
            print("Paciente COM prioridade")

        else:
            print("Paciente SEM prioridade")

    else:
        print("Paciente SEM prioridade")

# For, laço de repetição limitada

for numero in range(1, int(input("Digite um numero para determinar o fim: ")), 1):
    print("	" + str(numero))

# Tabuada com For:

tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)

for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))
