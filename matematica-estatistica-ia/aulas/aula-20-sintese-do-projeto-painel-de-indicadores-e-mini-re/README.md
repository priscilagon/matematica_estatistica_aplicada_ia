# Aula 20 — Síntese do projeto: painel de indicadores e mini-relatório final — AV4

| | |
|---|---|
| **Fase do projeto** | Fase 4 — Fundamentos matemáticos da IA e síntese |
| **Habilidade** | Integrar conceitos de matemática e estatística na análise de dados, comunicando resultados com clareza e responsabilidade. |
| **Objetos de conhecimento** | Integração dos objetos de conhecimento do componente. Comunicação de resultados. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | **AV4** — mini-relatório final do projeto integrador e avaliação dos conceitos das Aulas 17 a 20 (ver Parte III). |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** geral do componente e orientações sobre a AV4. |
| 105 min | **Elaboração do painel e do mini-relatório final** por grupo (Python + texto). |
| 45 min | **Apresentação** dos painéis (3 min por grupo) e feedback. |
| 15 min | **Encerramento:** autoavaliação socioemocional e fechamento do caderno de bordo. |

## 2. Conteúdo

### 1. O painel de indicadores

O projeto integrador culmina em um **painel**: poucas tabelas e gráficos que respondem a uma pergunta de forma honesta. Estrutura recomendada:

1. **Contexto e dados:** fonte, período, limites (base didática simulada).
2. **Tratamento:** o que foi feito com os atípicos e por quê.
3. **Indicadores por período:** média, mediana, DP, mínimo e máximo.
4. **Relações:** correlação cota × temperatura e ressalva sobre causalidade.
5. **Incerteza:** IC da média e comparação entre grupos (p-valor).
6. **Conclusão e limites:** o que os dados permitem e não permitem afirmar.

### 2. Exemplo de tabela de indicadores (dados tratados)

| Período | Dias | Média (m) | Mediana (m) | DP (m) | Mín. (m) | Máx. (m) |
|---|---|---|---|---|---|---|
| enchente | 150 | 21,29 | 21,14 | 3,16 | 16,43 | 26,70 |
| cheia | 92 | 27,81 | 27,98 | 0,59 | 26,38 | 28,60 |
| vazante | 60 | 21,65 | 21,95 | 2,70 | 17,40 | 26,27 |
| seca | 60 | 16,26 | 16,13 | 0,33 | 15,92 | 17,27 |

Correlação cota × temperatura: **r = -0,943**. Temperatura média: **28,56 °C** (IC95%: **28,47 a 28,65 °C**). Tratamento: removidas as leituras com cota fora de 10–33 m e temperatura ≥ 35 °C.

> **💡 Dica: honestidade analítica**
>
> Um bom relatório **registra o tratamento dos dados**, mostra incerteza (IC), usa linguagem de associação e lista as limitações. Resultados bonitos com procedimentos escondidos não são ciência de dados.

### 3. Autoavaliação socioemocional

Registre no caderno de bordo: (1) uma dificuldade que você superou; (2) como colaborou com o grupo; (3) uma situação em que mudou de ideia por causa dos dados; (4) o que ainda quer aprender.

## 3. Prática em Python

A célula produz a tabela de indicadores, a correlação, o IC e salva o gráfico-síntese `painel_rio_negro.png`.

- Script: [`aula_20.py`](aula_20.py)
- Notebook (Colab): [`aula_20.ipynb`](aula_20.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-20-sintese-do-projeto-painel-de-indicadores-e-mini-re/aula_20.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `d` guarda os dados tratados; sempre registre o critério.
- `groupby` + `agg` gera a tabela em poucas linhas.
- O arquivo `painel_rio_negro.png` pode ser inserido no relatório.

## 4. Atividades de fixação

1. Rode o código e reproduza a tabela de indicadores. Qual período tem maior e qual tem menor DP depois do tratamento?
2. Escreva um parágrafo de conclusão (5 a 7 linhas) que use pelo menos três medidas do painel e uma ressalva.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Estrutura de um relatório de análise de dados.
- [ ] Registrar o tratamento aplicado aos dados.
- [ ] Comunicar incerteza (IC) e limitações.
- [ ] Revisar as Aulas 17 a 19 para a **AV4**.

---
[← Voltar ao índice](../../README.md)
