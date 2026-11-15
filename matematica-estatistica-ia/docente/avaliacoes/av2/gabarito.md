# Gabarito oficial — AV2

> **Uso exclusivo do professor.** Não publique em repositório público antes da aplicação.

**Aplicação:** Aula 9 · **Conteúdo:** Aulas 4 a 9

## Parte A — Objetivas

| Questão | Resposta | Justificativa |
|---|---|---|
| 1 | **C** | 120 ÷ 5 = 24 m. |
| 2 | **B** | n = 6: (15 + 18) ÷ 2 = 16,5. |
| 3 | **B** | 25 − 11 = 14. |
| 4 | **C** | s² = 90 ÷ (10 − 1) = 10. |
| 5 | **E** | Dividir por n − 1 (em vez de n) dá um valor maior ou igual; a variância tem unidade ao quadrado. |
| 6 | **A** | 20 + 1,5 × 5,5 = 28,25; 45 > 28,25. |
| 7 | **C** | \|r\| próximo de 1 = forte; sinal negativo = sentido inverso; correlação não prova causa. |
| 8 | **A** | Ex.: o período hidrológico afeta cota e temperatura. |

## Parte B — Discursivas

### Questão 9

As leituras de cota de uma semana foram 15, 17, 17, 20, 21, 25 (m). Calcule a média, a mediana, a moda, a amplitude, a variância e o desvio-padrão (populacionais e amostrais) e escreva uma frase interpretando o desvio-padrão amostral.

> **Resposta-modelo**
>
> Soma = 115; **média = 19,1667 m**; **mediana = 18,5 m**; **moda = 17 m**; **amplitude = 10 m**.
>
> Desvios²: 17,36; 4,69; 4,69; 0,69; 3,36; 34,03 → **SQ = 64,8333**.
>
> **Var. pop.** = 64,8333 ÷ 6 = **10,8056 m²**; **DP pop.** = **3,2872 m**.
>
> **Var. amostral** = 64,8333 ÷ 5 = **12,9667 m²**; **DP amostral** = **3,6009 m**.
>
> Interpretação (modelo): “Na semana, a cota variou tipicamente cerca de 3,6 m em torno da média de 19,2 m.”

| Rubrica | Pontos |
|---|---|
| Média, mediana, moda e amplitude corretas (0,1 cada) | 0,40 |
| SQ e variâncias (pop. e amostral) corretas | 0,40 |
| DPs corretos (pop. e amostral) | 0,40 |
| Interpretação contextualizada com unidade | 0,30 |
| **Total** | **1,50** |

### Questão 10

Na base do projeto, a cota na cheia tem média 27,81 m e desvio-padrão amostral 0,594 m; na seca, média 16,26 m e desvio-padrão 0,334 m. Compare os períodos quanto ao nível e à previsibilidade e explique por que a amplitude da enchente (17,8 m) exige cuidado.

> **Resposta-modelo**
>
> **Nível:** cheia ≈ 11,5 m acima da seca (27,81 × 16,26 m).
>
> **Previsibilidade:** os dois períodos são estáveis (DP < 0,6 m); a seca é a mais estável (0,334 m), mas em ambos o nível de ontem prevê bem o de amanhã. Enchente e vazante têm DP ≈ 3 m: pouco previsíveis.
>
> **Cuidado com a amplitude:** depende só de máximo e mínimo; em enchente, o mínimo (8,90 m) é uma leitura atípica/erro. A amplitude fica inflada; o IQR ou o DP após tratar o atípico são mais confiáveis.

| Rubrica | Pontos |
|---|---|
| Compara níveis com valores corretos | 0,40 |
| Interpreta DP como previsibilidade | 0,40 |
| Explica a sensibilidade da amplitude a atípicos | 0,50 |
| Clareza e linguagem técnica | 0,20 |
| **Total** | **1,50** |

## Parte C — Prática

Em Python: (a) para a série 15, 17, 17, 20, 21, 25 calcule média, mediana, amplitude e as variâncias e desvios (ddof = 0 e ddof = 1); (b) calcule os limites de Tukey para `temperatura_c` e liste as leituras atípicas; (c) calcule r entre cota e temperatura **sem** a leitura atípica; (d) compare média e DP da cota na cheia e na seca. Responda em comentários: por que a leitura de 22/10 deve ser investigada?

Solução de referência: [`solucao_parte_c.py`](solucao_parte_c.py)

**Saída esperada**

```text
média 19.166666666666668 mediana 18.5 amplitude 10
var pop 10.8056 | var am 12.9667
dp pop 3.2872 | dp am 3.6009
Q1 17.73 Q3 26.67
limites temperatura: 25.55 ; 31.55
          data  temperatura_c
294 2025-10-22           38.5
r cota x temp: -0.924
cheia média 27.81 | dp 0.594
seca média 16.26 | dp 0.334
```

> **Interpretação esperada**
>
> O valor de 38,5 °C (22/10) está fora dos limites e é incompatível com a água do rio nessa época: provável erro de sensor ou de registro; deve ser verificado antes de excluir.

| Critério | Pontos |
|---|---|
| (a) todas as medidas, com ddof correto | 0,75 |
| (b) limites 25,55 e 31,55 e a leitura 38,5 °C | 0,75 |
| (c) r = −0,924 | 0,50 |
| (d) média e DP por período | 0,50 |
| Comentário: 38,5 °C é fisicamente improvável (sensor/anotação); atípico não é sempre erro | 0,50 |
| **Total** | **3,00** |
