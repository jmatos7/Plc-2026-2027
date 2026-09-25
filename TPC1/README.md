# 📝 TPC 1 — Expressão Regular
### 📌 Enunciado

Desenvolver uma expressão regular que reconheça strings binárias que não contenham a substring ``011``.

---

### ✏️ Resolução

- [TPC 1 — Expressão Regular](expressaoregular.txt)

Para testar a expressão em ferramentas como o [Regex101](https://regex101.com/), pode ser utilizada a seguinte versão:

^(1*(0|01)*)$

---

### 💡 Explicação 

Esta expressão é constituída por:

- 1* — permite zero ou mais 1s no início da string.
- (0|01)* — permite repetir 0s ou 01s 0 ou mais vezes.
- | — representa uma alternativa, ou seja, 0 ou 01.
- \* — significa que o elemento anterior pode aparecer zero ou mais vezes.

Desta forma, a expressão permite reconhecer strings binárias que não contêm a substring 011.

---

## 🔎 Exemplos

| ✅ Strings aceites | ❌ Strings rejeitadas |
|---|---|
| `0` | `011` |
| `1` | `0110` |
| `10` | `0011` |
| `101` | `1011` |
| `1001` | `11011` |
| `1010` | `1011010` |
| `1101` | `01000111` |
| `101010` |`11111000000111` |