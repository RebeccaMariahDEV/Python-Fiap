"""
Dicionarios são listas mais organizadas, pois são dividodos entre chave : valor, são delimitados com {}
diferente de sets( ainda vou explicar isso), não é dificil criar um dicionario e atribuir valores dentro dele,
basta saber o que queremos usar e como

ex: dicionari = {"chave": "valor"}, a chave geralmente usamos str, pois queremos deixar explicito o que estamos atribuindo,
porem oide ser int; já o valor pode ser qualquer tipo de dados como: int, str, float, lista, tupla( vou falar sobre elas
depois), sets ou outro dict(dicionario).


"""

# Dicionario para monitoramento de sistemas (é um exemplo)

usuarios = {"usuario1": ["Antonio Carlos", "24/11/2020", "admin_venda"],
            "usuario2": ["Cacau Mussi", "21/11/2020", "comida_gato"]}

print(usuarios)

"""
Relaxa, vou explicar.
Aqui é um exemplo de dicionarios de monitoramento, primeiro temos o usuario1 com a lista de dados sobre ele, o nome,
dia do ultimo acesso e onde ele acessou, depois o usuario2 seguindo a mesma logica.

O print mostra tudo que tem dentro do nosso dicionario

Podemos alterar uma informação do usuario, ou adicionar alguem tambem

"""

# Criando um usuario
usuarios["usuario3"] = ["Luke Lima", "23/11/2020", "adocao_pets"]

print(usuarios)

"""
Prontinho, criamos mais um usuario
Porem ainda na mão, mas se não souber como criar assim, não adianta saber mais alem, assim como listas podemos remover
algo, ou só um valor; podemos pegar um usuario específico tambem usando o .get() dentro a chave do usuario que quer

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

Ainda podemos usar outros metodos em dicionarios, por exemplo e se não soubermos o que tem dentro?
- .items() vai retornar os itens de dentro do seu dicionario
- .key() vai mostrar as chaves do dicionario
- .values() os valores das chaves, apenas os valores
- .clear() ele limpa o dicionario
- .popitem() remove somente um item e vc pode manipular essa informação atribuindo a uma variavel

Lembrando, os métodos são importantes e na duvida use a documentação

# Tuplas

Tuplas são delimitadas por (), são como listas, podem ter varios dados dentro, porem seu diferencial é que são imutaveis,
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
no primeiro print mostra o numero do usuario, no segundo o email dele, por isso chave com indice [0] e o [1],
no terceiro mostra o email do usuario 0, então dados[0] e a autorização dele dados[1], ao fim dividi tudo o que temos na
tupla em 4 componentes para cada usuario

ESta confuso, vou procurar melhorar

"""
