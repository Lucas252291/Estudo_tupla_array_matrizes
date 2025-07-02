import numpy as np


def imprimir_valor_questao(valor):
    print(f"{"-"*30}\nQuestão {valor}")
def formt():
    print(f"{"-"*30}")
# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho, 102 para verde e 0 para azul.
imprimir_valor_questao(1.1)
tupla_cor = (255,102,0)
print(tupla_cor)
formt()
# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.
imprimir_valor_questao(1.2)
tupla_cordenadas = (-8.0578,-34.8829)
print(tupla_cordenadas)
formt()
# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.
imprimir_valor_questao(1.3)
tupla_usuario = (101, 'ana_silva', '2023-01-15' )
print(tupla_usuario)
formt()
# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).
imprimir_valor_questao(1.4)
r,g,b = tupla_cor
print(f"cor r : {r}")
formt()
# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas latitude e longitude.
imprimir_valor_questao(1.5)
latitude, longitude = tupla_cordenadas
print(f"Latitude: {latitude}\nLongitude: {longitude}")
formt()


# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email), desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.
imprimir_valor_questao(1.6)
user_tupla = (205, 'Carlos Pereira', 'carlos.p@email.com')
id, nome , email = user_tupla

print(f"Seja bem vindo {nome} ao curso de programação ")
formt()


# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.
imprimir_valor_questao(1.7)
adm_tupla = ('moderador', 'editor', 'sysadmin')


for papeis in adm_tupla:
    print(f"Papeis adm:{papeis}")

formt()
# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.
imprimir_valor_questao(1.8)
for user in user_tupla:
    print(f"User: {user}")
formt()
# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.
imprimir_valor_questao(1.9)
for rgb in tupla_cor:
    print(f"RGB: {rgb}")

formt()

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.
imprimir_valor_questao(1.10)
def  administrador(papel):
    adms  = ('moderador', 'editor', 'sysadmin')
    
    for adm in adms:
        
        if papel == adm:
            return print(f"O papel {papel} é um adiministrador")
    
    return print(f"O papel {papel} não é um adiministrador")
            
administrador('moderador')
administrador('editor')
administrador('sysadmin')
administrador('lucas')

formt()
# 1.11 Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'), escreva uma função que conta o número de vezes em que um papel aparece, teste a função com os papíes 'editor', 'comentarista' e 'tradutor'..
imprimir_valor_questao(1.11)
def contador(papel):
    equipe = ('editor', 'leitor', 'editor', 'comentarista', 'editor')

    x = 0 

    for i in equipe:
        if i == papel:
            x+=1
    return x

print(f"Editor: {contador('editor')}")#'comentarista' e 'tradutor'..
print(f"Comentarista: {contador('comentarista')}")
print(f"Tradutor: {contador('tradutor')}")
print(f"leitor: {contador('leitor')}")
formt(),

# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.
imprimir_valor_questao(2.1)
usuario = {
    'username': 'bia_costa',
    'email' : 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
print(usuario)

formt()


# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 'estoque' com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.
imprimir_valor_questao(2.2)
produto = {
        'id_produto':'XYZ-001',
        'nome':'Fone de Ouvido Sem Fio',
        'preco': 299.90,
        'estoque':150

}
print(produto)

formt()
# 2.3 Crie um dicionário vazio chamado preferencias_usuario.
imprimir_valor_questao(2.3)
preferencias_usuario = {}
print(preferencias_usuario)
formt()

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. Em seguida, atualize o preço para o valor promocional de 249.99.
imprimir_valor_questao(2.4)
print(f"Preço orinal: R${produto['preco']}")
produto['preco'] = 249.99
print(f"Preço promocional: R$ {produto['preco']}")
formt()

# 2.5 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.
imprimir_valor_questao(2.5)
perfil_usuario =  {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}
print(f"Perfil de usuário: {perfil_usuario}")
perfil_usuario['telefone'] = '98765-4321'
print(f"Perfil de usuário atualizado: {perfil_usuario}")
formt()

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.
imprimir_valor_questao(2.6)
perfil_usuario = {'username': 'bia_costa'}
ultimo_login = perfil_usuario.get('ultimo_login', 'Nunca logou')
print(f"Último login: {ultimo_login}")
perfil_usuario['ultimo_login'] = '2024-05-22'
print(f"Perfil de usuário atualizado com último login: {perfil_usuario}")
formt()

# 2.7 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.
imprimir_valor_questao(2.7)
usuario = {'username':'bia_costa','email':'bia.costa@email.com','telefone_fixo':'3265-4321'}
print(f"Perfil de usuário antes da remoção: {usuario}")
del usuario['telefone_fixo']
print(f"Perfil de usuário após remoção: {usuario}")
formt()

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}, use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima uma mensagem de confirmação.
imprimir_valor_questao(2.8)
catalago_produtos = {'XYZ-001':'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}
print(f"Catálogo de produtos antes da remoção: {catalago_produtos}")
produto_removido = catalago_produtos.pop('XYZ-001')
print(f"Produto removido: {produto_removido}")
print(f"Catálogo de produtos após remoção: {catalago_produtos}")
formt()

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.
imprimir_valor_questao(2.9)
usuario = {'username': 'bia_costa'}
print(f"Usuario: {usuario}")
remover_email = usuario.pop('email','Email não encontrado.')
print(remover_email)
formt()

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.
imprimir_valor_questao(2.10)
catalago_produtos = {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}
print("O Catálogo de produtos é:")
for produto in catalago_produtos:
    print(f"{produto}: R${catalago_produtos[produto]}")

formt()

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.
imprimir_valor_questao(2.11)
compra_da_feira = {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}
valor_total = 0
print("A lista da compra é: ")
for produto in compra_da_feira:
    valor_total += compra_da_feira[produto]
    print(f"{produto} : R${compra_da_feira[produto]}")

formt()

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.
imprimir_valor_questao(2.12)
usuario = {'username': 'bia_costa'}
print(f"Usuario: {usuario}")
endereco = {'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo','cep': '01000-000'}
usuario['endereco'] = endereco
print(f"Usuario: {usuario}")

formt()

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'. O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.
imprimir_valor_questao(2.13)
usuario = {'username': 'bia_costa'}
print(f"Usuario: {usuario}")
usuario['profissao'] = {'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'}
print(f"Usuario: {usuario}")
formt()
# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas o valor associado à chave 'cidade'.
imprimir_valor_questao(2.14)
print(f"Usuario: {usuario}")
usuario['endereco'] = endereco
print(f"Usuario: {usuario}")
print(f"Cidade: {usuario['endereco']['cidade']}")

formt()
# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.
imprimir_valor_questao(2.15)
print(f"Usuario: {usuario}")
usuario['endereco']['rua'] = 'Avenida Principal, 456'
print(f"Usuario: {usuario}")

formt()
# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.
imprimir_valor_questao(2.16)
locais = {'Recife':(-8.0578, -34.8829), 'São Paulo' :(-23.5505, -46.6333) }
print(locais)


formt()
# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.
imprimir_valor_questao(2.17)
print(locais)
locais['Rio de Janeiro'] = (-22.9068, -43.1729)
print(locais)
formt()

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).
imprimir_valor_questao(2.18)
print(locais)

def encontra_cidade(x,y):
    for local in locais:
        cord = locais[local][:]
        if cord == (x, y):
            return print(f"Cordenadas: {x},{y} | Cidade : {local}")
    return  print(f"Cidade não encontrada aparti das cordenadas inseridas")

encontra_cidade(-23.5505, -46.6333)
encontra_cidade(0,0)
formt()
# Parte 3: Vetores (Listas e NumPy)
# 3.1 Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' ao final da lista.
imprimir_valor_questao(3.1)
lista_hashtags = {'tags_post':['#tecnologia', '#python', '#programacao']}
print(lista_hashtags)
lista_hashtags['tags_post'].append('#dados')
print(lista_hashtags)

formt()
# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], remova o elemento '#programacao'.
imprimir_valor_questao(3.2)
print(lista_hashtags)
lista_hashtags['tags_post'].remove('#programacao')
print(lista_hashtags)
formt()

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a string '#importante' existe na lista.
imprimir_valor_questao(3.3)
print(lista_hashtags)
if '#importante'in lista_hashtags['tags_post']:
    print("A hashtags #importante esta na lista")
