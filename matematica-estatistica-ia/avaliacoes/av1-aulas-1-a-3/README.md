# AV1 — Leitura de dados, tipos de variáveis, escalas, tabelas e gráficos

| | |
|---|---|
| **Aplicação** | Aula 3 |
| **Conteúdo** | Aulas 1 a 3 |
| **Pontuação** | Parte A: 4,0 · Parte B: 3,0 · Parte C: 3,0 · **Total: 10,0** |

**Regras:** calculadora simples permitida nas Partes A e B. Na Parte C é permitido consultar a apostila e a documentação das bibliotecas; não é permitido consultar colegas nem pedir o código a ferramentas de IA. Mostre o raciocínio.

## Parte A — Questões objetivas (4,0 pt)

**Questão 1.** A coluna `alerta` do CSV registra os níveis baixo, médio e alto. Essa variável é classificada como:

- (A) Quantitativa discreta, escala de razão
- (B) Qualitativa nominal, escala nominal
- (C) Qualitativa ordinal, escala ordinal
- (D) Quantitativa contínua, escala intervalar
- (E) Quantitativa contínua, escala de razão

**Questão 2.** A variável `cota_metros` (nível do rio em metros) é classificada como:

- (A) Quantitativa contínua, escala de razão
- (B) Quantitativa discreta, escala de razão
- (C) Qualitativa ordinal, escala ordinal
- (D) Quantitativa contínua, escala nominal
- (E) Qualitativa nominal, escala nominal

**Questão 3.** Qual gráfico é o mais adequado para comparar a variabilidade da cota entre os quatro períodos hidrológicos e destacar valores extremos?

- (A) Gráfico de setores
- (B) Gráfico de barras das médias
- (C) Gráfico de linhas
- (D) Boxplot por período
- (E) Tabela de frequência simples

**Questão 4.** Em 53 coletas semanais, o pirarucu foi registrado 6 vezes. A frequência relativa do pirarucu é, aproximadamente:

- (A) 6,0%
- (B) 11,3%
- (C) 15,1%
- (D) 26,4%
- (E) 41,5%

**Questão 5.** Sobre a temperatura da água em °C, é correto afirmar que:

- (A) É de escala de razão, logo 30 °C é o dobro de 15 °C
- (B) É qualitativa ordinal
- (C) É de escala nominal
- (D) Só admite valores inteiros
- (E) É de escala intervalar: o zero é convencional e não indica ausência de temperatura

**Questão 6.** A principal diferença entre um histograma e um gráfico de barras é que o histograma:

- (A) Usa sempre cores diferentes
- (B) Mostra categorias nominais
- (C) Representa intervalos (classes) de uma variável quantitativa contínua, com barras coladas
- (D) Só pode ser feito em planilha
- (E) Mostra a evolução no tempo

**Questão 7.** A coluna `especie_coleta` tem 312 valores ausentes (NaN) entre 365 linhas. A explicação correta é:

- (A) A coleta de espécies era semanal; nos demais dias não houve registro
- (B) Houve erro de digitação em 312 dias
- (C) A coluna é quantitativa e não aceita texto
- (D) O Python apagou os dados ao ler o CSV
- (E) O rio estava seco nesses dias

**Questão 8.** Em um mini-relatório de dados, a seção “Limites” serve para:

- (A) Mostrar apenas os pontos positivos
- (B) Repetir os gráficos em tabela
- (C) Listar o nome dos autores
- (D) Declarar o que os dados não permitem concluir (ex.: base de um único ano, base simulada)
- (E) Substituir a interpretação

## Parte B — Questões discursivas (3,0 pt)

**Questão 9.** Classifique as variáveis `chuva_mm`, `periodo` e `especie_coleta` quanto ao tipo (qualitativa/quantitativa e subtipo) e à escala de medição, justificando cada classificação em uma frase.

**Questão 10.** Observe o gráfico de linhas da cota diária de 2025 e escreva um parágrafo de 3 a 5 linhas, em linguagem acessível a um gestor, descrevendo o padrão e apontando um ponto que merece investigação.

## Parte C — Prática em Python (3,0 pt)

No Google Colab, carregue `rio_negro_cotas.csv` e: (a) mostre o número de linhas e colunas e a quantidade de valores ausentes por coluna; (b) crie a tabela com dias, mínimo, máximo e média da cota por período, na ordem do ano; (c) conte os dias de cada nível de alerta; (d) gere um boxplot da cota por período e salve a imagem. Escreva duas frases interpretando a tabela.

**Apoio:**

- Use `pd.read_csv(..., parse_dates=["data"])`.
- `groupby("periodo")[...].agg(...)` e `.reindex(ordem)`.
- `value_counts()` conta categorias; `df.boxplot(column=..., by=...)` faz o gráfico.

**Critérios de avaliação da Parte C**

| Critério | Pontos |
|---|---|
| Leitura correta e (a) shape + ausentes | 0,50 |
| (b) tabela por período, na ordem correta | 0,75 |
| (c) contagem dos alertas | 0,25 |
| (d) boxplot com título e arquivo salvo | 0,50 |
| Interpretação em 2 frases (cita enchente/vazante com mínimo/máximo atípicos) | 0,50 |
| Código organizado e executa sem erros | 0,50 |

