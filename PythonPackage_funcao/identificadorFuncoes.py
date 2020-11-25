"""
Agora temos um pacote python, ele poderá ser usado e chamado em outros projetos no futuro, aqui coloquei nossas funções
anteriores, usaremos ela no futuro.

Não falei de um arquivo que temos dentro do nosso pacote, ele é o __init__.py, bem basicamente é nele que fica as
Funções para uso interno do python, mas não precisamos dele ainda

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


# repare como esta escrito cada bloco de funções, umas tem print outra não, elas seguem o que disse a cima.
# A função depreciarPorNome recebe dois parametros, podem receber N parametros obrigatorios ou não

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

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")

    for elemento in lista:

        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])