import json
import os


def chamarMenu():
    escolha = int(input("Digite:\n"
                        "< 1 > para registrar ativo\n"
                        "< 2 > para exibir ativos armazenados\n"
                        "< 3 > Para sair:\n"))
    return escolha


def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario


def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar ou <N> para sair\n").upper()
        gravar_arquivo(dicionario, arquivo)
    return "JSON gerado!!!!"


def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print(f"Data.........:{dado[0]}")
        print(f"Descrição....: {dado[1]}")
        print(f"Departamento.: {dado[2]}")

"""
Funções criadas, agora vamos criar um outro arquivo para chamar as funções, vou chamar de manipularJSON.py.
"""