"""
Até o momento, nossos dados só existem enquanto o sistema estiver aberto e/ou a sua estrutura não fosse limpa ou
sobrescrita; a partir de agora vamos ver como deixar os nossos dados salvas e como retornar dados em JSON, que é um tipo
de estrutura de dados diferente, eles vão existir fisicamente o que nos permite passar os dados de uma máquina para outra,
 ou até mesmo atualizar  um sistema por meio de instruções encontradas em arquivos gerados por outros.

# Manipulação de arquivos

Para começarmos a manipular arquivos utilizamos algumas funções, a open() permite várias ações:

- open("<caminhoDoArquivo><nomeDoArquivo>", "w") => indica que estamos abrindo um arquivo para o modo de escrita
(w => write), permitindo assim escrever nele, caso o arquivo já exista ele será sobrescrito.

- open("<caminhoDoArquivo><nomeDoArquivo>", "r") => com a letra "r" (read) no segundo parametro da função, podemos abrir
o arquivo para leitura, permitindo assim outra pessoa ler em outro computador, ter acesso aos dados contido nesse arquivo,
porém sem mexer ou alterar nada, como emprestar um livro a alguém.

-  open("<caminhoDoArquivo><nomeDoArquivo>", "a") => dessa forma você pode ler e escrever no arquivo, como um diário,
acresentando conteudos de acordo com algum evento, sempre ao final do diário, a ideia é concatenar os dados, por isso a
letra "a" referindo-se a append(anexar).

- open("<caminhoDoArquivo><nomeDoArquivo>", "x") => permite criar um novo arquivo em modo exclusivo, uma vez que você
criou/abriu o arquivo, ninguém mais poderá abri-lo, caso tente abrir um arquivo já existente será retornado uma falha.

- open("<caminhoDoArquivo><nomeDoArquivo>", "t") => o arquivo que for aberto com parametro "t" (text/texto) irá retornar
para o python o seu conteúdo como string, diferente do parametro "b", que retorna os dados em formato binário e exigiria
uma conversão para string, caso fosse necessário

Podemos combinar os modos com as ações por exemplo: "w+b" ou "wb". (lembrando que o b é transformar o arquivo em binário)

Mão na massa agora:
"""

# Open()

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""
Para um primeiro teste apresenta a função  open() junto com o comando with por meio de 'alias', nos permite também abrir
 e fechar o arquivo sem precisar do close(), assim como vimos em outros blocos o with é um bloco de comando identado, 
usamos o 'as' tanana para pôr um nome mais fácil ao nosso arquivo, para utilizarmos durante o código.

Perceba que no parametro do caminho do código colocamos apenas o nome dele, sem falar exatamente onde está, isso indica 
que o python irá considerar o caminho do código-fonte, eu antes de abrir o arquivo tive que criar ele, para não dar 
erro, se tentar acessar algo que não existe o python dará um erro de:
 FileNotFoundError: [Errno 2] No such file or directory: 'teste.txt' (copiei esse erro)
Coloquei o print() para que conseguíssemos ler o arquivo, se não ele roda porem não mostra nada, também coloquei um texto
simples para ler, ex: oi tudo bem?
"""

# Vamos alterar o teste.txt para teste2.txt sem o criar antes ok

with open("teste2.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")
    print(arquivo)

"""
Aqui temos duas coisas para mostrar:
- Alteramos o parametro "r" para "w", o arquivo será aberto para escrita e não leitura.
- dentro do with não estamos mais utilizando o método read() e, sim, o método write(), que nos permite passar o 
conteúdo que queremos para dentro do arquivo.

Porem temos mais algumas coisas para ver alem desses dois pontos, quando rodamos o script retorna algo como:
<_io.TextIOWrapper name='teste2.txt' mode='w' encoding='cp1252'>, isso é onde está salvo o nosso arquivo, não mostra como
leitura por não ter o read(), também criamos esse novo arquivo a partir do "w", se trocar o texto tu vai sobrescrever o
arquivo, o nosso arquivo pode estar estranho quando abrimos ou não, porem se estivar é só mudar as configurações, clique
em reaload in another encoding e opte pela opção windows-1252 ou iso-8859-1.

vamos mostrar um exemplo de como abrir um arquivo e concatenar com o que já tinha nele
"""

# Arquivo com "a"

with open("teste2.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto, vamos ver  o que gera")
    print(arquivo)

"""
Agora vamos escrever ou arquivo html ( se não sabe o que é html tudo bem, é uma linguagem de script para frontend, pode
pesquisar no google como criar e usar depois), mas eu vou deixar o exemplo aqui, é só para ter noção exata do quão importante
poder ser a geração de um arquivo dentro de uma linguagem.
"""

# Arquivo HTML

with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Esta é um teste para página WEB </h1>\n")
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:\n  </h2>")
    pagina.write("<h3>\n")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR:\n ").upper()
        if nome != "SAIR":
            pagina.write("\n<br>" + nome)
    pagina.write("\n</h3></body>")
    print(pagina)

# Executa, responde e veja o que tem no seu novo arquivo, você irá gostar do que você mesmo criou.
# Refatorar nosso teste.txt combinando métodos

with open("teste.txt", "r+b") as arquivo:
    conteudo = arquivo.read()
print(f"Tipo de dado da variável {type(conteudo)}")
print(f"Conteúdo do arquivo: {conteudo}")

"""
Aqui analisamos algumas coisas, o r+b é para escrever em bytes, tanto que ele retorna o tipo bytes porem ainda está em 
texto e tudo bem, era apenas para mostrar o método combinado, lembra que acima mostrei quais métodos podemos usar, na 
dúvida pode consultar a documentação do python sempre que quiser.

Podemos usar outro método, vamos utilizar agora o readlines(), veja o que retorna usando o mesmo código:
"""

# readlines()
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)

"""
A saída não é mais uma string, agora é uma lista, o readlines() é muito útil quando optamos por quebrar um grande 
arquivo em partes, para que possamos retirar somente os dados que nos interessarem, vamos mostrar isso em um método 
pratico que tal?!
 pra isso vamos criar um novo arquivo, inventario.py ok, até lá
"""
