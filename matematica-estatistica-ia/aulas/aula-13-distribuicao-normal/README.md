# Aula 13 — Distribuição Normal

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Calcular probabilidades simples e condicionais, aplicá-las em situações do cotidiano e de IA e interpretar distribuições. |
| **Objetos de conhecimento** | Variável aleatória contínua. Distribuição Normal. Padronização (z). Regra empírica 68–95–99,7. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** padronização (z-score) e desvio-padrão. |
| 60 min | **Aula expositiva:** curva normal, parâmetros μ e σ, tabela/uso do z, regra 68–95–99,7. |
| 75 min | **Prática em Python:** ajustar uma normal à temperatura da água e calcular probabilidades com `scipy.stats`. |
| 30 min | **Sistematização:** quando a normal é um bom modelo e quando não é. |

## 2. Conteúdo

### 1. A curva normal

Muitas medições (altura, erro de instrumento, temperatura da água) agrupam-se em torno de um valor central e rareiam simetricamente para os lados, formando o “sino” da **distribuição normal**, definida por dois parâmetros: a **média μ** (centro) e o **desvio-padrão σ** (largura). Notação: **X ~ N(μ, σ)**.

![A distribuição normal ajustada à temperatura da água e a regra 68–95–99,7.](../../../figuras/f06_normal.png)

*A distribuição normal ajustada à temperatura da água e a regra 68–95–99,7.*

### 2. Regra empírica (68–95–99,7)

| Intervalo | Proporção teórica | Nos dados da temperatura |
|---|---|---|
| μ ± 1σ | 68,3% | 61,5% |
| μ ± 2σ | 95,4% | 99,2% |
| μ ± 3σ | 99,7% | 100,0% |

A diferença no primeiro intervalo (61,5% × 68,3%) lembra que os dados reais **não são perfeitamente normais**: a temperatura do rio depende da estação e não é simétrica ao longo do ano. A normal é um **modelo** — útil, mas aproximado.

### 3. Escore z e cálculo de probabilidades

```text
z = (x − μ) ÷ σ
```

O z diz **quantos desvios-padrão** o valor está acima (+) ou abaixo (−) da média. Probabilidades vêm da **área** sob a curva (tabela da normal padrão ou `scipy.stats.norm.cdf`).

> **📝 Exemplo resolvido: temperatura ~ N(28,56; 0,884)**
>
> **P(T < 28,0):** z = (28,0 − 28,56) ÷ 0,884 ≈ −0,63 → **0,2634** (≈ 26,3%).
>
> **P(T > 30,0):** z ≈ +1,63 → **0,0517** (≈ 5,2%).
>
> **P(27 < T < 30)** = **0,9094** (≈ 90,9%).

> **⚠️ Atenção: contínua: P(X = valor) = 0**
>
> Em variáveis contínuas, a probabilidade de um valor **exato** é zero; só intervalos têm probabilidade positiva (área sob a curva).

> **💡 Dica: quando desconfiar da normal**
>
> Histograma muito assimétrico (como a chuva diária), valores sempre positivos e próximos de zero, ou dois picos (como a cota ao longo do ano) indicam que **outro modelo** é mais adequado.

## 3. Prática em Python

Ajuste a normal à temperatura (sem a leitura atípica) e verifique a regra 68–95–99,7 nos dados.

- Script: [`aula_13.py`](aula_13.py)
- Notebook (Colab): [`aula_13.ipynb`](aula_13.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-13-distribuicao-normal/aula_13.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `norm.cdf(x, mu, sigma)` devolve P(T < x).
- A proporção em 1σ (61,5%) fica abaixo de 68,3%; em 2σ e 3σ a regra funciona bem (99,2% e 100%).
- O histograma com a curva ajustada permite “ver” a qualidade do ajuste.

## 4. Atividades de fixação

1. Se X ~ N(28; 2), calcule o escore z de x = 30 e de x = 25. Interprete.
2. Se X ~ N(28; 2), qual a proporção aproximada de valores entre 26 e 30? Qual o valor de P(X < 30)?
3. Com a temperatura ~ N(28,56; 0,884), calcule P(T < 28) e P(T > 30). O que significa o resultado em linguagem simples?
4. A chuva diária pode ser modelada por uma normal? Justifique com base no histograma e nas medidas descritivas.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Parâmetros μ e σ e notação N(μ, σ).
- [ ] Calcular e interpretar z.
- [ ] Aplicar a regra 68–95–99,7.
- [ ] Usar `scipy.stats.norm.cdf` e `ppf`.
- [ ] Reconhecer quando a normal não é adequada.

---
[← Voltar ao índice](../../README.md)
