# Aula 18 — Produto escalar, funções lineares e não lineares

| | |
|---|---|
| **Fase do projeto** | Fase 4 — Fundamentos matemáticos da IA e síntese |
| **Habilidade** | Aplicar conceitos de álgebra linear e cálculo em problemas simples de IA, interpretando o significado dos resultados. |
| **Objetos de conhecimento** | Produto escalar. Função linear e não linear. Modelo como combinação de features. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** vetores e matrizes. |
| 55 min | **Aula expositiva:** produto escalar, previsão linear w·x + b, funções lineares e não lineares, erro quadrático médio. |
| 80 min | **Prática em Python:** calcular previsões e comparar ajuste linear × polinomial da cota. |
| 30 min | **Sistematização:** o que significa “aprender” um modelo. |

## 2. Conteúdo

### 1. Produto escalar

```text
a · b = a₁b₁ + a₂b₂ + … + aₙbₙ
```

Multiplica-se componente a componente e somam-se os resultados; o resultado é **um número**. Exemplo: [2, 1, 3] · [4, 0, 5] = 8 + 0 + 15 = **23**.

### 2. Um modelo linear é um produto escalar

```text
previsão = w · x + b = w₁x₁ + w₂x₂ + … + b
```

**x** são as *features* de um dia; **w**, os **pesos** (a importância de cada feature) e **b**, o **viés**. “Treinar” o modelo é encontrar w e b que dão boas previsões.

> **📝 Exemplo resolvido: x = [24; 10; 28], w = [0,5; 0,1; −0,2], b = 3**
>
> w · x = 0,5·24 + 0,1·10 + (−0,2)·28 = 12 + 1 − 5,6 = 7,4.
>
> previsão = 7,4 + 3 = **10,4**.
>
> O peso negativo (−0,2) indica que a temperatura **diminui** a previsão.

### 3. Funções lineares e não lineares

Uma função **linear** (y = a·x + b) tem taxa de variação **constante**: gráfico em reta. Uma função **não linear** (ex.: y = x², polinômio de grau 3, exponencial) tem taxa de variação que **muda**. A cota ao longo do ano sobe, atinge o pico e desce: **não é uma reta**.

![A reta não acompanha o ciclo da cota; o polinômio de grau 3, sim.](../../../figuras/f08_ajuste.png)

*A reta não acompanha o ciclo da cota; o polinômio de grau 3, sim.*

Medimos a qualidade do ajuste pelo **erro quadrático médio (EQM)**: média dos quadrados das diferenças entre valor real e previsto. Para a cota por dia do ano: EQM da reta = **15,851** e EQM do polinômio de grau 3 = **2,807** — o ajuste não linear erra muito menos.

> **⚠️ Atenção: ajuste melhor ≠ modelo melhor**
>
> Um polinômio de grau muito alto pode “decorar” os dados (*overfitting*) e falhar com dados novos. Por isso se avalia o modelo com dados que ele **não viu** (conjunto de teste).

## 3. Prática em Python

Calcule produtos escalares, a previsão linear e compare reta e polinômio com `np.polyfit`.

- Script: [`aula_18.py`](aula_18.py)
- Notebook (Colab): [`aula_18.ipynb`](aula_18.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-18-produto-escalar-funcoes-lineares-e-nao-lineares/aula_18.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `np.dot(a, b)` = 23.
- A previsão do modelo com pesos dados é 10,4.
- `np.polyfit(x, y, grau)` ajusta o polinômio; `np.polyval` calcula as previsões.
- EQM de 15,851 (reta) contra 2,807 (grau 3).

## 4. Atividades de fixação

1. Calcule [1, −2, 3] · [4, 0, −1].
2. Um modelo tem w = [0,5; 0,1; −0,2] e b = 3. Calcule a previsão para o dia x = [22; 8; 25].
3. Classifique como linear ou não linear: (a) y = 3x + 2; (b) y = x²; (c) y = 5; (d) y = 2ˣ.
4. Por que uma reta não é um bom modelo para a cota ao longo do ano? Use o EQM.
5. O que é *overfitting* e por que avaliar o modelo com dados novos?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Calcular produto escalar à mão e com `np.dot`.
- [ ] Interpretar pesos e viés em w·x + b.
- [ ] Diferenciar função linear e não linear.
- [ ] Definir EQM e interpretá-lo.
- [ ] Explicar overfitting e a necessidade de dados de teste.

---
[← Voltar ao índice](../../README.md)
