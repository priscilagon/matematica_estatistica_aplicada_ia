# Gabarito oficial — AV1

> **Uso exclusivo do professor.** Não publique em repositório público antes da aplicação.

**Aplicação:** Aula 3 · **Conteúdo:** Aulas 1 a 3

## Parte A — Objetivas

| Questão | Resposta | Justificativa |
|---|---|---|
| 1 | **C** | As categorias têm ordem (baixo < médio < alto), mas a distância entre elas não está definida: qualitativa ordinal. |
| 2 | **A** | É uma medida numérica que admite valores fracionários (contínua), com zero absoluto (razão). |
| 3 | **D** | O boxplot por categoria resume mediana, quartis e valores atípicos de cada grupo. |
| 4 | **B** | 6 ÷ 53 = 0,113 → 11,3%. |
| 5 | **E** | Em °C o zero é uma convenção; por isso a escala é intervalar e não faz sentido falar em “dobro”. |
| 6 | **C** | Histograma: classes de variável contínua. Barras: categorias. |
| 7 | **A** | Foram 53 coletas semanais; ausente significa “sem coleta no dia”. |
| 8 | **D** | Limitações explicam a abrangência e evitam conclusões exageradas. |

## Parte B — Discursivas

### Questão 9

Classifique as variáveis `chuva_mm`, `periodo` e `especie_coleta` quanto ao tipo (qualitativa/quantitativa e subtipo) e à escala de medição, justificando cada classificação em uma frase.

> **Resposta-modelo**
>
> **chuva_mm:** quantitativa contínua, escala de razão — é medida em mm e o zero indica ausência de chuva.
>
> **periodo:** qualitativa nominal — categorias (enchente, cheia, vazante, seca) sem ordem numérica própria. *Aceitar “ordinal” se o aluno justificar a sequência cíclica do ano, sem pontuar a incoerência da justificativa.*
>
> **especie_coleta:** qualitativa nominal — nomes de espécies, sem ordem.

| Rubrica | Pontos |
|---|---|
| Classifica corretamente as 3 variáveis (0,25 cada) | 0,75 |
| Justifica com o critério certo (medir/contar, ordem, zero absoluto) | 0,50 |
| Linguagem técnica correta | 0,25 |
| **Total** | **1,50** |

### Questão 10

Observe o gráfico de linhas da cota diária de 2025 e escreva um parágrafo de 3 a 5 linhas, em linguagem acessível a um gestor, descrevendo o padrão e apontando um ponto que merece investigação.

> **Resposta-modelo**
>
> Elementos esperados: ciclo anual (sobe, pico ≈ 28 m em junho, desce, vale ≈ 16 m em outubro-novembro); comparação entre períodos (cheia alta e estável; enchente e vazante com mais variação); duas leituras fora do padrão (**8,90 m em 18/03** e **35,10 m em 09/08**) a investigar; ressalva de que é uma base didática de um ano.

| Rubrica | Pontos |
|---|---|
| Descreve corretamente o padrão do ciclo | 0,50 |
| Cita valores aproximados do gráfico | 0,25 |
| Identifica as leituras estranhas e propõe verificá-las | 0,50 |
| Linguagem acessível, sem jargão e com coesão | 0,25 |
| **Total** | **1,50** |

## Parte C — Prática

No Google Colab, carregue `rio_negro_cotas.csv` e: (a) mostre o número de linhas e colunas e a quantidade de valores ausentes por coluna; (b) crie a tabela com dias, mínimo, máximo e média da cota por período, na ordem do ano; (c) conte os dias de cada nível de alerta; (d) gere um boxplot da cota por período e salve a imagem. Escreva duas frases interpretando a tabela.

Solução de referência: [`solucao_parte_c.py`](solucao_parte_c.py)

**Saída esperada**

```text
(365, 7)
data                0
cota_metros         0
chuva_mm            0
temperatura_c       0
alerta              0
periodo             0
especie_coleta    312
dtype: int64
          dias  minimo  maximo  media
periodo                              
enchente   151    8.90   26.70  21.21
cheia       92   26.38   28.60  27.81
vazante     61   17.40   35.10  21.87
seca        61   15.92   17.27  16.26
alerta
baixo    141
alto     125
médio     99
Name: count, dtype: int64
```

> **Interpretação esperada**
>
> Esperado: cheia e seca são estáveis (faixas estreitas: 26,38–28,60 m e 15,92–17,27 m); enchente e vazante têm mínimo 8,90 m e máximo 35,10 m, valores atípicos que precisam de investigação.

| Critério | Pontos |
|---|---|
| Leitura correta e (a) shape + ausentes | 0,50 |
| (b) tabela por período, na ordem correta | 0,75 |
| (c) contagem dos alertas | 0,25 |
| (d) boxplot com título e arquivo salvo | 0,50 |
| Interpretação em 2 frases (cita enchente/vazante com mínimo/máximo atípicos) | 0,50 |
| Código organizado e executa sem erros | 0,50 |
| **Total** | **3,00** |
