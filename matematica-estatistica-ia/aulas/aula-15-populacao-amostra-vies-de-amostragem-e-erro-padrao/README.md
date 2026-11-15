# Aula 15 — População, amostra, viés de amostragem e erro-padrão

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Explicar a diferença entre população e amostra, reconhecer vieses de amostragem e interpretar a variação amostral. |
| **Objetos de conhecimento** | População e amostra. Amostragem aleatória. Viés. Erro-padrão da média. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** distribuições de probabilidade. |
| 55 min | **Aula expositiva:** população × amostra; amostragem aleatória; vieses; distribuição das médias amostrais. |
| 80 min | **Prática em Python:** simular amostras aleatórias e uma amostra viciada. |
| 30 min | **Sistematização:** como planejar uma coleta de dados sem viés. |

## 2. Conteúdo

### 1. População e amostra

**População** é o conjunto de **todos** os elementos de interesse; **amostra** é um subconjunto observado. Quase nunca medimos a população inteira, então usamos a amostra para **estimar** parâmetros (μ, σ, p) por meio de **estatísticas** (x̄, s, p̂).

> **📌 Conceito-chave: neste material**
>
> Para fins didáticos, tratamos os 365 dias da base como **população** e sorteamos amostras dela, o que nos permite comparar a estimativa com o valor verdadeiro.

### 2. Variação amostral e erro-padrão

Cada amostra produz uma média diferente. Em cinco amostras de 30 dias, as médias de temperatura variaram de 28,44 a 28,57 (população: 28,560). Repetindo 1000 vezes, as médias se distribuem em torno do valor verdadeiro (média das médias = 28,562) com desvio de **0,155**, que é o **erro-padrão**:

```text
erro-padrão da média = σ ÷ √n
```

Teoricamente: 0,883 ÷ √30 = **0,161**, muito próximo do simulado. Com n = 120, o erro-padrão cai para **0,081** — quadruplicar n **reduz o erro à metade**.

![Médias de 1000 amostras de 30 dias: concentradas em torno da média da população.](../../../figuras/f07_amostragem.png)

*Médias de 1000 amostras de 30 dias: concentradas em torno da média da população.*

### 3. Viés de amostragem

Aumentar n **não corrige viés**. Se coletarmos só dias de seca (out.–nov.), a média da temperatura é **29,678 °C**, bem acima do valor da população (28,560 °C), qualquer que seja o tamanho da amostra.

| Tipo de viés | Descrição | Exemplo |
|---|---|---|
| Seleção | A amostra não representa a população | Medir só em um período do ano |
| Voluntários | Só responde quem quer | Pesquisa online com adesão espontânea |
| Sobrevivência | Só vemos o que “sobreviveu” | Analisar só estações que não falharam |
| Medição | Instrumento ou método distorce | Régua mal calibrada |

> **💡 Dica: IA e viés**
>
> Um modelo treinado com dados enviesados reproduz o viés. Uma IA de previsão de cheias treinada só com dados de seca falharia na cheia — por mais dados que tivesse.

## 3. Prática em Python

Simule amostragem aleatória e compare com uma amostra viciada.

- Script: [`aula_15.py`](aula_15.py)
- Notebook (Colab): [`aula_15.ipynb`](aula_15.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-15-populacao-amostra-vies-de-amostragem-e-erro-padrao/aula_15.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `df.sample(30, random_state=k)` sorteia 30 dias sem reposição.
- A média das 1000 médias (28,562) é quase igual à da população (28,560).
- O erro-padrão simulado (0,155) é próximo do teórico (0,161).
- A amostra só de seca dá 29,678: **viés**.

## 4. Atividades de fixação

1. Defina população e amostra e dê um exemplo para cada um no contexto do Rio Negro.
2. Uma amostra de n = 36 tem desvio-padrão populacional σ = 3. Calcule o erro-padrão. O que acontece com ele se n for quadruplicado (144)?
3. Um pesquisador mediu a temperatura apenas na seca e concluiu que a água do rio “é quente o ano todo”. Qual é o problema?
4. Aumentar o tamanho de uma amostra viciada resolve o viés? Justifique.
5. Cite duas formas de reduzir o viés de amostragem ao planejar uma coleta.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir população, amostra, parâmetro e estatística.
- [ ] Explicar o erro-padrão e como diminuí-lo.
- [ ] Reconhecer tipos de viés.
- [ ] Diferenciar erro aleatório e erro sistemático.
- [ ] `df.sample` e simulação de amostras no Python.

---
[← Voltar ao índice](../../README.md)
