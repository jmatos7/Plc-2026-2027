import re
import doctest


def markdown_to_html(markdown):
    """
    Converte Markdown para HTML.

    >>> markdown_to_html("# Exemplo")
    '<h1>Exemplo</h1>'

    >>> markdown_to_html("Este é um **exemplo** ...")
    'Este é um <b>exemplo</b> ...'

    >>> markdown_to_html("Este é um *exemplo* ...")
    'Este é um <i>exemplo</i> ...'

    >>> print(markdown_to_html("1. Primeiro item\\n2. Segundo item\\n3. Terceiro item"))
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>

    >>> markdown_to_html("Como pode ser consultado em [página da UC](http://www.uc.pt)")
    'Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>'

    >>> markdown_to_html("Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...")
    'Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...'
    """

    linhas = markdown.splitlines()
    resultado = []
    lista_aberta = False

    for linha in linhas:

        # Lista numerada
        lista = re.match(r"^\d+\.\s+(.+)$", linha)

        if lista:
            
            if not lista_aberta:

                resultado.append("<ol>")
                lista_aberta = True

            item = formatacao(lista.group(1))
            resultado.append(f"<li>{item}</li>")

        else:
            if lista_aberta:

                resultado.append("</ol>")
                lista_aberta = False

            # Cabeçalho
            titulo = re.match(r"^(#{1,3})\s+(.+)$", linha)

            if titulo:

                nivel = len(titulo.group(1))
                texto = formatacao(titulo.group(2))
                resultado.append(f"<h{nivel}>{texto}</h{nivel}>")

            else:
                # Texto normal
                resultado.append(formatacao(linha))

    if lista_aberta:
        resultado.append("</ol>")

    return "\n".join(resultado)


def formatacao(texto):
    """Aplica as formatações inline do Markdown."""

    # Imagens
    texto = re.sub(
        r"!\[([^\]]+)\]\(([^)]+)\)",
        r'<img src="\2" alt="\1"/>',
        texto
    )

    # Links
    texto = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        texto
    )

    # Bold
    texto = re.sub(
        r"\*\*([^*]+)\*\*",
        r"<b>\1</b>",
        texto
    )

    # Itálico
    texto = re.sub(
        r"\*([^*]+)\*",
        r"<i>\1</i>",
        texto
    )

    return texto


if __name__ == "__main__":
    doctest.testmod(verbose=True)