# Aula 10 — Probabilidade: eventos, regra da soma e regra do produto

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Calcular probabilidades simples e condicionais, aplicá-las em situações do cotidiano e de IA e interpretar distribuições. |
| **Objetos de conhecimento** | Experimentos aleatórios, espaço amostral, eventos. Regra da soma e do produto. Evento complementar. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** da Fase 2 e abertura da Fase 3: “o que podemos prever?”. |
| 60 min | **Aula expositiva:** espaço amostral, evento, probabilidade (frequência relativa); regras da soma, do produto e do complemento. |
| 75 min | **Prática em Python:** estimar probabilidades a partir dos dados do rio e testar independência. |
| 30 min | **Sistematização:** mapa conceitual de probabilidade no caderno de bordo. |

## 2. Conteúdo

### 1. Linguagem da probabilidade

- **Experimento aleatório:** resultado não previsível com certeza (a cota de amanhã, o sorteio de um dia do ano).
- **Espaço amostral (Ω):** conjunto de todos os resultados possíveis.
- **Evento:** subconjunto do espaço amostral (ex.: “o dia tem alerta alto”).
- **Probabilidade:** número entre 0 e 1 que mede a chance do evento.

```text
P(A) = casos favoráveis ÷ casos possíveis      (resultados igualmente prováveis)
```

Com dados históricos, estimamos a probabilidade pela **frequência relativa**. Seja **A = “alerta alto”**: 125 dias em 365 → **P(A) = 0,3425**.

### 2. Complemento e regra da soma

```text
P(não A) = 1 − P(A)
```

```text
P(A ou B) = P(A) + P(B) − P(A e B)
```

Subtraímos P(A e B) porque os dias que satisfazem os dois eventos foram contados duas vezes. Se A e B são **mutuamente exclusivos** (não ocorrem juntos), P(A e B) = 0.

> **📝 Exemplo resolvido: A = alerta alto; B = choveu (chuva > 0)**
>
> P(A) = 0,3425; P(B) = 0,5342 (195 dias); P(A e B) = 0,1671 (61 dias).
>
> **P(A ou B)** = 0,3425 + 0,5342 − 0,1671 = **0,7096**. **P(não A)** = 1 − 0,3425 = **0,6575**.

### 3. Regra do produto e independência

Dois eventos são **independentes** quando saber que um ocorreu não muda a probabilidade do outro. Nesse caso:

```text
P(A e B) = P(A) × P(B)      (somente se A e B forem independentes)
```

Se alerta alto e chuva fossem independentes, esperaríamos P(A)×P(B) = 0,1830 → cerca de **66,8 dias** com os dois eventos. Observamos **61**. A diferença é pequena, mas observe: com dados reais, a “independência” é sempre **aproximada**; nas próximas aulas veremos como quantificar essa diferença.

> **⚠️ Atenção: erros comuns**
>
> (1) Somar probabilidades sem subtrair P(A e B). (2) Multiplicar P(A)×P(B) quando os eventos **não** são independentes. (3) Confundir “mutuamente exclusivos” com “independentes”: se dois eventos de probabilidade positiva são exclusivos, eles são **dependentes** (saber que um ocorreu garante que o outro não ocorreu).

> **📌 Conceito-chave: probabilidade e IA**
>
> Classificadores, filtros de spam, assistentes e sistemas de recomendação trabalham com probabilidades: o modelo não “sabe”, ele **estima** a chance de cada resposta.

## 3. Prática em Python

Estime P(A), P(B), P(A e B), a regra da soma e teste a independência com contagens.

- Script: [`aula_10.py`](aula_10.py)
- Notebook (Colab): [`aula_10.ipynb`](aula_10.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-10-probabilidade-eventos-regra-da-soma-e-regra-do-pro/aula_10.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- A média de uma coluna booleana (`True/False`) é a **proporção** de `True`: é a forma mais simples de estimar probabilidades.
- A regra da soma e a contagem direta dão o mesmo valor (0,7096).
- O produto P(A)×P(B) = 0,1830 é próximo de P(A e B) = 0,1671, mas não igual.

## 4. Atividades de fixação

1. Um dado de 6 faces é lançado. Calcule P(par), P(maior que 4) e P(par ou maior que 4).
2. No CSV, calcule P(alerta alto) e P(não alto). Explique em uma frase.
3. Calcule P(alto ou choveu) e confira com a contagem direta.
4. Se “alerta alto” e “choveu” fossem independentes, quantos dias com os dois eventos esperaríamos? Compare com o observado.
5. Explique a diferença entre eventos mutuamente exclusivos e eventos independentes. Dê um exemplo de cada.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir espaço amostral, evento e probabilidade.
- [ ] Calcular P(complemento), P(A ou B) e P(A e B).
- [ ] Aplicar a regra do produto somente sob independência.
- [ ] Estimar probabilidades com frequências relativas no Python.
- [ ] Diferenciar exclusivos de independentes.

---
[← Voltar ao índice](../../README.md)
