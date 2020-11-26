"""
Listas são delimitadas em [], em python isso é muito importante, pois temos outros tipos
dentro dela podemos colocar varios dados

Todas as listas podem ser inicializadas vazia ou com dados, e em uma lista pode ter varios tipos de dados

"""

# lista preenchida estaticamente
lista_estatica = ["xpto", True]

# lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), print("Digite 1 para sim e 0 para não"),
                  bool(int(input("Está logado? ")))]

# lista vazia
lista_vazia = []

# Adicionando dados em uma lista de maneira indeterminada

inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

# .append() é um metodo para adicionar algo em uma lista, podemos usar esse exemplo para criar uma lista básica de coisas

# Usando um FOR para imprimir o que tem dentro da nossa lista inventario

inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))  # podemos passar para str, para o código ter letras e numeros
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)

# Podemos criar uma lista para cada item, e adicionarmos varias coisas dentro tambem

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for equipamento in equipamentos:
    print("Equipamento: ", equipamento)

"""
Porem aqui ainda não esta do melhor jeito, vamos refatorar o código, com uma mudança, vamos colocar e chamar tudo por indice

Indice são as posições de cada dado ou elemento dentro de uma lista, mas pode ser usado em outros exemplos tambem.
como o indece de uma string, ou numero, valor ect; o indice sempre começa em 0, quando não sabemos qual o indice do ultimo
valor podemos acessar através de -1, assim retorna o ultimo valor

"""

# Lista com indece:

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

"""
Já se torna um metodo melhor, mais legivel e organizado, lembrando que é fundamental ter codigo limpo, isso é boas praticas 

len() função interna do python para contar o numero de indices, caracteres e outros dados, pode ser dentro de uma lista
ou em outros tipos

"""

# Exemplo de buscas com listas, ainda usando o exemplo acima com a junção do exemplo a baixo

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for indice in range(0, len(equipamentos)):

    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])

# isso ira gerar uma busca a partir da lista do nome do equipamento

# Desafio de listas

'''
Situação 1: 
todos os equipamentos "Impressora" terar um desconto de 10% depois de determinado periodo.
Monte um codigo que sera responsavel por dar esse desconto e alterar todos os valores de "impressora"

Situação 2:
Um equipamento com determinado numero serial foi danificado e sera descartado.
Precisamos eliminar esse equipamento . DICA: para eliminar um item de uma lista podemos usar o comando "del"
Exemplo: del lista[<indice>]

'''
# Exemplo situação 1:

depreciacao = input("Digite o nome do equipamento que será depreciado:\n ")

for indice in range(0, len(equipamentos)):

    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

# Não existe metodo exato para resolver algo, se conseguir resolver esta certo!

# Exemplo situação 2:

serial = int(input("\nDigite o serial do equipamento que será excluido: "))

for indice in range(0, len(departamentos)):

    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

"""
Aqui usamos um break, ele serve para parar uma algo, no caso o nosso FOR pois no final queremos sair do if e gerar algo novo

existe outros meios de remover ou deletar algo de uma lista, na duvida pesquise ou veja a documentação do Python

"""

# Listas dentro de listas, assim como if's podemos usar listas encadeadas

inventario = []
resposta = "S"

while resposta == "S":
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for elemento in inventario:

    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")

for elemento in inventario:

    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial = int(input("\nDigite o serial do equipamento que será excluído: "))

for elemento in inventario:

    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

'''
A cada vez que passa vemos que podemos usar tudo que aprendemos aqui, um codigo por um todo é assim tambem,
Aqui estamos criando uma lista dentro de outra para organizar, mais no futuro veremos um outro exemplo de fazer isso de 
modo mmais claro e melhor, antes temos que entender como criar e manipular dados em lista

A cima usamos mais um metodo do python:
.remove() é para remover/ deletar algo de uma lista, sendo tambem usado em outros modos, dentro dos parentes é onde passaremos
exatamente o que queremos remover

Usar listas dentro de listas pode parecer assustador, mas isso evita erros e evita que mostre um dado errado, tambem em 
determinadas situações será muito importante o uso de listas assim, já que toda aplicação que criamos tem que ser a mais
segura e exata possivel, sempre tentando prever os possiveis erros do usuario para não bugar seu codigo

'''

# Funções para lista numericas

valores = []

for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))

"""
Aqui usamos 3 coisas novas que os nomes já explica o que é:

Max() retorna o maior valor
Min() retorna o menor valor
sum() soma os valores, porem lembrando que ela só pode ser usada em numeros

Max e Min pode ser usado em praticamente qualquer dado 

Existe varios metodos que podemos usar, porem para saber você pode usar um dir direto em um terminal python ex:
dir(list), ele retornara todos os metodos para usar em listas

"""
