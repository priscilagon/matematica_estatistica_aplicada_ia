# Gabarito oficial — AV3

> **Uso exclusivo do professor.** Não publique em repositório público antes da aplicação.

**Aplicação:** Aula 16 · **Conteúdo:** Aulas 10 a 16

## Parte A — Objetivas

| Questão | Resposta | Justificativa |
|---|---|---|
| 1 | **B** | 0,40 + 0,30 − 0,10 = 0,60. |
| 2 | **C** | P(A\|B) = 0,10 ÷ 0,30 = 1/3. |
| 3 | **C** | P(alarme) = 0,9×0,1 + 0,1×0,9 = 0,18; posteriori = 0,09 ÷ 0,18 = 0,50. |
| 4 | **C** | z = (30 − 24) ÷ 3 = 2. |
| 5 | **C** | C(5,2)·0,5⁵ = 10 ÷ 32 = 0,3125. |
| 6 | **A** | P(0) = e⁻³ ≈ 0,0498. |
| 7 | **B** | Viés de seleção é sistemático; mais dados do mesmo viés não o corrigem. |
| 8 | **D** | p < α → rejeita-se H₀; p-valor não é a probabilidade de H₀ nem mede a importância prática. |

## Parte B — Discursivas

### Questão 9

Um sistema de alerta detecta 90% das cheias reais (sensibilidade) e dispara falso alarme em 8% dos dias sem cheia. Se uma cheia ocorre em apenas 5% dos dias, calcule P(cheia | alarme) e explique por que o resultado surpreende.

> **Resposta-modelo**
>
> P(alarme) = 0,90×0,05 + 0,08×0,95 = 0,045 + 0,076 = **0,121**.
>
> P(cheia | alarme) = 0,045 ÷ 0,121 = **0,3719** (≈ 37%).
>
> Explicação: como a cheia é rara, os falsos positivos dos muitos dias normais superam os acertos; mais da metade dos alarmes é falsa, apesar de o sistema ser “bom” (90%/92%). É o problema da taxa-base.

| Rubrica | Pontos |
|---|---|
| Probabilidade total correta | 0,40 |
| Aplicação correta de Bayes e resultado | 0,50 |
| Explicação da taxa-base / falsos positivos | 0,50 |
| Clareza | 0,10 |
| **Total** | **1,50** |

### Questão 10

Com os 92 dias da cheia, a cota tem média 27,814 m e DP amostral 0,594 m, e o IC de 95% para a média é [27,691 ; 27,937]. Interprete o intervalo corretamente, diga o que mudaria com mais dias de observação e aponte uma interpretação **incorreta** comum.

> **Resposta-modelo**
>
> O método usado produz intervalos que contêm a média verdadeira em 95% das amostras possíveis; a estimativa da média da cota na cheia vai de 27,69 a 27,94 m.
>
> Com mais observações, o erro-padrão (s ÷ √n) diminui e o intervalo fica **mais estreito** (maior precisão).
>
> Interpretação incorreta: “há 95% de probabilidade de a média verdadeira estar neste intervalo” ou “95% dos dias estão neste intervalo” — o IC é sobre a **média**, não sobre os dias individuais.

| Rubrica | Pontos |
|---|---|
| Interpretação correta do IC | 0,60 |
| Efeito de n na largura | 0,50 |
| Cita equívoco comum e o corrige | 0,40 |
| **Total** | **1,50** |

## Parte C — Prática

Em Python, defina A = alerta “alto” e E = chuva > 10 mm e calcule P(A), P(E), P(A | E) e P(E | A). Calcule o IC de 95% da cota na cheia e P(X ≥ 15) para o número de dias com alerta alto em 30 dias (Binomial). Comente, em duas frases, por que P(A | E) ≠ P(E | A).

Solução de referência: [`solucao_parte_c.py`](solucao_parte_c.py)

**Saída esperada**

```text
P(alto) = 0.3425
P(chuva>10) = 0.2521
P(alto | chuva>10) = 0.3696
P(chuva>10 | alto) = 0.2720
cheia: n=92 média=27.814 dp=0.594 IC95%=[27.691 ; 27.937]
P(X>=15 dias altos em 30) = 0.0546
```

> **Interpretação esperada**
>
> P(A|E) = 0,3696 responde “entre os dias de chuva forte, quantos têm alerta alto”; P(E|A) = 0,2720 responde “entre os dias de alerta alto, quantos têm chuva forte”. Os denominadores são diferentes (E tem 92 dias; A tem 125).

| Critério | Pontos |
|---|---|
| P(A) e P(E) corretas | 0,50 |
| P(A\|E) e P(E\|A) corretas | 0,75 |
| IC da cheia | 0,50 |
| P(X ≥ 15) binomial | 0,50 |
| Comentário sobre a diferença entre as condicionais | 0,50 |
| Código organizado | 0,25 |
| **Total** | **3,00** |
