"""
Vamos mudar e alterar o inventario que criamos, de modo que seja mais fácil a sua utilização no futuro, também vamos
usar o slice() que é um método para manipular string, onde utilizamos ex: linha[2:-1], pode ser usado em uma variavel
ou direto em um print.

vamos ao código, nele também criaremos um meio de mostrar linha por linha e não listas todas em uma linha única, também
não queremos ter o número do patrimônio em todos os ativos, apenas mostrar eles, ninguém vai no mercado e procura um
produto por código de barras né kkkk.
"""
# refatorando o inventario

from funcoesInventario import *

inventario = {}
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            print(linha[2:-1])
    opcao = chamarMenu()

"""
Método find(), rfind() e split():

- find() também é utilizado com string, permite que você encontre um caractere e/ou uma parte de string (conjunto de 
caracteres), retornando a posição da primeira incidência encontrada; por ex: caso tenhamos uma string 'Becca' e 
executamos um comando como: 'Becca'.find('c') ele retornar o valor 2, pois a primeira vogal 'c' que se encontra na 
posição 2, assim com o código a baixo acontecerá o mesmo, ele tambem faz a leitura da esquerda para a direita.
- rfind() tem o mesmo objetivo do find() porem sua leitura é da direita para a esquerda.

- split() ele quebra um string de acordo com um conjunto de caracteres que você pode definir, se olharmos para o conteudo
da variavel linha percebemos que nossos dados são separados por ';' (importante não separar os dados por um simbolo 
comum). A função split() irá gerar uma lista e em cada posição teremos uma parte da string, de acordo com a quebra foi
proposta. 

"""
# Ficara assim com find():

inventario = {}
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            print(linha[linha.find(";") + 1:-1])
    opcao = chamarMenu()

"""
Roda o código, veja como o resultado ficou mais claro e limpinho, o que achou?
Porem podemos separar melhor os resultados ainda, vamos separar linha por linha que tal???
"""

# Fica assim com rfind():

inventario = {}
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            separacao = linha[linha.find(";") + 1:-1]
            data = separacao[0:separacao.find(";")]
            separacao = separacao[separacao.find(";") + 1:-1]
            descricao = separacao[0:separacao.find(";")]
            departamento = linha[linha.rfind(";") + 1:-1]
            print(f"Data.........: {data}")
            print(f"Descrição....: {descricao}")
            print(f"Departamento.: {departamento}")

    opcao = chamarMenu()
"""
Agora quando termos o retorno dos dados ficou mais bonito né.
Eu não lembro se comentei sobre F string, é um modo de impressão mais bunito e moderno em python, vou explicar oque é:
- A partir do Python 3.6, f-strings são uma ótima maneira de formatar strings. Além de serem mais legíveis, mais 
concisos e menos sujeitos a erros do que outras formas de formatação, eles também são mais rápidos!
Como as f-strings são avaliadas em tempo de execução, você pode colocar qualquer e todas as expressões Python válidas 
nelas. Isso permite que você faça algumas coisas interessantes.

Podemos usar em um return f"{variavel}", direto em um print, dentro de outra variavel, junto com métodos e por ai vai. 
"""
# Fica assim com split()

inventario = {}
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print(f"Data.........: {data}")
            print(f"Descrição....: {descricao}")
            print(f"Departamento.: {departamento}")
    opcao = chamarMenu()

"""
Rode o código para ver como ficou mais legível, compare com as outras, veja as diferenças, qual se tornou mais pratica,
sempre que manipular strings terá n maneiras de fazer, se ver que está ficando muito grande o código você pode procurar
um método capaz de simplificar o que você deseja, as vezes não tem como mas ai ok kkkk.
"""
