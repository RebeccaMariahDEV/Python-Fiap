"""
Aqui é onde vamos chamar nossa função para utilizar

Aqui vamos usar duas coisas novas o from e o import:

- from é de onde vamos chamar o script de funções que queremos usar
- import é qual a função desejamos usar desse nosso script
# Se usar * ele vai chamar todas as funções do script que chamamos

"""
from .PythonPackage_funcao.identificadorFuncoes import *


minhaLista = []

print("Preenchendo")

preencherInventario(minhaLista)
print("Exibindo")

exibirInventario(minhaLista)
print("Pesquisando")

localizarPorNome(minhaLista)
print("Alterando")

depreciarPorNome(minhaLista, 20)
print("Excluindo")
print(excluirPorSerial(minhaLista))

exibirInventario(minhaLista)
print("Resumindo")

resumirValores(minhaLista)

"""
Ficou um pouco confuso o modo como importei e como chamei né?! Mas ok vamos explicar

Em Python usamos algo.algo para chamar exatamente de onde queremos as funções pre criadas, porem tem outros meios de usar
ex: from PythonPackage_funcao import identificadorFuncoes, porem aqui deveremos usar 
identificadorFuncoes.oNomeDaFunçãoQueQueremos, assim usaremos uma função específica, já o * você usa o nome da função direto

Fica mais facil para ler não é mesmo?

O que devemos pensar é, se o nosso codigo esta muito extenso sera que não podemos criar um pacote e usar as funções em 
outro lugar?, isso facilitara a manutenção do código sem falar nas mudanças do código para inovar algo, e principalmente
a reutilização de códigos; podemos dividir tambem em classes, mas isso vai ficar um pouco mais para frente. 

"""
