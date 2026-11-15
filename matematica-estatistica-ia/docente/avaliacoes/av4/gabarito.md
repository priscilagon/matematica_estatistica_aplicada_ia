# Gabarito oficial — AV4

> **Uso exclusivo do professor.** Não publique em repositório público antes da aplicação.

**Aplicação:** Aula 20 · **Conteúdo:** Aulas 17 a 20 e projeto integrador

## Parte A — Objetivas

| Questão | Resposta | Justificativa |
|---|---|---|
| 1 | **B** | Linhas = observações; colunas = features. Dimensão 364 × 3. |
| 2 | **C** | 4 + 0 − 3 = 1. |
| 3 | **A** | Colunas de A (3) = linhas de B (3); resultado 5 × 4. |
| 4 | **C** | w é o vetor de pesos; b é o viés. |
| 5 | **E** | EQM = média de (previsto − real)²; treinar = minimizá-lo. |
| 6 | **B** | w_novo = w − 0,1×5 = w − 0,5. |
| 7 | **A** | Passos grandes ultrapassam o mínimo e a loss pode explodir. |
| 8 | **D** | Bom no treino e ruim em dados novos. |

## Parte B — Discursivas

### Questão 9

Considere o modelo ŷ = w·x, com x = [1, 2, 3] e y = [2, 4, 6]. Para w = 1 e taxa α = 0,1, calcule a loss, o gradiente e o novo valor de w. Em seguida, diga qual é o w ótimo e por quê.

> **Resposta-modelo**
>
> Erros (ŷ − y) = −1, −2, −3. **Loss** = (1 + 4 + 9) ÷ 3 = **4,6667**.
>
> **Gradiente** = 2·média(erro·x) = 2·(−1 − 4 − 9) ÷ 3 = **-9,3333**.
>
> **w novo** = 1 − 0,1·(-9,3333) = **1,9333**.
>
> **w ótimo = 2:** com w = 2 todas as previsões coincidem com y (loss = 0).

| Rubrica | Pontos |
|---|---|
| Loss correta | 0,25 |
| Gradiente correto | 0,25 |
| Atualização de w correta | 0,25 |
| w ótimo e justificativa | 0,25 |
| **Total** | **1,00** |

### Questão 10

Explique, em um parágrafo, o laço de treinamento de um modelo (prever, medir o erro, corrigir) e dois cuidados necessários para que o treino funcione bem.

> **Resposta-modelo**
>
> Esperado: o modelo faz previsões; calcula-se a loss; calcula-se o gradiente; atualizam-se os pesos na direção que reduz a loss; repete-se até convergir. Cuidados (dois): escolher taxa de aprendizado adequada; padronizar/normalizar as features; tratar outliers; separar dados de teste para evitar overfitting.

| Rubrica | Pontos |
|---|---|
| Descreve as etapas na ordem correta | 0,40 |
| Dois cuidados corretos e justificados (0,2 cada) | 0,40 |
| Clareza e vocabulário técnico | 0,20 |
| **Total** | **1,00** |

## Parte C — Mini-relatório

**Mini-relatório final (individual ou em dupla).** Em Python: (a) multiplique C = [[2, 0], [1, 3]] por D = [[1, 4], [2, 5]]; (b) implemente 3 passos de gradiente descendente para x = [1, 2, 3], y = [2, 4, 6], w = 1 e α = 0,1, mostrando w, loss e gradiente a cada passo; (c) gere a tabela de indicadores da cota por período usando os dados **tratados** (temperatura < 35 °C e cota entre 10 e 33 m) e a correlação cota × temperatura. Redija um parágrafo de conclusão (5 a 7 linhas) com ressalvas sobre causalidade e sobre a base simulada.

Solução de referência: [`solucao_parte_c.py`](solucao_parte_c.py)

**Saída esperada**

```text
[[ 2  8]
 [ 7 19]]
passo 0: w=1.0000 loss=4.6667 grad=-9.3333
passo 1: w=1.9333 loss=0.0207 grad=-0.6222
passo 2: w=1.9956 loss=0.0001 grad=-0.0415
w após 3 passos: 1.9997
          count   mean  median   std
periodo                             
cheia        92  27.81   27.98  0.59
enchente    150  21.29   21.14  3.16
seca         60  16.26   16.13  0.33
vazante      60  21.65   21.95  2.70
r = -0.943
```

> **Interpretação esperada**
>
> Esperado no parágrafo: cheia alta e estável (≈ 27,8 m, DP 0,59); seca baixa e estável (≈ 16,3 m, DP 0,33); enchente e vazante com maior variação (DP ≈ 2,7 a 3,2 m); correlação negativa forte entre cota e temperatura (−0,94), sem afirmar causa (sazonalidade); base simulada, um ano.

| Critério | Pontos |
|---|---|
| (a) produto matricial correto | 0,50 |
| (b) 3 passos corretos (w converge para ≈ 2) | 1,00 |
| (c) tabela de indicadores por período com dados tratados | 1,00 |
| (c) correlação r = −0,943 e registro do tratamento | 0,50 |
| Conclusão: uso correto de medidas, linguagem de associação, ressalvas | 1,50 |
| Organização, legibilidade e execução sem erros | 0,50 |
| **Total** | **5,00** |
