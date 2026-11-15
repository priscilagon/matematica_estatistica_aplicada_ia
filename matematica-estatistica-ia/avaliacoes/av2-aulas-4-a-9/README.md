# AV2 — Medidas descritivas, variação, quartis, outliers, normalização, covariância e correlação

| | |
|---|---|
| **Aplicação** | Aula 9 |
| **Conteúdo** | Aulas 4 a 9 |
| **Pontuação** | Parte A: 4,0 · Parte B: 3,0 · Parte C: 3,0 · **Total: 10,0** |

**Regras:** calculadora simples permitida nas Partes A e B. Na Parte C é permitido consultar a apostila e a documentação das bibliotecas; não é permitido consultar colegas nem pedir o código a ferramentas de IA. Mostre o raciocínio.

## Parte A — Questões objetivas (4,0 pt)

**Questão 1.** A cota de cinco dias foi 20, 22, 23, 25 e 30 m. A média é:

- (A) 22 m
- (B) 23 m
- (C) 24 m
- (D) 25 m
- (E) 26 m

**Questão 2.** Os valores 12, 15, 15, 18, 22 e 30 estão ordenados. A mediana é:

- (A) 15 m
- (B) 16,5 m
- (C) 18 m
- (D) 18,67 m
- (E) 22 m

**Questão 3.** A amplitude dos valores 14, 19, 11, 25 e 16 é:

- (A) 11
- (B) 14
- (C) 19
- (D) 25
- (E) 36

**Questão 4.** Uma amostra de n = 10 tem soma dos quadrados dos desvios igual a 90. A variância amostral é:

- (A) 8
- (B) 9
- (C) 10
- (D) 11
- (E) 90

**Questão 5.** Para o mesmo conjunto de dados, é correto afirmar que:

- (A) O desvio-padrão amostral é menor que o populacional
- (B) Os dois são sempre iguais
- (C) A variância é medida na mesma unidade dos dados
- (D) A variância é sempre menor que o desvio-padrão
- (E) O desvio-padrão amostral é maior ou igual ao populacional

**Questão 6.** Para o conjunto 12, 14, 15, 16, 17, 18, 19, 21, 45 (Q1 = 14,5; Q3 = 20; IQR = 5,5), o limite superior de Tukey e a conclusão são:

- (A) 28,25; o valor 45 é outlier
- (B) 28,25; não há outliers
- (C) 31,50; o valor 45 é outlier
- (D) 20; todos os valores são outliers
- (E) 45; o valor 45 é o limite

**Questão 7.** O coeficiente de correlação entre cota e temperatura da água foi r = −0,9. A interpretação mais adequada é:

- (A) Se a temperatura sobe, a cota sobe em 90%
- (B) A cota causa a queda da temperatura
- (C) Há forte relação linear negativa: cota alta tende a coincidir com temperatura baixa, sem provar causa
- (D) Não existe relação entre as variáveis
- (E) Só 9% dos dias têm relação

**Questão 8.** Qual das alternativas descreve corretamente uma variável de confusão?

- (A) Terceira variável que influencia as duas analisadas e cria uma associação aparente
- (B) Variável com muitos valores ausentes
- (C) Variável que só assume dois valores
- (D) Erro de digitação em uma coluna
- (E) Variável sempre qualitativa

## Parte B — Questões discursivas (3,0 pt)

**Questão 9.** As leituras de cota de uma semana foram 15, 17, 17, 20, 21, 25 (m). Calcule a média, a mediana, a moda, a amplitude, a variância e o desvio-padrão (populacionais e amostrais) e escreva uma frase interpretando o desvio-padrão amostral.

**Questão 10.** Na base do projeto, a cota na cheia tem média 27,81 m e desvio-padrão amostral 0,594 m; na seca, média 16,26 m e desvio-padrão 0,334 m. Compare os períodos quanto ao nível e à previsibilidade e explique por que a amplitude da enchente (17,8 m) exige cuidado.

## Parte C — Prática em Python (3,0 pt)

Em Python: (a) para a série 15, 17, 17, 20, 21, 25 calcule média, mediana, amplitude e as variâncias e desvios (ddof = 0 e ddof = 1); (b) calcule os limites de Tukey para `temperatura_c` e liste as leituras atípicas; (c) calcule r entre cota e temperatura **sem** a leitura atípica; (d) compare média e DP da cota na cheia e na seca. Responda em comentários: por que a leitura de 22/10 deve ser investigada?

**Apoio:**

- `np.var(x, ddof=1)`, `np.std(x, ddof=0)`.
- `quantile([.25, .75])`; filtre com `(t < li) | (t > ls)`.
- Para r, filtre `df["temperatura_c"] < 35` e use `.corr()`.

**Critérios de avaliação da Parte C**

| Critério | Pontos |
|---|---|
| (a) todas as medidas, com ddof correto | 0,75 |
| (b) limites 25,55 e 31,55 e a leitura 38,5 °C | 0,75 |
| (c) r = −0,924 | 0,50 |
| (d) média e DP por período | 0,50 |
| Comentário: 38,5 °C é fisicamente improvável (sensor/anotação); atípico não é sempre erro | 0,50 |

