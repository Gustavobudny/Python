biblioteca = {
    "Dom Casmurro": {
        "autor": "Machado de Assis",
        "ano": 1899
    },
    "1984": {
        "autor": "George Orwell",
        "ano": 1949
    },
    "O Senhor dos Anéis": {
        "autor": "J.R.R. Tolkien",
        "ano": 1954
    }
}

titulo = input('digite o titulo do livro que voce deseja acessar: ')

if titulo in biblioteca:
    livro = biblioteca[titulo]
    print(f'autor: {livro['autor']}')
    print(f'ano: {livro['ano']}')
else:
    print('autor nao encontrado')

