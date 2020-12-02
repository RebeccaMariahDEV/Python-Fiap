"""
Dicionários são listas mais organizadas, pois são divididos entre chave : valor, são delimitados com {}
diferente de sets( ainda vou explicar isso), não é difícil criar um dicionário e atribuir valores dentro dele,
basta saber o que queremos usar e como

ex: dicionário = {"chave": "valor"}, a chave geralmente usamos str, pois queremos deixar explícito o que estamos atribuindo,
porém pode ser int; já o valor pode ser qualquer tipo de dados como: int, str, float, lista, tupla( vou falar sobre elas
depois), sets ou outro dict(dicionário).
"""

# Dicionario para monitoramento de sistemas (é um exemplo)

usuarios = {"usuario1": ["Antonio Carlos", "24/11/2020", "admin_venda"],
            "usuario2": ["Cacau Mussi", "21/11/2020", "comida_gato"]}

print(usuarios)

"""
Relaxa, vou explicar.
Aqui é um exemplo de dicionários de monitoramento, primeiro temos o usuario1 com a lista de dados sobre ele, o nome,
dia do último acesso e onde ele acessou, depois o usuario2 seguindo a mesma lógica.

O print mostra tudo que tem dentro do nosso dicionário.

Podemos alterar uma informação do usuario, ou adicionar alguém também
"""

# Criando um usuario
usuarios["usuario3"] = ["Luke Lima", "23/11/2020", "adocao_pets"]

print(usuarios)

"""
Prontinho, criamos mais um usuario
Porem ainda na mão, mas se não souber como criar assim, não adianta saber mais além, assim como listas podemos remover
algo, ou só um valor; podemos pegar um usuario específico também usando o .get() dentro a chave do usuario que quer, porem
se passarmos uma chave que não existe ele nos retornará None, palavra reservada em python para não existe ou é algo vazio
"""
# Pegando um usuario

print(usuarios.get("usuario3"))

# Remover algo

usuarios.pop("usuario1")
print(usuarios)

usuarios.popitem()

"""
.pop() remove o ultimo se não tiver um parametro dentro, caso tenha ele vai remover o que quis dizer, porem dentro
ainda esta salvo o que removeu

Ainda podemos usar outros métodos em dicionários, por exemplo e se não soubermos o que tem dentro?
- .items() vai retornar os itens de dentro do seu dicionário
- .key() vai mostrar as chaves do dicionário
- .values() os valores das chaves, apenas os valores
- .clear() ele limpa o dicionário
- .popitem() remove somente um item e vc pode manipular essa informação atribuindo a uma variavel

Lembrando, os métodos são importantes e na duvida use a documentação

# Tuplas

Tuplas são delimitadas por (), são como listas, podem ter vários dados dentro, porem seu diferencial é que são imutáveis,
ou seja, não podemos alterar uma tupla; nem todos os métodos podem ser usados em tuplas, porem quando queremos um resultado
ele pode retornar em formas de tupla

Assim como mudamos um dado int para str(dado), podemos criar com list(), tuple(), dict(), set() ...
"""

# Dados com tupla

usuarios = {}
emails = ["gmail@gmail.com", "hotmail@hotmail.com"]

tupla = list(enumerate(emails))

print(tupla) # retorna uma lista de tuplas, sempre começando com indice 0

for chave in range(0, len(tupla)):
    print(f"Email: {tupla[chave][1]}")
    usuarios[tupla[chave]] = [input("Digite um email "), input("Digite o nivel ")]

for chave, dados in usuarios.items():
    print(f"Usuario : {chave[0]}")
    print(f"Email : {chave[1]}")
    print(f"Nome: {dados[0]}")
    print(f"Nivel : {dados[1]}")

"""
no primeiro print mostra o número do usuario, no segundo o email dele, por isso chave com indice [0] e o [1],
no terceiro mostra o email do usuario 0, então dados[0] e a autorização dele dados[1], ao fim dividi tudo o que temos na
tupla em 4 componentes para cada usuario

Está confuso, vou procurar melhorar

Porem tem uma curiosidade, se tentarmos atribuir um valor para uma variavel já inicializada, assim que um novo valor for
atribuído essa variavel vai ser sobrescrita, o mesmo vai acontecer em um dicionário, se tentarmos usar uma chave já usada
e passar novos atributos para ela, ele não vai salvar como se as duas fossem diferentes, ele vai sobrescrever, por isso
devemos tomar o maior cuidado para não acontecer isso.
"""
