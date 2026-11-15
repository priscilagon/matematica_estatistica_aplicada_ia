# Aula 6 — Quartis, outliers, normalização e padronização

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Calcular e interpretar medidas descritivas e de variação, explicando o que significam no contexto do problema. |
| **Objetos de conhecimento** | Quartis e outliers. Normalização e padronização (conceito e quando usar). |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** variância e desvio-padrão. |
| 60 min | **Aula expositiva:** quartis; identificação de outliers via boxplot; conceito e finalidade de normalização e padronização. |
| 75 min | **Prática guiada:** identificar leituras atípicas de cota e temperatura e aplicar normalização/padronização; discutir quando cada técnica é indicada. |
| 30 min | **Discussão:** impacto de um outlier não tratado em uma futura análise ou modelo de IA. |

## 2. Conteúdo

### 1. Quartis e boxplot

Os **quartis** dividem os dados ordenados em quatro partes de mesmo tamanho: **Q1** (25% dos valores abaixo), **Q2** = mediana (50%) e **Q3** (75%). O **intervalo interquartil** é **IQR = Q3 − Q1**: a amplitude da metade central dos dados, que **não** sofre influência de extremos.

![Anatomia do boxplot: a caixa vai de Q1 a Q3; a linha é a mediana; os bigodes vão até o último valor dentro dos limites; pontos fora são candidatos a outliers.](../../../figuras/f04_boxplot_anatomia.png)

*Anatomia do boxplot: a caixa vai de Q1 a Q3; a linha é a mediana; os bigodes vão até o último valor dentro dos limites; pontos fora são candidatos a outliers.*

### 2. Regra de Tukey (1,5 × IQR)

```text
limite inferior = Q1 − 1,5 × IQR        limite superior = Q3 + 1,5 × IQR
```

Valores fora dos limites são classificados como **outliers** (valores atípicos). O fator 1,5 é convenção, não lei.

> **📝 Exemplo resolvido: dados: 12, 14, 15, 16, 17, 18, 19, 21, 45 (n = 9)**
>
> **Q1** = mediana da metade inferior (12, 14, 15, 16) = **14,5**; **Q3** = mediana da metade superior (18, 19, 21, 45) = **20,0**. **IQR** = 5,5.
>
> **Limites:** 14,5 − 1,5×5,5 = **6,25**; 20,0 + 1,5×5,5 = **28,25**. O valor **45** está acima → **outlier**.

> **⚠️ Atenção: métodos de quartil**
>
> Existem várias convenções para calcular quartis. O método “mediana das metades” (acima) dá Q1 = 14,5 e Q3 = 20,0; o `pandas` (interpolação linear) dá Q1 = 15 e Q3 = 19. As conclusões costumam ser iguais, mas os números diferem. **Declare o método** que usou.

### 3. Outlier não é o mesmo que erro

A regra do IQR apenas **sinaliza** valores incomuns. O que fazer depende da investigação:

- **Erro de medição ou digitação** (ex.: cota de 8,90 m num dia em que o rio estava em 23,8 m): corrigir ou excluir, **registrando** o motivo.
- **Fenômeno real raro** (ex.: cheia histórica): manter e analisar à parte.
- **Falso alarme do método** (ex.: 4 dias de início de outubro, em plena seca, sinalizados porque a regra usa só os dias de seca; a cota ainda está descendo do período anterior): manter.

Um teste de **plausibilidade** ajuda: um rio não sobe ou desce mais de 2 m de um dia para o outro. Os saltos de 18/03 (8,90 → 23,80) e de 09/08 (35,10 → 24,74) violam essa regra e são **erros**.

> **💡 Dica: contexto manda**
>
> Aplicar a regra à cota do **ano inteiro** não acusaria os dois erros (a variação sazonal é grande). Aplicada **por período**, a regra enxerga o que é incomum *dentro* de cada fase do rio. Analise sempre no contexto certo.

### 4. Normalização e padronização

Variáveis em unidades diferentes (cota em metros, chuva em mm, temperatura em °C) têm escalas diferentes. Muitos algoritmos de IA (distâncias, gradiente descendente) dão mais peso a quem tem números maiores. A solução é **reescalar**.

|  | Normalização (min-máx) | Padronização (z-score) |
|---|---|---|
| Fórmula | x' = (x − mín) ÷ (máx − mín) | z = (x − média) ÷ desvio-padrão |
| Resultado | Valores entre 0 e 1 | Média 0 e desvio-padrão 1; sem limites fixos |
| Sensível a outliers? | **Muito** (mín e máx entram na fórmula) | Moderadamente (média e DP também mudam) |
| Quando usar | Quando se precisa de faixa fixa [0, 1] (redes neurais, imagens) | Quando os dados são aproximadamente simétricos; muito usada em regressão e k-NN |

> **📝 Exemplo resolvido: reescalando 10, 20, 30, 50**
>
> **Min-máx:** (x − 10) ÷ 40 → 0,00; 0,25; 0,50; 1,00.
>
> **Z-score:** média = 27,5; DP amostral = 14,79 → -1,183; -0,507; 0,169; 1,521.

O efeito do atípico é visível: na cota, o valor de 20 m vira **0,424** na escala min-máx com os atípicos (mín 8,90; máx 35,10) e **0,322** sem eles. O mesmo dado ganha “posição” diferente na escala.

> **📌 Conceito-chave: impacto em modelos de IA**
>
> Um outlier **não tratado** pode (i) deslocar a média, (ii) comprimir toda a escala min-máx, (iii) “puxar” uma reta de regressão e (iv) levar o modelo a aprender o erro como se fosse padrão. Tratar dados é parte do modelo.

## 3. Prática em Python

Aplique a regra do IQR à temperatura (ano todo) e à cota (por período), teste o salto diário e reescale a cota.

- Script: [`aula_06.py`](aula_06.py)
- Notebook (Colab): [`aula_06.ipynb`](aula_06.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-06-quartis-outliers-normalizacao-e-padronizacao/aula_06.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- A temperatura de **38,5 °C (22/10)** é o único atípico do ano; limites 25,55 e 31,55 °C.
- A regra por período acusa 18/03 (enchente) e 09/08 (vazante) e também **quatro dias de início de outubro** na seca — um alerta sem erro (teste do salto diário os absolve).
- `min-máx` termina em 0 e 1; o `z-score` tem média 0 e DP 1.
- A comparação “com e sem atípicos” mostra o valor 20 m indo de 0,424 para 0,322.

## 4. Atividades de fixação

1. Para 12, 14, 15, 16, 17, 18, 19, 21, 45, calcule Q1, Q3, IQR e os limites de Tukey. Existe outlier?
2. Normalize pelo método min-máx os valores 10, 20, 30, 50.
3. Padronize os valores 10, 20, 30, 50 (use DP amostral).
4. Aplique a regra do IQR à temperatura da água. Quais são os limites e o que você faria com o valor atípico?
5. O dia 18/03 tem cota de 8,90 m, e o dia seguinte, 23,80 m. É um outlier “real”? Justifique.
6. Por que a normalização min-máx é mais sensível a outliers do que a mediana e o IQR?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir Q1, Q2, Q3 e IQR; ler um boxplot.
- [ ] Aplicar a regra de Tukey (1,5 × IQR) à mão e no Python.
- [ ] Diferenciar outlier estatístico de erro de medição.
- [ ] Calcular e comparar min-máx e z-score.
- [ ] Explicar o impacto de outliers em modelos de IA.
- [ ] Revisar as Aulas 4 e 5 e a Oficina da Aula 6 para a **AV2**.

---
[← Voltar ao índice](../../README.md)
