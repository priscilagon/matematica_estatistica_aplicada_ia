# Aula 7 — Dispersão entre duas variáveis e covariância

| | |
|---|---|
| **Fase do projeto** | Fase 2 — Estatística descritiva e relações entre variáveis |
| **Habilidade** | Interpretar a relação entre variáveis por meio de gráficos de dispersão, covariância e correlação. |
| **Objetos de conhecimento** | Gráfico de dispersão. Covariância. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** variância e desvio-padrão; pergunta-problema: “quando a cota sobe, o que acontece com a temperatura?”. |
| 55 min | **Aula expositiva:** variáveis em par; gráfico de dispersão; covariância (sinal e limitações). |
| 80 min | **Prática em Python:** gráficos de dispersão e matriz de covariância com os dados do projeto. |
| 30 min | **Sistematização:** o que a covariância informa e o que não informa. |

## 2. Conteúdo

### 1. Gráfico de dispersão

Cada ponto representa **uma observação** com duas medidas: (x, y). O formato da nuvem mostra se as variáveis se relacionam: nuvem **ascendente** (quando x aumenta, y tende a aumentar), **descendente** (y tende a diminuir) ou **sem forma** (sem relação linear aparente).

![Dispersão cota × temperatura: nuvem descendente, com duas leituras de cota fora do padrão.](../../../figuras/f05_dispersao.png)

*Dispersão cota × temperatura: nuvem descendente, com duas leituras de cota fora do padrão.*

### 2. Covariância

A covariância mede se duas variáveis **variam juntas** e em que sentido:

```text
cov(X, Y) = Σ (xᵢ − média_x)(yᵢ − média_y) ÷ (n − 1)
```

- **cov > 0:** quando uma está acima da média, a outra tende a estar acima.
- **cov < 0:** quando uma está acima da média, a outra tende a estar abaixo.
- **cov ≈ 0:** sem relação linear clara.

> **📝 Exemplo resolvido: X = 1, 2, 3, 4, 5 e Y = 2, 4, 5, 4, 5**
>
> Médias: x̄ = 3; ȳ = 4. Desvios de X: −2, −1, 0, 1, 2. Desvios de Y: −2, 0, 1, 0, 1.
>
> Produtos: 4, 0, 0, 0, 2 → soma = 6.
>
> **Covariância amostral** = 6 ÷ 4 = **1,5**; **populacional** = 6 ÷ 5 = **1,2**. Positiva: as duas variáveis crescem juntas.

> **⚠️ Atenção: limitação: a covariância depende da unidade**
>
> A covariância entre cota e temperatura vale **-3,702** com a cota em metros, mas **-370,2** com a cota em centímetros — a mesma relação, 100 vezes maior. Por isso o valor da covariância **não diz se a relação é forte**; só dá o sinal. Para a intensidade, usamos a correlação (Aula 8).

Com os dados do projeto: cov(cota, temperatura) = **-3,702** (sinal negativo: cota alta e temperatura baixa andam juntas) e cov(cota, chuva) = **-3,931**.

## 3. Prática em Python

Gere a matriz de covariância e verifique que mudar a unidade muda o valor.

- Script: [`aula_07.py`](aula_07.py)
- Notebook (Colab): [`aula_07.ipynb`](aula_07.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-07-dispersao-entre-duas-variaveis-e-covariancia/aula_07.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- A diagonal da matriz é a **variância** de cada variável (ex.: 20,528 para a cota).
- Fora da diagonal estão as covariâncias, simétricas.
- Trocar a cota de metros para cm multiplica a covariância por 100.

## 4. Atividades de fixação

1. Calcule a covariância amostral entre X = 1, 2, 3, 4, 5 e Y = 2, 4, 5, 4, 5.
2. O que significa uma covariância negativa entre cota e temperatura da água? Isso prova que a cota diminui a temperatura?
3. Por que a covariância entre cota (em cm) e temperatura é 100 vezes maior que com a cota em metros? Qual medida resolve esse problema?
4. Qual é o valor da diagonal da matriz de covariância e o que ele representa?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Ler um gráfico de dispersão (sentido e forma).
- [ ] Calcular a covariância à mão em 5 pares.
- [ ] Interpretar o sinal da covariância.
- [ ] Explicar por que a covariância depende da unidade.
- [ ] Gerar `df.cov()` e `plt.scatter` no Python.

---
[← Voltar ao índice](../../README.md)
