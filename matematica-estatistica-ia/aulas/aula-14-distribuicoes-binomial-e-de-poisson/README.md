# Aula 14 — Distribuições Binomial e de Poisson

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Calcular probabilidades simples e condicionais, aplicá-las em situações do cotidiano e de IA e interpretar distribuições. |
| **Objetos de conhecimento** | Variáveis aleatórias discretas. Distribuição Binomial. Distribuição de Poisson. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** da distribuição normal. |
| 55 min | **Aula expositiva:** ensaios de Bernoulli, Binomial; contagens de eventos raros, Poisson. |
| 80 min | **Prática em Python:** modelar dias de alerta alto (Binomial) e dias de chuva forte por mês (Poisson). |
| 30 min | **Sistematização:** quadro comparativo Binomial × Poisson × Normal. |

## 2. Conteúdo

### 1. Distribuição Binomial

Modela o **número de sucessos** em n tentativas independentes, cada uma com probabilidade de sucesso p constante (ensaios de Bernoulli). Notação: **X ~ Bin(n, p)**.

```text
P(X = k) = C(n, k) · pᵏ · (1 − p)ⁿ⁻ᵏ        μ = n·p        σ = √(n·p·(1 − p))
```

> **📝 Exemplo resolvido: moeda: 10 lançamentos, p = 0,5**
>
> P(X = 5) = C(10,5) · 0,5¹⁰ = 252 ÷ 1024 = **0,2461**.
>
> P(X ≥ 8) = (45 + 10 + 1) ÷ 1024 = 56 ÷ 1024 = **0,0547**.

**No projeto:** em 30 dias, quantos terão alerta alto? Com p = 0,3425: esperado μ = 30 × 0,3425 ≈ **10,3 dias**, σ ≈ **2,6**. P(X = 10) = **0,1522**; P(X ≥ 15) = **0,0546**.

> **⚠️ Atenção: cuidado com a independência**
>
> Dias consecutivos do rio **não são independentes** (cota alta hoje implica cota alta amanhã). O modelo binomial é uma **aproximação didática**; um modelo sério trataria a dependência temporal.

### 2. Distribuição de Poisson

Modela o **número de ocorrências** de um evento em um intervalo fixo (tempo, área), quando ocorrem de forma independente e a uma taxa média λ constante. Notação: **X ~ Poisson(λ)**.

```text
P(X = k) = (e^(−λ) · λᵏ) ÷ k!        média = variância = λ
```

> **📝 Exemplo resolvido: λ = 2 ocorrências por intervalo**
>
> P(X = 0) = e⁻² = **0,1353**; P(X = 1) = 2·e⁻² = **0,2707**; P(X ≥ 2) = 1 − 0,1353 − 0,2707 = **0,5940**.

**No projeto:** dias de chuva forte (> 30 mm) por mês: média λ = **0,583**. P(nenhum dia em um mês) = **0,5580**; P(3 ou mais dias) = **0,0215**. A comparação entre meses observados e esperados mostra um ajuste razoável.

| Modelo | Variável | Parâmetros | Exemplo |
|---|---|---|---|
| Binomial | Nº de sucessos em n ensaios | n, p | Dias com alerta alto em 30 dias |
| Poisson | Nº de ocorrências por intervalo | λ | Dias de chuva forte por mês |
| Normal | Medida contínua | μ, σ | Temperatura da água |

## 3. Prática em Python

Use `scipy.stats.binom` e `scipy.stats.poisson` e compare o esperado com o observado.

- Script: [`aula_14.py`](aula_14.py)
- Notebook (Colab): [`aula_14.ipynb`](aula_14.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-14-distribuicoes-binomial-e-de-poisson/aula_14.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `binom.pmf(k, n, p)` = P(X = k); `binom.sf(k-1, n, p)` = P(X ≥ k).
- Para Poisson, λ = média mensal = 0,583.
- A tabela final compara meses observados com meses esperados em cada contagem k.

## 4. Atividades de fixação

1. Em 10 lançamentos de uma moeda justa, calcule P(X = 5) e P(X ≥ 8).
2. Para X ~ Bin(30; 0,3425), calcule a média e o desvio-padrão e interprete.
3. Se chegam em média 2 alertas por semana a um centro de monitoramento (Poisson), qual a probabilidade de uma semana sem nenhum alerta? E de 2 ou mais?
4. Chuvas fortes ocorrem em média λ = 0,583 dias por mês. Calcule P(0) e P(≥ 3).
5. Por que o modelo binomial para “dias com alerta alto” é só uma aproximação?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Condições do modelo Binomial e de Poisson.
- [ ] Fórmulas de P(X = k), média e desvio-padrão.
- [ ] Calcular com a calculadora e com `scipy.stats`.
- [ ] Comparar valores esperados com os observados.
- [ ] Reconhecer limitações (independência).

---
[← Voltar ao índice](../../README.md)
