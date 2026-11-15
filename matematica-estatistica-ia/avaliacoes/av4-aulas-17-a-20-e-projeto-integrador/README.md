# AV4 — Vetores, matrizes, produto escalar, modelos, gradiente descendente e mini-relatório final

| | |
|---|---|
| **Aplicação** | Aula 20 |
| **Conteúdo** | Aulas 17 a 20 e projeto integrador |
| **Pontuação** | Parte A: 3,0 · Parte B: 2,0 · Parte C: 5,0 · **Total: 10,0** |

**Regras:** calculadora simples permitida nas Partes A e B. Na Parte C é permitido consultar a apostila e a documentação das bibliotecas; não é permitido consultar colegas nem pedir o código a ferramentas de IA. Mostre o raciocínio.

## Parte A — Questões objetivas (3,0 pt)

**Questão 1.** Uma matriz X tem 364 linhas e 3 colunas. Sobre ela, é correto afirmar:

- (A) Tem 3 observações e 364 features
- (B) Tem 364 observações e 3 features
- (C) Não pode ser transposta
- (D) Tem 364 + 3 elementos
- (E) É um vetor

**Questão 2.** O produto escalar [1, −2, 3] · [4, 0, −1] é:

- (A) −1
- (B) 0
- (C) 1
- (D) 5
- (E) 7

**Questão 3.** Se A é 5 × 3 e B é 3 × 4, então A·B:

- (A) É 5 × 4
- (B) Não existe
- (C) É 3 × 3
- (D) É 4 × 5
- (E) É 5 × 3

**Questão 4.** Em um modelo ŷ = w·x + b, o parâmetro w representa:

- (A) A taxa de aprendizado
- (B) O erro de previsão
- (C) Os pesos (importância) de cada feature
- (D) O número de observações
- (E) O valor previsto

**Questão 5.** Sobre a função de perda EQM, é correto dizer que:

- (A) Quanto maior, melhor o modelo
- (B) É sempre negativa
- (C) Não depende dos parâmetros
- (D) Só serve para classificação
- (E) É a média dos quadrados dos erros e deve ser reduzida no treino

**Questão 6.** Em um ponto onde a derivada da loss em relação a w é positiva e igual a 5, com taxa α = 0,1, o gradiente descendente faz:

- (A) w aumentar em 0,5
- (B) w diminuir em 0,5
- (C) w ficar igual
- (D) w dobrar
- (E) a taxa mudar

**Questão 7.** Uma taxa de aprendizado excessivamente grande (ex.: 1,1 no exemplo da aula) tende a:

- (A) Fazer o treino oscilar ou divergir
- (B) Convergir mais rápido sempre
- (C) Zerar os pesos
- (D) Eliminar o overfitting
- (E) Padronizar os dados

**Questão 8.** O overfitting acontece quando o modelo:

- (A) Erra igualmente em treino e teste
- (B) Não consegue aprender nada
- (C) Usa poucos parâmetros
- (D) Ajusta-se tão bem ao treino (inclusive ao ruído) que generaliza mal para dados novos
- (E) Tem loss zero no teste

## Parte B — Questões discursivas (2,0 pt)

**Questão 9.** Considere o modelo ŷ = w·x, com x = [1, 2, 3] e y = [2, 4, 6]. Para w = 1 e taxa α = 0,1, calcule a loss, o gradiente e o novo valor de w. Em seguida, diga qual é o w ótimo e por quê.

**Questão 10.** Explique, em um parágrafo, o laço de treinamento de um modelo (prever, medir o erro, corrigir) e dois cuidados necessários para que o treino funcione bem.

## Parte C — Mini-relatório final (5,0 pt)

**Mini-relatório final (individual ou em dupla).** Em Python: (a) multiplique C = [[2, 0], [1, 3]] por D = [[1, 4], [2, 5]]; (b) implemente 3 passos de gradiente descendente para x = [1, 2, 3], y = [2, 4, 6], w = 1 e α = 0,1, mostrando w, loss e gradiente a cada passo; (c) gere a tabela de indicadores da cota por período usando os dados **tratados** (temperatura < 35 °C e cota entre 10 e 33 m) e a correlação cota × temperatura. Redija um parágrafo de conclusão (5 a 7 linhas) com ressalvas sobre causalidade e sobre a base simulada.

**Apoio:**

- `C @ D` é o produto matricial.
- Siga o modelo da Aula 19.
- `d = df[(df["temperatura_c"] < 35) & (df["cota_metros"].between(10, 33))]`.

**Critérios de avaliação da Parte C**

| Critério | Pontos |
|---|---|
| (a) produto matricial correto | 0,50 |
| (b) 3 passos corretos (w converge para ≈ 2) | 1,00 |
| (c) tabela de indicadores por período com dados tratados | 1,00 |
| (c) correlação r = −0,943 e registro do tratamento | 0,50 |
| Conclusão: uso correto de medidas, linguagem de associação, ressalvas | 1,50 |
| Organização, legibilidade e execução sem erros | 0,50 |

