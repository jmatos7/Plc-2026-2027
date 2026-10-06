# 📝 TPC 2 — Conversor de Markdown para HTML

**### 📌 Enunciado**

Criar em Python um pequeno conversor de Markdown para HTML que processe os elementos básicos da "Basic Syntax": Cabeçalhos, Bold, Itálico, Listas numeradas, Links e Imagens.

---

**### ✏️ Resolução**

* [TPC 2 — Conversor de Markdown para HTML](MarkDown_To_HTML.py)

O conversor foi desenvolvido em Python utilizando o módulo `re` para reconhecer os diferentes elementos de Markdown através de expressões regulares e convertê-los para as respetivas tags HTML.

---

**### 💡 Funcionalidades**

* **Cabeçalhos:** reconhece linhas iniciadas por `#`, `##` ou `###` e converte-as para `<h1>`, `<h2>` e `<h3>`.

* **Bold:** reconhece texto entre `**` e converte-o para `<b>`.

* **Itálico:** reconhece texto entre `*` e converte-o para `<i>`.

* **Listas numeradas:** reconhece linhas iniciadas por um número seguido de `.`, agrupando os elementos numa lista `<ol>` com elementos `<li>`.

* **Links:** reconhece a estrutura `[texto](url)` e converte-a para uma tag `<a>`.

* **Imagens:** reconhece a estrutura `![texto alternativo](src)` e converte-a para uma tag `<img>`.

---

**### 🔎 Exemplos**

| Entrada (Markdown)                 | Saída (HTML)                                  |
| ---------------------------------- | --------------------------------------------- |
| `# Exemplo`                        | `<h1>Exemplo</h1>`                            |
| `## Exemplo`                       | `<h2>Exemplo</h2>`                            |
| `Este é um **exemplo**`            | `Este é um <b>exemplo</b>`                    |
| `Este é um *exemplo*`              | `Este é um <i>exemplo</i>`                    |
| `1. Primeiro item`                 | `<li>Primeiro item</li>`                      |
| `[página da UC](http://www.uc.pt)` | `<a href="http://www.uc.pt">página da UC</a>` |
| `![coelho](http://coelho.com)`     | `<img src="http://coelho.com" alt="coelho"/>` |

---

**### 🧪 Testes**

Foram utilizados **doctests** para verificar o funcionamento do conversor, testando os diferentes elementos de Markdown definidos no enunciado.

Os testes podem ser executados diretamente através do ficheiro `MarkDown_To_HTML.py`.
