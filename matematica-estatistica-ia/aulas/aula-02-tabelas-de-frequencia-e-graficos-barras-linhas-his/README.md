# Aula 2 — Tabelas de frequência e gráficos (barras, linhas, histogramas, boxplot)

| | |
|---|---|
| **Fase do projeto** | Fase 1 — Exploração e leitura de dados |
| **Habilidade** | Interpretar tabelas e gráficos, identificar padrões e resumir conjuntos de dados de forma objetiva. |
| **Objetos de conhecimento** | Tabelas e gráficos (barras, linhas, histogramas, boxplot). |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 10 min | **Retomada:** tipos de variáveis e escalas. |
| 50 min | **Aula expositiva:** tabelas de frequência; barras, linhas, histogramas e boxplot — quando usar cada um. |
| 90 min | **Oficina 1 (Estatística do mundo real), parte 1:** em grupos, construir ao menos três tipos de gráfico com o CSV do projeto, em planilha ou Python. |
| 30 min | **Apresentação rápida** (1 min por grupo): leitura oral do padrão observado em um gráfico. |

## 2. Conteúdo

### 1. Tabela de frequência

Resume uma variável contando quantas vezes cada valor (ou classe) aparece. A **frequência absoluta** é a contagem; a **frequência relativa** é a proporção em relação ao total.

```text
frequência relativa = frequência absoluta ÷ total de observações
```

> **📝 Exemplo resolvido: espécies registradas**
>
> Em 53 coletas, o **tambaqui** apareceu 22 vezes: 22 ÷ 53 = 0,415 → **41,5%**. As frequências relativas somam 100%.

Para uma variável **contínua** (como a cota) agrupamos os valores em **classes** (intervalos) antes de contar.

### 2. Qual gráfico para qual pergunta?

| Pergunta que quero responder | Gráfico | Tipo de variável |
|---|---|---|
| Qual categoria aparece mais? | Barras | Qualitativa |
| Como a variável muda no tempo? | Linhas | Quantitativa × tempo |
| Como os valores se distribuem? | Histograma | Quantitativa contínua |
| Como comparo grupos e vejo valores extremos? | Boxplot | Quantitativa × categoria |

![Gráfico de linhas: a cota sobe na enchente, atinge o pico na cheia e desce na vazante. Note as duas “agulhas” (leituras atípicas).](../../../figuras/f01_hidrograma.png)

*Gráfico de linhas: a cota sobe na enchente, atinge o pico na cheia e desce na vazante. Note as duas “agulhas” (leituras atípicas).*

![Histograma: a distribuição tem dois grupos de dias (águas baixas e águas altas).](../../../figuras/f02_histograma.png)

*Histograma: a distribuição tem dois grupos de dias (águas baixas e águas altas).*

> **⚠️ Atenção: histograma não é gráfico de barras**
>
> No **histograma** as barras representam intervalos de uma variável contínua e ficam coladas; no **gráfico de barras** cada barra é uma categoria e há espaço entre elas.

O **boxplot** resume cinco números (mínimo, Q1, mediana, Q3, máximo) e marca valores muito distantes como pontos isolados. Vamos detalhá-lo na Aula 6.

![Boxplot da cota por período: a cheia é alta e estável; enchente e vazante variam mais.](../../../figuras/f03_boxplot_periodo.png)

*Boxplot da cota por período: a cheia é alta e estável; enchente e vazante variam mais.*

## 3. Prática em Python

A célula abaixo monta a tabela de frequência das espécies, agrupa a cota em classes e desenha quatro gráficos de uma vez.

- Script: [`aula_02.py`](aula_02.py)
- Notebook (Colab): [`aula_02.ipynb`](aula_02.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-02-tabelas-de-frequencia-e-graficos-barras-linhas-his/aula_02.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `value_counts()` já conta as categorias; dividir por `freq.sum()` dá a frequência relativa.
- `pd.cut` cria as classes da cota; o intervalo `(16, 20]` inclui 20 e exclui 16.
- Cada gráfico responde a uma pergunta diferente — veja a tabela acima.

## 4. Atividades de fixação

1. Monte a tabela de frequência (absoluta e relativa) das espécies registradas e indique a moda.
2. Agrupe a cota em classes de 4 m e indique em qual classe há mais dias. O que isso revela sobre o rio?
3. Associe cada pergunta ao gráfico mais adequado: (a) Qual espécie é mais registrada? (b) Como a cota evoluiu em 2025? (c) A cota se distribui de forma simétrica? (d) Qual período tem maior variabilidade de cota?
4. Observe o gráfico de linhas e descreva, em duas frases, o padrão da cota ao longo do ano. Há algum ponto que parece “estranho”? Qual?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Calcular frequência absoluta e relativa.
- [ ] Escolher o gráfico adequado à pergunta e ao tipo de variável.
- [ ] Diferenciar histograma de gráfico de barras.
- [ ] Ler um boxplot de forma geral (caixa = metade central dos dados).
- [ ] Gerar gráficos com `matplotlib`/`pandas` e salvar a figura.

---
[← Voltar ao índice](../../README.md)
