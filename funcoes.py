"""
Funções
Até agora já usamos varias funções, são funções internas como : int, str, min, max, print, todas elas estão incorporadas
no PVM do python (Python Virtual Machine)

Em um código que já vimos vamos indentificar onde poderiamos criar funções:
"""
# identificando funções

inventario = []
resposta = "S"

# adicionar item no inventario
while resposta == "S":
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

# exibir dados do inventário
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# localizar um item no inventario
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for elemento in inventario:

    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

# depreciar itens no inventario
depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")

for elemento in inventario:

    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

# excluir um item do inventario
serial = int(input("\nDigite o serial do equipamento que será excluído: "))

for elemento in inventario:

    if elemento[2] == serial:
        inventario.remove(elemento)

# exibir dados do inventário
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# resumo de valores do inventário
valores = []

for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))

"""
Para criarmos uma função precisamos usar um comando def nomeFuncao():, esse é o modo de criar, lembra tudo que 
sabemos usar até aqui podemos usar dentro de uma função, ela é justamente para deixar seu código mais legível e 
organizável, é mais fácil ler um livro todo, sem o título para cada capítulo ou separado por capítulos?

Uma função pode ou não ter parâmetros, parâmetros são dados que ela vai precisar receber para funcionar corretamente,
se precisamos calcular um salário para aumento por exemplo, temos que saber o salário atual né, então a função vai 
receber esse salário como parametro.

Ao fim de uma função ele pode retornar algo ou não, isso vai do programa, para retornar algo usamos a palavra return,
porem dependendo você pode usar um print normal.

Para executar a função temos que chamar ela em algum lugar, se não ela nunca vai funcionar.
"""

# Funções para completar cada bloco que queremos criar, algo parecido oa que já usamos em listas

def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()


def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])


def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print("Novo valor: ", elemento[1])


# repare como está escrito cada bloco de funções, umas tem print outra não, elas seguem o que disse acima.
# A função depreciarPorNome recebe dois parâmetros, podem receber N parâmetros obrigatórios ou não

def excluirPorSerial(lista):
    serial = int(input("\nDigite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos."


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