else:
    print("A hashtags #importante não esta na lista")

formt()

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): [('camiseta', 10), ('calça', 5), ('sapato', 2)].
imprimir_valor_questao(3.4)

formt()
# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno: [0.85, 0.92, 0.78, 0.95, 0.88].
imprimir_valor_questao(3.5)

formt()
# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].
imprimir_valor_questao(3.6)

formt()
# 3.7 Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0), (Tênis, 150.0)]), crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).
imprimir_valor_questao(3.7)

formt()
# 3.8 Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.
imprimir_valor_questao(3.8)

formt()
# 3.9 Dados o array de quantidades quantidades = np.array([1, 2, 3]) e o array de preços unitários precos_unitarios = np.array([15.0, 30.0, 22.5]), calcule o valor total por item multiplicando os dois arrays.
imprimir_valor_questao(3.9)

formt()
# 3.10 Dado o array de temperaturas em Celsius temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]), converta todas as temperaturas para Fahrenheit usando a fórmula F = C * 1.8 + 32.
imprimir_valor_questao(3.10)

formt()
# Parte 4: Matrizes (NumPy)
# 4.1 Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas com os dados: 
# [0, 1, 3]
# [9, 7, 4]
# [2, 6, 6]
# [3, 3, 3].
imprimir_valor_questao(4.1)

formt()



# 4.2 Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) e sua transposta (atributo .T).
imprimir_valor_questao(4.2)

formt()
# 4.3 Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).
imprimir_valor_questao(4.3)

formt()
# 4.4 Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados para o segundo produto (linha de índice 1).
imprimir_valor_questao(4.4)

formt()
# 4.5 Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados para o terceiro mês (coluna de índice 2).
imprimir_valor_questao(4.5)

formt()
# 4.6 Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) no mês 2 (coluna 1).
imprimir_valor_questao(4.6)

formt()
# 4.7 Dada a matriz de preços matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]]), crie uma nova matriz com todos os preços aumentados em 5%.
imprimir_valor_questao(4.7)

formt()
# 4.8 Dadas as matrizes de vendas com a quantidade de vendas de 4 produtos nos primeiros 3 meses do ano, vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]]) e vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]]), some-as para criar uma matriz vendas_globais.
imprimir_valor_questao(4.8)

formt()
# 4.9 Dada a matriz de vendas vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) (3 produtos x 2 meses) e o vetor de preços precos = np.array([4.99, 5.25, 2.19]), calcule a receita total por mês usando o produto escalar (np.dot).
imprimir_valor_questao(4.9)

formt()
# 4.10 Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas em cada mês (soma ao longo do eixo 0).
imprimir_valor_questao(4.10)

formt()
# 4.11 Usando a mesma matriz de vendas, calcule a média de vendas para cada produto (média ao longo do eixo 1).
imprimir_valor_questao(4.11)

formt()
# 4.12 A partir da matriz de vendas, encontre e imprima o valor máximo.
imprimir_valor_questao(4.12)

formt()
# Parte 5: Desafios Finais
# Crie uma lista chamada usuarios contendo um dicionário para um usuário. Este dicionário deve ter: a chave 'id_usuario' com valor 101; a chave 'perfil' com um dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'}; a chave 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' com uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função registrar_login(usuario) que incremente o contador no mapa de calor do usuário correspondente ao dia e hora atuais.

# Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. A função deve retornar uma tupla contendo: 1. O valor total do inventário (soma de preco * estoque), 2. O nome do produto mais caro, e 3. Uma lista de produtos sem estoque. Teste a função com o catálogo: {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': {'preco': 250.00, 'estoque': 0}}.

# Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar um dicionário self.conexoes. Implemente os métodos adicionar_amizade(id1, id2) para criar uma amizade mútua e obter_amigos(id_usuario) para retornar a lista de amigos. Instancie a classe e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). Teste o método obter_amigos para os usuários 101, 205 e 999.

imprimir_valor_questao(5)

formt()








