# Aula 9 — Correlação não é causalidade — Oficina 2 e AV2

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Interpretar a relação entre variáveis por meio de gráficos de dispersão, covariância e correlação, distinguindo associação de causalidade. |
| **Objetos de conhecimento** | Correlação e causalidade. Variáveis de confusão. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | **AV2** — avaliação desta aula, cobrindo as Aulas 4 a 9 (ver Parte III): 8 objetivas, 2 discursivas e prática em Python. |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada** das Aulas 7 e 8. |
| 60 min | **Oficina 2 (Estatística do mundo real):** analisar relações do projeto e discutir casos em que correlação não implica causa. |
| 90 min | **Aplicação da AV2** (objetivas, discursivas e prática em Python). |
| 15 min | **Fechamento** e encaminhamento para a Fase 3. |

## 2. Conteúdo

### 1. Correlação sem causa

Duas variáveis podem estar fortemente correlacionadas sem que uma cause a outra. Há quatro explicações possíveis para um r alto:

| Explicação | Exemplo |
|---|---|
| A causa B | Mais chuva na cabeceira → cota mais alta (com defasagem) |
| B causa A | (Causalidade invertida) — inverter o raciocínio, por engano |
| Uma terceira variável causa as duas (**variável de confusão**) | A estação do ano altera a cota **e** a temperatura da água |
| Coincidência | Duas séries que apenas crescem com o tempo |

### 2. Caso do projeto: cota e temperatura

r = -0,924: forte. Mas é improvável que a cota “esfrie” a água: a **estação do ano** move as duas variáveis. Controlar a estação (comparar dias do mesmo período) reduz muito a associação.

### 3. Caso clássico: sorvete e afogamentos

Num experimento simulado, vendas de sorvete e afogamentos têm r = 0,535. Ao **controlar a temperatura (calor)**, r cai para 0,008. O calor é a **variável de confusão**: leva mais gente à praia e a comprar sorvete.

> **📌 Conceito-chave: como estabelecer causalidade?**
>
> Correlação é o ponto de partida, não de chegada. Para sustentar causa: **experimento controlado** (com grupo de comparação e atribuição aleatória), **mecanismo plausível**, **ordem temporal** (causa antes do efeito) e **controle de variáveis de confusão**.

> **⚠️ Atenção: linguagem cuidadosa em relatórios**
>
> Prefira “**está associado a**” ou “**anda junto com**” a “**causa**” ou “**provoca**” quando só há dados observacionais.

## 3. Prática em Python

Compare uma correlação forte, uma fraca, uma que “anda junto” só por tendência temporal e um caso de variável de confusão simulado.

- Script: [`aula_09.py`](aula_09.py)
- Notebook (Colab): [`aula_09.ipynb`](aula_09.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-09-correlacao-nao-e-causalidade-oficina-2-e-av2/aula_09.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `cota × dia do ano` tem r = 0,943 apenas na fase de enchente: ambos crescem com o tempo.
- `sorvete × afogamentos` cai de 0,535 para 0,008 quando se controla o calor (dados **fictícios**).
- r próximo de zero não prova ausência de relação (pode ser não linear ou defasada).

## 4. Atividades de fixação

1. Um estudo encontrou correlação r = 0,85 entre o número de jogadores online e as quedas de energia em uma cidade. Liste duas explicações não causais possíveis.
2. Explique, com suas palavras, o que é variável de confusão e dê um exemplo do Rio Negro.
3. Reescreva a frase “o aumento da temperatura reduz a cota do rio” de modo cientificamente mais cuidadoso.
4. Cite três condições que reforçam um argumento de causalidade.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir variável de confusão e dar exemplos.
- [ ] Listar as explicações possíveis para um r alto.
- [ ] Redigir conclusões com linguagem adequada (associação × causa).
- [ ] Revisar toda a Fase 2 (Aulas 4 a 8) para a **AV2**.

---
[← Voltar ao índice](../../README.md)
