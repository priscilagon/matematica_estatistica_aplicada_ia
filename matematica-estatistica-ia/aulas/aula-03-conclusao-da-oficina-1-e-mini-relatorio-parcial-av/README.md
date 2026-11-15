# Aula 3 — Conclusão da Oficina 1 e mini-relatório parcial (AV1)

| | |
|---|---|
| **Fase do projeto** | Fase 1 — Exploração e leitura de dados |
| **Habilidade** | Interpretar tabelas e gráficos, identificar padrões e resumir conjuntos de dados de forma objetiva. |
| **Objetos de conhecimento** | Leitura de dados. Tabelas e gráficos. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | **AV1** — avaliação desta aula (ver Parte III da apostila): 8 questões objetivas, 2 discursivas e a prática em Python, que inclui o mini-relatório do grupo. |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** e esclarecimento de dúvidas sobre gráficos. |
| 100 min | **Oficina 1, parte 2:** cada grupo elabora um **mini-relatório de 1 página** (gráficos + interpretação escrita em linguagem acessível a um público não técnico). |
| 45 min | **Entrega e socialização** dos mini-relatórios, com feedback do docente. |
| 20 min | **Fechamento:** critérios de uma boa leitura de dados e transição para as medidas descritivas. |

## 2. Conteúdo

### 1. O que é um bom mini-relatório de dados

Um relatório técnico curto precisa **dizer algo sobre os dados**, não apenas mostrar gráficos. A estrutura recomendada cabe em uma página:

| Parte | O que escrever | Exemplo |
|---|---|---|
| Título e fonte | Nome claro; de onde vêm os dados; período | “Cota diária do Rio Negro, Porto de Manaus, 2025 (base didática)” |
| Gráfico(s) | Um por pergunta, com título e unidades nos eixos | Linha da cota + boxplot por período |
| Tabela-resumo | Poucos números que sustentam a leitura | Dias, mínimo e máximo por período |
| Interpretação | 2 a 4 frases: padrão, comparação, ponto estranho | “O pico ocorreu na cheia, perto de 28 m…” |
| Limites | O que os dados **não** permitem concluir | “Dados de um único ano.” |

> **💡 Dica: linguagem acessível**
>
> Escreva para alguém de outra área (um gestor, um colega de outra equipe). Evite jargão: em vez de “distribuição bimodal”, diga “há dois grupos de dias: de águas baixas e de águas altas”.

### 2. Tabela-resumo por período

| Período | Dias | Cota mínima (m) | Cota máxima (m) |
|---|---|---|---|
| enchente | 151 | 8,90 | 26,70 |
| cheia | 92 | 26,38 | 28,60 |
| vazante | 61 | 17,40 | 35,10 |
| seca | 61 | 15,92 | 17,27 |

> **⚠️ Atenção: cuidado com valores extremos**
>
> As colunas de mínimo e máximo de **enchente** (8,90 m) e **vazante** (35,10 m) estão contaminadas pelas leituras atípicas. Um bom relatório **menciona** esse fato ou trata os dados antes de resumir — assunto da Aula 6.

## 3. Prática em Python

Esta célula produz a tabela-resumo e salva o gráfico em um arquivo `.png` para você inserir no relatório (no Colab, o arquivo aparece no painel de arquivos à esquerda; clique com o botão direito para baixar).

- Script: [`aula_03.py`](aula_03.py)
- Notebook (Colab): [`aula_03.ipynb`](aula_03.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-03-conclusao-da-oficina-1-e-mini-relatorio-parcial-av/aula_03.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `groupby("periodo")` separa os dados por período; `.agg(...)` calcula várias medidas de uma vez.
- `reindex(ordem)` coloca os períodos na ordem do ano, e não em ordem alfabética.
- `fig.savefig(...)` grava a imagem; use `dpi=150` para boa qualidade de impressão.

## 4. Atividades de fixação

1. Gere a tabela-resumo por período e identifique o período com maior diferença entre máximo e mínimo. Essa diferença é “real” ou há algum problema nos dados?
2. Escreva, em até 4 frases e linguagem acessível, a interpretação do gráfico de linhas da cota para um gestor da Defesa Civil.
3. Liste três limitações do relatório que você produziu.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Estrutura de um mini-relatório (título/fonte, gráficos, tabela, interpretação, limites).
- [ ] Redigir interpretação em linguagem não técnica.
- [ ] Usar `groupby`, `agg` e `savefig`.
- [ ] Reconhecer que valores extremos distorcem mínimos, máximos e amplitudes.
- [ ] Revisar as Aulas 1 e 2 para a **AV1**.

---
[← Voltar ao índice](../../README.md)
