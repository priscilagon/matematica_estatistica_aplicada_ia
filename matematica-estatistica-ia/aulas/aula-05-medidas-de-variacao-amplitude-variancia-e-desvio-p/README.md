# Aula 5 — Medidas de variação: amplitude, variância e desvio-padrão

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Calcular e interpretar medidas descritivas e de variação, explicando o que significam no contexto do problema. |
| **Objetos de conhecimento** | Amplitude, variância, desvio-padrão (populacional e amostral). |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 20 min | **Retomada rápida** das medidas de tendência central. |
| 55 min | **Aula expositiva:** amplitude, variância e desvio-padrão como medidas de variabilidade; conexão com a ideia de “quão previsível” é o rio em cada período. |
| 75 min | **Prática em planilha e Python:** calcular as medidas por período hidrológico. |
| 30 min | **Sistematização:** texto interpretativo conjunto sobre a variabilidade encontrada. |

## 2. Conteúdo

### 1. Duas séries com a mesma média

Considere duas séries de cota, ambas com média 24 m: **A = 20, 22, 24, 26, 28** e **B = 24, 24, 24, 24, 24**. A média não distingue as duas. Falta uma medida de **quanto os valores se espalham**: a variação.

### 2. Amplitude

```text
amplitude = valor máximo − valor mínimo
```

É simples, mas depende só de dois valores — um atípico a distorce. Na série A, a amplitude é 28 − 20 = 8 m; em B, é 0.

### 3. Variância e desvio-padrão

A ideia: medir o quanto cada valor se afasta da média. Somar os desvios dá zero (positivos e negativos se anulam), então **elevamos ao quadrado**:

```text
SQ = Σ (xᵢ − média)²        (soma dos quadrados dos desvios)
```

|  | Fórmula | Divide por | Quando usar |
|---|---|---|---|
| Variância populacional (σ²) | SQ ÷ N | N | Os dados são **toda** a população de interesse |
| Variância amostral (s²) | SQ ÷ (n − 1) | n − 1 | Os dados são uma **amostra** que representa algo maior |

```text
desvio-padrão = √variância         (volta à unidade original: metros)
```

> **📌 Conceito-chave: por que n − 1?**
>
> A média da amostra é calculada **com os próprios dados**, o que faz os desvios parecerem menores do que são. Dividir por n − 1 compensa esse efeito (correção de Bessel) e torna a variância amostral um estimador **não viciado** da variância da população. Em amostras grandes, a diferença é pequena; em amostras pequenas, é relevante.

> **📝 Exemplo resolvido: série 18, 21, 21, 24, 26 (m)**
>
> **Média** = 110 ÷ 5 = 22 m.
>
> **Desvios (x − 22):** −4, −1, −1, +2, +4. **Quadrados:** 16, 1, 1, 4, 16 → **SQ = 38**.
>
> **Variância populacional:** 38 ÷ 5 = **7,6 m²**; **DP populacional** = √7,6 ≈ **2,7568 m**.
>
> **Variância amostral:** 38 ÷ 4 = **9,5 m²**; **DP amostral** = √9,5 ≈ **3,0822 m**.

A variância é medida em **unidade ao quadrado** (m²), o que dificulta a interpretação. Por isso, para **comunicar**, usamos o desvio-padrão (m).

### 4. Variação por período do rio

| Período | n | Amplitude (m) | DP amostral (m) |
|---|---|---|---|
| enchente | 151 | 17,80 | 3,303 |
| cheia | 92 | 2,22 | 0,594 |
| vazante | 61 | 17,70 | 3,181 |
| seca | 61 | 1,35 | 0,334 |

Cheia e seca têm DP de apenas 0,59 e 0,33 m: o rio é **muito previsível** nesses períodos. Enchente e vazante têm DP em torno de 3 m: **pouco previsíveis**, e é nelas que os alertas devem ser mais atentos.

![Desvio-padrão da cota por período: cheia e seca são estáveis; enchente e vazante variam mais.](../../../figuras/f10_variabilidade.png)

*Desvio-padrão da cota por período: cheia e seca são estáveis; enchente e vazante variam mais.*

> **⚠️ Atenção: armadilha das bibliotecas**
>
> O `pandas` (`.std()`, `.var()`) usa **ddof = 1** (amostral) por padrão; o `NumPy` (`np.std`, `np.var`) usa **ddof = 0** (populacional). Sempre declare o `ddof` explicitamente: `np.std(x, ddof=1)`.

## 3. Prática em Python

Compare a variação dos quatro períodos e veja a diferença entre ddof=0 e ddof=1.

- Script: [`aula_05.py`](aula_05.py)
- Notebook (Colab): [`aula_05.ipynb`](aula_05.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-05-medidas-de-variacao-amplitude-variancia-e-desvio-p/aula_05.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- As colunas `dp_pop` e `dp_amostral` são próximas porque n é grande; com n = 5 a diferença seria grande.
- Em enchente e vazante, a amplitude está inflada pelas leituras atípicas (8,90 m e 35,10 m) — compare com o DP.
- As três chamadas finais mostram `0,5937` (pandas e `ddof=1`) e `0,5905` (NumPy padrão).

## 4. Atividades de fixação

1. Para 18, 21, 21, 24, 26, calcule amplitude, variância e DP populacionais e amostrais.
2. Duas estações registram média de 24 m. A estação X tem DP de 0,3 m e a Y, DP de 3 m. Qual é mais previsível? O que você diria a um gestor?
3. Por que a variância amostral divide por n − 1? Em que situação a diferença entre dividir por n e por n − 1 é menos relevante?
4. Por que o desvio-padrão é mais fácil de interpretar do que a variância?
5. Use a tabela por período: qual período é o mais previsível e qual o menos previsível? Qual medida você usou e por quê?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir amplitude, variância e DP, com fórmulas.
- [ ] Diferenciar população e amostra e as duas variâncias.
- [ ] Explicar o papel do n − 1.
- [ ] Calcular à mão para séries de 5 valores.
- [ ] Saber o `ddof` padrão do pandas e do NumPy.

---
[← Voltar ao índice](../../README.md)
