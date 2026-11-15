# Aula 17 — Vetores e matrizes: dados como números organizados

| | |
|---|---|
| **Fase do projeto** | Fase 4 — Fundamentos matemáticos da IA e síntese |
| **Habilidade** | Aplicar conceitos de álgebra linear e cálculo em problemas simples de IA, interpretando o significado dos resultados. |
| **Objetos de conhecimento** | Vetores. Matrizes. Operações: soma, multiplicação por escalar, transposta e produto matricial. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** da Fase 3 e abertura da Fase 4: “como o computador enxerga uma tabela?”. |
| 55 min | **Aula expositiva:** vetor, matriz, dimensões, soma, escalar, transposta, produto matricial. |
| 80 min | **Prática em Python (NumPy):** transformar o CSV em matriz de *features* e operar com matrizes. |
| 30 min | **Sistematização:** dicionário “tabela ↔ matriz ↔ tensor” no caderno de bordo. |

## 2. Conteúdo

### 1. Vetor e matriz

Um **vetor** é uma lista ordenada de números. O registro de **um dia** — cota, chuva e temperatura — é um vetor de dimensão 3: **x = [18,01; 4,4; 29,4]**. Uma **matriz** é uma tabela retangular de números: cada **linha** é uma observação e cada **coluna**, uma variável (*feature*). Uma matriz de m linhas e n colunas tem **dimensão m × n**.

A base do projeto, só com as três colunas numéricas e sem as leituras atípicas, vira uma matriz **X** de dimensão **364 × 3** (observações × features). Para a IA, imagens, textos e sons também são, no final, matrizes ou tensores (matrizes de dimensão maior).

### 2. Operações

| Operação | Como se faz | Exigência |
|---|---|---|
| Soma A + B | Soma entrada por entrada | Mesma dimensão |
| Escalar k·A | Multiplica cada entrada por k | Nenhuma |
| Transposta Aᵀ | Troca linhas por colunas | Nenhuma |
| Produto A·B | Linha de A × coluna de B (produto escalar) | Colunas de A = linhas de B |

> **📝 Exemplo resolvido: C = [[2, 0], [1, 3]] e D = [[1, 4], [2, 5]]**
>
> **C + D** = [[3, 4], [3, 8]]. **2·C** = [[4, 0], [2, 6]].
>
> **C · D:** (1,1) = 2·1 + 0·2 = 2; (1,2) = 2·4 + 0·5 = 8; (2,1) = 1·1 + 3·2 = 7; (2,2) = 1·4 + 3·5 = 19.
>
> Resultado: **[[2, 8], [7, 19]]**.

> **⚠️ Atenção: o produto matricial não é comutativo**
>
> Em geral, **A·B ≠ B·A**. Calcule D·C para verificar: o resultado é diferente de C·D.

> **📌 Conceito-chave: conexão com IA**
>
> Uma camada de rede neural calcula **Y = X·W + b**: um produto de matrizes. Por isso as GPUs, que multiplicam matrizes muito rápido, são tão importantes para a IA.

Operação útil no projeto: o vetor de **médias das colunas** de X é [22,174; 6,286; 28,560], e as **médias mensais** formam uma matriz 12 × 3 — uma “impressão digital” de cada mês do rio.

## 3. Prática em Python

Converta o DataFrame em matriz NumPy e treine as operações com matrizes pequenas.

- Script: [`aula_17.py`](aula_17.py)
- Notebook (Colab): [`aula_17.ipynb`](aula_17.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-17-vetores-e-matrizes-dados-como-numeros-organizados/aula_17.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `df[[...]].to_numpy()` devolve a matriz; `X.shape` mostra (364, 3).
- `@` é o produto matricial; `*` multiplica **entrada por entrada** — não confunda.
- A matriz mensal 12 × 3 mostra que a cota máxima ocorre em junho e a mínima em novembro.

## 4. Atividades de fixação

1. Dados C = [[2, 0], [1, 3]] e D = [[1, 4], [2, 5]], calcule C + D, 2·C e C·D.
2. Calcule D·C e compare com C·D. O que se conclui?
3. Uma matriz tem dimensão 5 × 3 e outra 3 × 4. É possível multiplicá-las? Qual a dimensão do resultado? E na ordem inversa?
4. Qual é a dimensão da matriz X do projeto e o que representam suas linhas e colunas?
5. Escreva a transposta de A = [[1, 2, 3], [4, 5, 6]] e informe sua dimensão.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir vetor, matriz e dimensão.
- [ ] Somar, multiplicar por escalar e transpor.
- [ ] Multiplicar matrizes à mão (2×2) e saber quando é possível.
- [ ] Diferenciar `@` de `*` no NumPy.
- [ ] Relacionar a tabela de dados à matriz de *features*.

---
[← Voltar ao índice](../../README.md)
