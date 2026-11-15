# Aula 8 — Correlação de Pearson

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Interpretar a relação entre variáveis por meio de gráficos de dispersão, covariância e correlação. |
| **Objetos de conhecimento** | Correlação de Pearson. Interpretação de intensidade e sentido. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** covariância e suas limitações. |
| 55 min | **Aula expositiva:** coeficiente de correlação de Pearson; intensidade, sentido e r². |
| 80 min | **Prática em Python:** matriz de correlação, mapa de calor e efeito de um valor atípico. |
| 30 min | **Sistematização:** guia de interpretação de r no caderno de bordo. |

## 2. Conteúdo

### 1. Da covariância à correlação

Dividindo a covariância pelo produto dos desvios-padrão, eliminamos as unidades e obtemos um número **entre −1 e +1**:

```text
r = cov(X, Y) ÷ (s_x · s_y)
```

| Valor de r | Interpretação (guia prático) |
|---|---|
| +1 ou −1 | Relação linear perfeita (positiva ou negativa) |
| 0,7 a 1 (em módulo) | Forte |
| 0,4 a 0,7 | Moderada |
| 0,1 a 0,4 | Fraca |
| próximo de 0 | Sem relação **linear** |

> **📝 Exemplo resolvido: com X = 1…5 e Y = 2, 4, 5, 4, 5**
>
> cov amostral = 1,5; s_x = 1,5811; s_y = 1,2247.
>
> **r** = 1,5 ÷ (1,5811 × 1,2247) = **0,7746** → relação forte e positiva.

### 2. O coeficiente de determinação r²

Elevando r ao quadrado, obtemos a fração da variação de uma variável “acompanhada” linearmente pela outra. Entre cota e temperatura, r = -0,924 e **r² = 0,854**: cerca de 85% da variação de uma é acompanhada linearmente pela variação da outra.

### 3. Cuidados

- **Só mede relação linear.** Cota × chuva do mesmo dia: r = -0,093 (≈ 0). Isso **não** quer dizer que a chuva não influencia o rio — o efeito é defasado e acumulado.
- **Sensível a outliers.** Com a única leitura de 38,5 °C incluída, r cai de -0,924 para -0,830.
- **Não implica causalidade** (Aula 9).
- **Sempre acompanhe com um gráfico de dispersão.**

Quando calculamos o coeficiente para várias variáveis ao mesmo tempo, organizamos os resultados em uma **matriz de correlação**, que pode ser colorida como um **mapa de calor** para facilitar a leitura.

## 3. Prática em Python

Calcule a matriz de correlação do projeto e quantifique o impacto de um único valor atípico.

- Script: [`aula_08.py`](aula_08.py)
- Notebook (Colab): [`aula_08.ipynb`](aula_08.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-08-correlacao-de-pearson/aula_08.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- A diagonal vale 1,000 (cada variável com ela mesma).
- `cota × temperatura = −0,924`: forte e negativa.
- Incluir a leitura de 38,5 °C reduz |r| de 0,924 para 0,830.
- `dropna()` evita erros por dados ausentes ao correlacionar.

## 4. Atividades de fixação

1. Calcule r para X = 1,2,3,4,5 e Y = 2,4,5,4,5 e classifique a relação.
2. Classifique cada relação: r = +0,95; r = −0,35; r = 0,05; r = −0,82.
3. Entre cota e temperatura o r é -0,924. Qual o valor de r² e o que significa?
4. Cota × chuva (mesmo dia) tem r ≈ −0,09. Podemos concluir que a chuva não afeta o nível do rio? Justifique.
5. Explique por que um único valor atípico pode alterar bastante r. Cite o exemplo do projeto.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Fórmula e propriedades de r (−1 a +1, adimensional).
- [ ] Guia de interpretação de intensidade e sentido.
- [ ] Calcular r a partir de cov e DPs.
- [ ] Explicar r² e o limite de r (só linear, sensível a outliers).
- [ ] `df.corr()` e leitura de mapa de calor.

---
[← Voltar ao índice](../../README.md)
