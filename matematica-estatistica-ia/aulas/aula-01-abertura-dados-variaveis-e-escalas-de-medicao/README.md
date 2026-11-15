# Aula 1 — Abertura, dados, variáveis e escalas de medição

| | |
|---|---|
| **Fase do projeto** | Fase 1 — Exploração e leitura de dados |
| **Habilidade** | Interpretar tabelas e gráficos, identificar padrões e resumir conjuntos de dados de forma objetiva. |
| **Objetos de conhecimento** | Leitura de dados. Tipos de variáveis (qualitativas e quantitativas). Escalas. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 10 min | **Acolhida.** Apresentação da ementa (60 h / 20 aulas), do sistema de avaliação (AV1 a AV4) e do projeto integrador “Painel de Indicadores Hidrológicos e Ambientais do Rio Negro”. |
| 40 min | **Aula expositiva dialogada:** o que é um dado; variáveis qualitativas e quantitativas, com exemplos regionais (nível do rio, espécies de peixe, temperatura da água, volume de chuva). |
| 30 min | **Escalas de medição** (nominal, ordinal, intervalar, razão) associadas aos exemplos amazônicos. |
| 70 min | **Prática guiada em duplas:** classificação das variáveis do CSV de cotas do Rio Negro (tipo e escala). |
| 30 min | **Sistematização:** quadro coletivo e registro individual no caderno de bordo do projeto. |

## 2. Conteúdo

### 1. Dado, variável e conjunto de dados

Um **dado** é o registro de uma observação: “a cota do rio foi 24,50 m no dia 15/06”. Uma **variável** é a característica que observamos e que pode mudar de uma observação para outra (a *cota*, a *chuva*, a *espécie* registrada). Um **conjunto de dados** reúne várias observações: cada **linha** é uma observação (um dia) e cada **coluna** é uma variável.

> **📌 Conceito-chave: Dado x informação**
>
> O número 24,50 sozinho é um dado. Quando dizemos “o rio está em nível de alerta alto”, interpretamos o dado: isso é **informação**. Todo o componente de Estatística serve para transformar dados em informação confiável.

### 2. Tipos de variáveis

| Tipo | Subtipo | O que representa | Exemplo no projeto |
|---|---|---|---|
| Qualitativa | Nominal | Categorias **sem** ordem | Espécie de peixe, período hidrológico |
| Qualitativa | Ordinal | Categorias **com** ordem, sem distância definida | Alerta: baixo < médio < alto |
| Quantitativa | Discreta | Contagem: valores inteiros | Nº de dias de chuva no mês |
| Quantitativa | Contínua | Medição: qualquer valor num intervalo | Cota (m), temperatura (°C), chuva (mm) |

Uma pergunta que resolve a maioria dos casos: **“posso fazer conta com esse valor?”** Se a resposta for não (espécie, bairro), é qualitativa. Se for sim, é quantitativa, e a pergunta seguinte é: ela vem de **contar** (discreta) ou de **medir** (contínua)?

### 3. Escalas de medição

A escala diz **que operações fazem sentido** com a variável. Ela é mais fina que o tipo e orienta a escolha de gráficos, medidas e modelos.

| Escala | Tem ordem? | Distâncias iguais? | Zero absoluto? | Exemplo | Pode calcular… |
|---|---|---|---|---|---|
| Nominal | Não | — | — | Espécie de peixe | contagens, moda |
| Ordinal | Sim | Não | — | Alerta (baixo/médio/alto) | mediana, ordem |
| Intervalar | Sim | Sim | Não | Temperatura em °C | diferenças, média |
| Razão | Sim | Sim | Sim | Cota em m; chuva em mm | tudo, inclusive razões |

> **⚠️ Atenção: Zero absoluto**
>
> Em 0 mm de chuva **não choveu**: o zero indica ausência, então 60 mm é o dobro de 30 mm (escala de razão). Já 0 °C **não** é “ausência de temperatura”: é só um ponto de referência; por isso 30 °C não é “o dobro” de 15 °C (escala intervalar).

> **📝 Exemplo resolvido: classificando a variável cota_metros**
>
> **1)** Posso fazer conta com ela? Sim → quantitativa.
>
> **2)** Vem de contar ou de medir? Medir (admite 24,53 m) → contínua.
>
> **3)** Tem zero absoluto? Sim, 0 m é ausência de altura da lâmina d’água na régua → escala de razão.
>
> **Resposta:** quantitativa contínua, escala de razão.

> **💡 Dica: conexão com IA**
>
> Antes de treinar qualquer modelo é preciso saber o tipo de cada coluna: variáveis qualitativas são **codificadas** em números e variáveis quantitativas são **normalizadas**. Classificar errado leva a médias sem sentido (por exemplo, “média” do alerta) e a modelos mal treinados.

## 3. Prática em Python

Vamos carregar o CSV do projeto e descobrir o que o Python “enxerga” em cada coluna. Execute a célula e responda: qual coluna tem dados ausentes e por quê?

- Script: [`aula_01.py`](aula_01.py)
- Notebook (Colab): [`aula_01.ipynb`](aula_01.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-01-abertura-dados-variaveis-e-escalas-de-medicao/aula_01.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `df.shape` mostra (linhas, colunas): 365 dias e 7 variáveis.
- `df.dtypes` mostra o tipo técnico de cada coluna; ele ajuda, mas **não substitui** a sua classificação (alerta aparece como texto, mas é ordinal).
- `especie_coleta` tem muitos valores ausentes (`NaN`): a coleta só acontece uma vez por semana.

## 4. Atividades de fixação

1. Preencha a tabela de classificação das 7 colunas do CSV (tipo, subtipo e escala): `data`, `cota_metros`, `chuva_mm`, `temperatura_c`, `alerta`, `periodo`, `especie_coleta`.
2. Quantas linhas e colunas tem a base? Quantos valores ausentes há em `especie_coleta` e por que existem?
3. Classifique (tipo e escala): (a) número de embarcações no porto; (b) velocidade da correnteza em m/s; (c) cor predominante da água; (d) turbidez em baixa/média/alta; (e) o ano de cada medição.
4. Por que não faz sentido calcular a “média” da coluna `alerta`? E da coluna `especie_coleta`? Qual medida resumiria cada uma?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir dado, variável e conjunto de dados com exemplo do Rio Negro.
- [ ] Explicar a diferença entre variável discreta e contínua.
- [ ] Citar as 4 escalas e dizer o que cada uma permite calcular.
- [ ] Explicar a diferença entre zero absoluto (razão) e zero convencional (intervalar).
- [ ] Usar `df.shape`, `df.dtypes`, `df.isna().sum()` e interpretar a saída.

---
[← Voltar ao índice](../../README.md)
