# Aula 11 — Probabilidade condicional

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Calcular probabilidades simples e condicionais, aplicá-las em situações do cotidiano e de IA e interpretar distribuições. |
| **Objetos de conhecimento** | Probabilidade condicional. Tabelas de contingência. Independência. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** das regras da soma e do produto. |
| 55 min | **Aula expositiva:** probabilidade condicional; tabela cruzada; P(A\|B) ≠ P(B\|A). |
| 80 min | **Prática em Python:** tabela cruzada alerta × chuva; condicional por período. |
| 30 min | **Sistematização:** a “falácia da inversão” no caderno de bordo. |

## 2. Conteúdo

### 1. Mudando o espaço amostral

A **probabilidade condicional** de A dado B é a chance de A **sabendo que B ocorreu**. Restringimos o universo aos casos em que B aconteceu:

```text
P(A | B) = P(A e B) ÷ P(B)
```

Se A e B são independentes, P(A | B) = P(A). Portanto, comparar P(A | B) com P(A) é um **teste informal de independência**.

### 2. Tabela cruzada (de contingência)

| Alerta | Choveu | Não choveu | Total |
|---|---|---|---|
| alto | 61 | 64 | 125 |
| médio | 55 | 44 | 99 |
| baixo | 79 | 62 | 141 |
| **Total** | **195** | **170** | **365** |

> **📝 Exemplo resolvido: P(alto | choveu)**
>
> Entre os **195** dias com chuva, **61** tiveram alerta alto → P(alto | choveu) = 61 ÷ 195 = **0,3128**.
>
> Já P(choveu | alto) = 61 ÷ 125 = **0,4880**. São números **diferentes**, pois respondem a perguntas diferentes.

> **⚠️ Atenção: falácia da inversão**
>
> P(A | B) **não** é igual a P(B | A). “A maioria dos jogadores profissionais treina muito” não significa “a maioria de quem treina muito é profissional”. Em IA, esse erro aparece ao interpretar a “probabilidade de a doença dado o teste positivo” como “probabilidade do teste positivo dada a doença”.

### 3. Condicional por grupo

A chance de chover depende fortemente do período: P(choveu | enchente) = **0,755**; cheia = 0,446; seca = 0,475; vazante = **0,180**. Nos dados da enchente, chover é a regra; na vazante, é exceção.

## 3. Prática em Python

Monte a tabela cruzada com `pd.crosstab` e calcule as probabilidades condicionais.

- Script: [`aula_11.py`](aula_11.py)
- Notebook (Colab): [`aula_11.ipynb`](aula_11.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-11-probabilidade-condicional/aula_11.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `P(alto | choveu) = 0,3128` e `P(choveu | alto) = 0,4880` — não são iguais.
- `normalize="columns"` calcula a proporção **dentro** de cada coluna (condicional à chuva).
- A chance de chover varia de 18% (vazante) a 75,5% (enchente).

## 4. Atividades de fixação

1. Em uma urna há 4 bolas azuis e 6 vermelhas. Retiram-se duas bolas sem reposição. Qual a probabilidade de a segunda ser azul dado que a primeira foi azul?
2. Use a tabela cruzada do projeto e calcule P(alto | choveu) e P(choveu | alto).
3. Compare P(alto | choveu) com P(alto). Há indício de dependência?
4. Em qual período a chance de chover é maior? Qual é menor? Cite as probabilidades.
5. Explique, com um exemplo seu, por que P(A|B) ≠ P(B|A).

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Fórmula de P(A|B) e seu significado.
- [ ] Montar e ler tabela cruzada.
- [ ] Diferenciar P(A|B) e P(B|A).
- [ ] Usar P(A|B) vs P(A) como teste informal de independência.
- [ ] `pd.crosstab` e `normalize`.

---
[← Voltar ao índice](../../README.md)
