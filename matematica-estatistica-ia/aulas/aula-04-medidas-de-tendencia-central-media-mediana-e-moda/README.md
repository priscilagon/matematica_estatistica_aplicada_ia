# Aula 4 — Medidas de tendência central: média, mediana e moda

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Calcular e interpretar medidas descritivas e de variação, explicando o que significam no contexto do problema. |
| **Objetos de conhecimento** | Média, mediana, moda. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** de tabelas e gráficos; pergunta-problema: “qual é o nível *típico* do Rio Negro?”. |
| 55 min | **Aula expositiva dialogada:** média, mediana e moda; como o valor atípico afeta cada uma. |
| 80 min | **Prática em planilha e em Python:** calcular as três medidas para cota, chuva, alerta e espécie. |
| 30 min | **Sistematização:** redação coletiva de um texto interpretativo (“o que a média esconde?”). |

## 2. Conteúdo

### 1. Por que resumir com um número?

Resumir 365 leituras em um valor “típico” facilita comparar períodos, comunicar um resultado e alimentar modelos. As **medidas de tendência central** respondem: *em torno de que valor os dados se concentram?*

### 2. Média aritmética

```text
média = (x₁ + x₂ + … + xₙ) ÷ n
```

É o “ponto de equilíbrio” dos dados. Usa **todos** os valores, por isso é sensível a valores extremos.

### 3. Mediana

É o valor do **meio** dos dados ordenados. Se n é ímpar, é o valor central; se n é par, é a média dos dois valores centrais. Não é afetada por valores extremos (**medida robusta**).

### 4. Moda

É o valor (ou categoria) **mais frequente**. Pode não existir (amodal), ter uma (unimodal) ou várias (multimodal). É a **única** medida possível para variáveis nominais.

| Medida | Escala mínima | Sensível a extremos? | Quando usar |
|---|---|---|---|
| Média | Intervalar/razão | Sim | Dados simétricos, sem atípicos |
| Mediana | Ordinal ou acima | Não | Dados assimétricos ou com atípicos |
| Moda | Nominal | Não | Categorias; valor mais comum |

> **📝 Exemplo resolvido: cota de seis dias consecutivos: 21, 23, 23, 24, 25, 27 (m)**
>
> **Média:** (21+23+23+24+25+27) ÷ 6 = 143 ÷ 6 = **23,83 m**.
>
> **Mediana:** n = 6 (par). Os dois valores centrais são 23 e 24 → (23+24) ÷ 2 = **23,5 m**.
>
> **Moda:** o 23 aparece duas vezes → **23 m**.

### 5. O efeito do valor atípico

Na semana de 6 a 12/ago a cota foi: 25,54; 25,36; 25,14; 35,10; 24,74; 24,59; 24,45. O 35,10 m é uma leitura atípica. Com ele, a **média** é **26,42 m**; a **mediana** continua em **25,14 m**, que representa melhor a semana.

> **⚠️ Atenção: assimetria**
>
> A chuva diária tem média **6,27 mm**, mediana **1,30 mm** e moda **0,0 mm**. Muitos dias secos e poucos dias de chuva forte “puxam” a média para cima. Dizer “chove 6,3 mm por dia” é enganoso: na maioria dos dias chove bem menos.

> **💡 Dica: regra prática**
>
> Se média e mediana são parecidas, os dados são aproximadamente simétricos. Se são muito diferentes, há assimetria ou valores atípicos: prefira a mediana e **mostre as duas**.

## 3. Prática em Python

Calcule as três medidas e veja, nos próprios dados do rio, quando a média engana.

- Script: [`aula_04.py`](aula_04.py)
- Notebook (Colab): [`aula_04.ipynb`](aula_04.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-04-medidas-de-tendencia-central-media-mediana-e-moda/aula_04.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- Para a cota (contínua), a moda quase nunca informa: nenhum valor se repete muito.
- Em `chuva_mm`, média ≫ mediana: assimetria à direita.
- `mode()` devolve uma Série (pode haver empate); por isso usamos `.iloc[0]` para pegar a primeira.
- A média da semana de 6 a 12/ago foi “contaminada” pela leitura de 35,10 m; a mediana não.

## 4. Atividades de fixação

1. Para os dados 20, 25, 25, 34, 36 (cota em m), calcule média, mediana, moda e amplitude.
2. Calcule média, mediana e moda de 21, 23, 23, 24, 25, 27 e explique o resultado em uma frase.
3. Adicione o valor 60 aos dados do exercício 2. Recalcule a média e a mediana e compare.
4. No CSV, qual é a espécie mais registrada (moda) e o alerta mais frequente? Por que a média não se aplica a essas colunas?
5. A média diária de chuva do ano é maior ou menor que a mediana? O que isso diz sobre a distribuição da chuva?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Calcular média, mediana e moda à mão e no Python.
- [ ] Saber quando n é par ou ímpar na mediana.
- [ ] Explicar por que a mediana é robusta e a média, não.
- [ ] Relacionar assimetria com a diferença entre média e mediana.
- [ ] Escolher a medida certa por escala (moda para nominal).

---
[← Voltar ao índice](../../README.md)
