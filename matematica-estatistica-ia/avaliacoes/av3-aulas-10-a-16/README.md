# AV3 — Probabilidade, Bayes, distribuições, amostragem, intervalo de confiança e p-valor

| | |
|---|---|
| **Aplicação** | Aula 16 |
| **Conteúdo** | Aulas 10 a 16 |
| **Pontuação** | Parte A: 4,0 · Parte B: 3,0 · Parte C: 3,0 · **Total: 10,0** |

**Regras:** calculadora simples permitida nas Partes A e B. Na Parte C é permitido consultar a apostila e a documentação das bibliotecas; não é permitido consultar colegas nem pedir o código a ferramentas de IA. Mostre o raciocínio.

## Parte A — Questões objetivas (4,0 pt)

**Questão 1.** Sejam P(A) = 0,40; P(B) = 0,30 e P(A e B) = 0,10. A probabilidade de ocorrer A ou B é:

- (A) 0,12
- (B) 0,60
- (C) 0,70
- (D) 0,80
- (E) 0,40

**Questão 2.** Com os mesmos valores (P(A) = 0,40; P(B) = 0,30; P(A e B) = 0,10), P(A | B) vale:

- (A) 0,10
- (B) 0,25
- (C) 1/3 ≈ 0,333
- (D) 0,40
- (E) 0,75

**Questão 3.** Um alarme de cheia dispara em 90% das cheias e em 10% dos dias sem cheia. Se a cheia ocorre em 10% dos dias, P(cheia | alarme) é:

- (A) 0,09
- (B) 0,18
- (C) 0,50
- (D) 0,90
- (E) 1,00

**Questão 4.** Se X ~ N(24; 3), o escore z do valor x = 30 é:

- (A) 1
- (B) 1,5
- (C) 2
- (D) 6
- (E) 8

**Questão 5.** Em 5 lançamentos de uma moeda justa, a probabilidade de exatamente 2 caras é:

- (A) 0,1250
- (B) 0,2500
- (C) 0,3125
- (D) 0,4000
- (E) 0,5000

**Questão 6.** Se os alertas chegam a um centro a uma taxa média de 3 por semana (Poisson), a probabilidade de uma semana sem nenhum alerta é aproximadamente:

- (A) 0,0498
- (B) 0,1494
- (C) 0,3679
- (D) 0,5000
- (E) 0,9502

**Questão 7.** Um pesquisador mede a temperatura apenas nos dias de seca e generaliza para o ano todo. Aumentar a amostra de 30 para 300 dias de seca:

- (A) Elimina o viés
- (B) Reduz o erro aleatório, mas não corrige o viés de seleção
- (C) Aumenta o viés
- (D) Torna a amostra normal
- (E) Não altera nada

**Questão 8.** Um teste de hipótese resultou em p = 0,03 com α = 0,05. A conclusão correta é:

- (A) H₀ é verdadeira com probabilidade de 3%
- (B) Não se rejeita H₀
- (C) O efeito é grande e importante
- (D) Rejeita-se H₀: há evidência estatística contra ela
- (E) A hipótese alternativa é verdadeira com 97% de certeza

## Parte B — Questões discursivas (3,0 pt)

**Questão 9.** Um sistema de alerta detecta 90% das cheias reais (sensibilidade) e dispara falso alarme em 8% dos dias sem cheia. Se uma cheia ocorre em apenas 5% dos dias, calcule P(cheia | alarme) e explique por que o resultado surpreende.

**Questão 10.** Com os 92 dias da cheia, a cota tem média 27,814 m e DP amostral 0,594 m, e o IC de 95% para a média é [27,691 ; 27,937]. Interprete o intervalo corretamente, diga o que mudaria com mais dias de observação e aponte uma interpretação **incorreta** comum.

## Parte C — Prática em Python (3,0 pt)

Em Python, defina A = alerta “alto” e E = chuva > 10 mm e calcule P(A), P(E), P(A | E) e P(E | A). Calcule o IC de 95% da cota na cheia e P(X ≥ 15) para o número de dias com alerta alto em 30 dias (Binomial). Comente, em duas frases, por que P(A | E) ≠ P(E | A).

**Apoio:**

- Média de booleanos = proporção.
- `stats.t.interval(0.95, df=n-1, loc=m, scale=s/np.sqrt(n))`.
- `stats.binom.sf(14, 30, p)` é P(X ≥ 15).

**Critérios de avaliação da Parte C**

| Critério | Pontos |
|---|---|
| P(A) e P(E) corretas | 0,50 |
| P(A\|E) e P(E\|A) corretas | 0,75 |
| IC da cheia | 0,50 |
| P(X ≥ 15) binomial | 0,50 |
| Comentário sobre a diferença entre as condicionais | 0,50 |
| Código organizado | 0,25 |

