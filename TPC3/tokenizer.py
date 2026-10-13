
import re


def tokenizer(query):
    reconhecidos = []
    linha = 1

    tokens = [
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),

        ('COMENTARIO', r'\#.*'),

        ('PALAVRA_RESERVADA', r'(?i:SELECT|WHERE|LIMIT)\b'),

        ('VAR', r'\?[a-zA-Z0-9]+'),

        ('LINGUA', r'@[a-zA-Z]{2}'),

        ('STRING', r'"[^"]*"'),

        ('NUM', r'\d+'),

        ('SINAL', r'[{}.]'),

        ('IDENT', r'[a-zA-Z0-9]+'),

        ('ERRO', r'.')
    ]

    token_regex = '|'.join(
        f'(?P<{nome}>{padrao})'
        for nome, padrao in tokens
    )

    for resultado in re.finditer(token_regex, query):
        tipo = resultado.lastgroup
        valor = resultado.group()

        if tipo == 'NEWLINE':
            linha += 1

        elif tipo in ('SKIP', 'COMENTARIO'):
            continue

        else:
            reconhecidos.append(
                (tipo, valor, linha, resultado.span())
            )

    print(reconhecidos)
    return reconhecidos


if __name__ == "__main__":
    query = """# DBPedia: obras de Chuck Berry
    SELECT ?nome ?desc WHERE {
        ?s a dbo:MusicalArtist.
        ?s foaf:name "Chuck Berry"@en .
        ?w dbo:artist ?s.
        ?w foaf:name ?nome.
        ?w dbo:abstract ?desc
    } LIMIT 1000
    """

    tokenizer(query)
