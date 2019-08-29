produtos = [
    {'nome': 'produto1', 'valor': '1.0'},
    {'nome': 'produto2', 'valor': '2.0'},
    {'nome': 'produto3', 'valor': '3.0'},
    {'nome': 'produto4', 'valor': '4.0'},
]

try:
    for produto in produtos:
        produto['valor'] += produto['valor'] * 0.1
except KeyError as e:
    print('Chave não pertence ao produto {}'. format(e))
except Exception as e:
    print('Erro: {}'.format(e))
finally:
    print(produtos)