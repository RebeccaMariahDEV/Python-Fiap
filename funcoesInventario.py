def chamarMenu():
    escolha = int(input("Digite:\n"
                        "<1> para registrar ativo\n"
                        "<2> para persistir em arquivo\n"
                        "<3> para exibir ativos armazenados\n"
                        "<4> para sair:\n"))
    return escolha


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial:\n")] = [
                input("Digite a data da última atualização:\n"),
                input("Digite a descrição:\n"),
                input("Digite o departamento:\n")]
        resp = input("Digite <S> para continuar ou <N> para sair.\n").upper()


def persistir(dicionario):
    with open("inventario2.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(f"{chave}; {valor[0]}; {valor[1]}; {valor[2]} \n")
    return "Persistido com sucesso"


def exibir():
    with open("inventario2.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas
