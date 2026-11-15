# Aula 12 — Teorema de Bayes (intuição) — Oficina 3

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Calcular probabilidades simples e condicionais, aplicá-las em situações do cotidiano e de IA e interpretar distribuições. |
| **Objetos de conhecimento** | Lei da probabilidade total. Teorema de Bayes. Probabilidades a priori e a posteriori. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** da probabilidade condicional. |
| 55 min | **Aula expositiva:** probabilidade total e Teorema de Bayes; por que o teste “bom” pode errar muito. |
| 80 min | **Oficina 3 (Estatística do mundo real):** sistema de alerta de cheia com Python; discussão de falsos positivos. |
| 30 min | **Sistematização:** relação com classificadores em IA. |

## 2. Conteúdo

### 1. Atualizar crenças com evidências

O Teorema de Bayes mostra como **atualizar** uma probabilidade quando surge uma nova evidência. Ele inverte a condicional:

```text
P(H | E) = P(E | H) × P(H) ÷ P(E)
```

H é a hipótese; E, a evidência. **P(H)** é a probabilidade **a priori**; **P(H | E)**, a **a posteriori**. O denominador vem da **lei da probabilidade total**:

```text
P(E) = P(E | H) × P(H) + P(E | não H) × P(não H)
```

> **📝 Exemplo resolvido: alarme de cheia**
>
> Um sistema de alerta dispara quando detecta sinais de cheia. Dados didáticos: **P(cheia) = 0,30** (a priori); **sensibilidade** P(alarme | cheia) = 0,90; **falso positivo** P(alarme | não cheia) = 0,08.
>
> **P(alarme)** = 0,90×0,30 + 0,08×0,70 = 0,27 + 0,056 = **0,326**.
>
> **P(cheia | alarme)** = 0,27 ÷ 0,326 = **0,8282** → 82,8%.

> **⚠️ Atenção: o paradoxo da evidência rara**
>
> Se a cheia fosse rara (P = 0,05), o **mesmo** alarme (90% / 8%) teria P(cheia | alarme) = apenas **0,372** (37%). O alarme bom erra muito quando o evento é raro, porque os falsos positivos de milhares de dias normais superam os acertos dos poucos dias de cheia. Em IA, isso se chama **problema da taxa-base**.

![Frequências naturais do alarme de cheia: de 1000 dias, 326 têm alarme e 270 deles são cheias de verdade (270 ÷ 326 ≈ 0,83).](../../../figuras/f11_bayes.png)

*Frequências naturais do alarme de cheia: de 1000 dias, 326 têm alarme e 270 deles são cheias de verdade (270 ÷ 326 ≈ 0,83).*

### 2. Bayes com dados do projeto

H = “alerta alto”; E = “chuva forte (> 10 mm)”. P(H) = 0,343; P(E) = 0,252; P(E | H) = 0,272. Por Bayes, **P(H | E) = 0,3696**, igual ao cálculo direto por contagem — um bom “teste de sanidade” das fórmulas.

> **📌 Conceito-chave: conexão com IA**
>
> O classificador **Naive Bayes** (filtro de spam, análise de sentimento) aplica exatamente essa fórmula: calcula P(classe | palavras) a partir de P(palavras | classe) e P(classe).

## 3. Prática em Python

Calcule a posteriori do alarme de cheia e confirme a fórmula com os dados do projeto.

- Script: [`aula_12.py`](aula_12.py)
- Notebook (Colab): [`aula_12.ipynb`](aula_12.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-12-teorema-de-bayes-intuicao-oficina-3/aula_12.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `P(alarme) = 0,3260` e `P(cheia | alarme) = 0,8282`.
- Os dois caminhos (Bayes e contagem direta) dão 0,3696.
- Altere `prev` para 0,05 e veja a posteriori cair a 0,3719.

## 4. Atividades de fixação

1. Refaça o alarme de cheia com P(cheia) = 0,20, sensibilidade 0,95 e falso positivo 0,10. Calcule P(alarme) e P(cheia | alarme).
2. Explique por que o mesmo alarme é menos confiável quando o evento é raro.
3. Verifique, no projeto, que P(alto | chuva > 10) por Bayes coincide com a contagem direta.
4. Cite duas aplicações de Bayes em IA.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Enunciar o Teorema de Bayes e a lei da probabilidade total.
- [ ] Distinguir a priori e a posteriori; sensibilidade e falso positivo.
- [ ] Resolver problemas de teste/alarme à mão.
- [ ] Explicar o problema da taxa-base.
- [ ] Conectar Bayes a classificadores.

---
[← Voltar ao índice](../../README.md)
