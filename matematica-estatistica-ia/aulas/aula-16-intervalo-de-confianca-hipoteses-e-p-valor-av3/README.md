# Aula 16 — Intervalo de confiança, hipóteses e p-valor — AV3

| | |
|---|---|
| **Fase do projeto** | Fase 3 — Probabilidade e inferência |
| **Habilidade** | Interpretar intervalos de confiança e testes de hipótese de forma básica, evitando conclusões incorretas sobre os dados. |
| **Objetos de conhecimento** | Intervalo de confiança. Hipótese nula e alternativa. p-valor. Nível de significância. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | **AV3** — avaliação desta aula, cobrindo as Aulas 10 a 16 (ver Parte III). |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** erro-padrão e viés. |
| 50 min | **Aula expositiva:** intervalo de confiança; hipótese nula, p-valor e nível de significância. |
| 45 min | **Prática em Python:** IC para a média e teste t para comparar cheia e seca. |
| 70 min | **Aplicação da AV3** (objetivas, discursivas e prática em Python). |

## 2. Conteúdo

### 1. Intervalo de confiança (IC) para a média

Uma média amostral é uma estimativa **pontual**. O IC acrescenta a **margem de erro**: um intervalo que, **em 95% das amostras possíveis**, contém a média verdadeira.

```text
IC95% = x̄ ± t · (s ÷ √n)        (t da distribuição t de Student com n − 1 g.l.)
```

> **📝 Exemplo resolvido: n = 25; x̄ = 50; s = 10**
>
> EP = 10 ÷ √25 = 2; t(24 g.l.) ≈ 2,0639; margem de erro = 2,0639 × 2 ≈ **4,128**.
>
> **IC95% = [45,87 ; 54,13]**. (Com z = 1,96 a margem seria 3,92: IC ≈ [46,08 ; 53,92] — mais estreito, pois ignora a incerteza de estimar s com n pequeno.)

**No projeto:** temperatura da água, média 28,560 °C → **IC95% = [28,469 ; 28,651]**.

> **⚠️ Atenção: interpretação correta**
>
> **Certo:** “o método usado produz intervalos que contêm a média verdadeira em 95% das vezes”. **Errado:** “há 95% de probabilidade de a média estar neste intervalo” (a média é fixa; o intervalo é que varia de amostra em amostra). IC mais **estreito** = estimativa mais precisa (n maior ou menos variação).

### 2. Teste de hipótese e p-valor

1. Formular **H₀** (hipótese nula: “não há diferença/efeito”) e **H₁** (alternativa).
2. Escolher o nível de significância **α** (usualmente 0,05).
3. Calcular a estatística de teste e o **p-valor**.
4. Decidir: se **p < α**, rejeitamos H₀; caso contrário, **não rejeitamos**.

> **📌 Conceito-chave: o que é o p-valor**
>
> É a probabilidade de observar um resultado **tão extremo quanto o obtido (ou mais), supondo que H₀ seja verdadeira**. P-valor pequeno = dados “surpreendentes” sob H₀.

> **📝 Exemplo resolvido: temperatura na cheia × seca (teste t de Welch)**
>
> H₀: as temperaturas médias são iguais. Cheia = 27,489 °C; seca = 29,678 °C. **t = -39,178**; **p ≈ 1,2 × 10⁻⁷⁰** → p < 0,05: **rejeita-se H₀**. Há evidência estatística de que a temperatura média é diferente.
>
> Contraste: dois sorteios do **mesmo** conjunto dão **p = 0,901** → não se rejeita H₀ (sem diferença, como esperado).

> **⚠️ Atenção: erros de interpretação mais comuns**
>
> (1) p-valor **não** é a probabilidade de H₀ ser verdadeira. (2) **Não rejeitar** H₀ não prova que H₀ é verdadeira. (3) “Significativo” **não** significa “importante”: com n enorme, diferenças minúsculas dão p pequeno. (4) Testar muitas hipóteses até “achar” p < 0,05 (p-hacking) produz falsas descobertas.

## 3. Prática em Python

Calcule o IC da temperatura e faça o teste t de Welch entre cheia e seca.

- Script: [`aula_16.py`](aula_16.py)
- Notebook (Colab): [`aula_16.ipynb`](aula_16.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-16-intervalo-de-confianca-hipoteses-e-p-valor-av3/aula_16.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- `stats.t.interval` devolve os limites do IC.
- `ttest_ind(..., equal_var=False)` é o teste t de Welch (não supõe variâncias iguais).
- Remova o valor atípico (38,5 °C) antes: `temperatura_c < 35`.
- No segundo teste, p = 0,901: **não** há diferença entre dois sorteios do mesmo grupo.

## 4. Atividades de fixação

1. Uma amostra de n = 25 tem x̄ = 50 e s = 10. Construa o IC de 95% para a média.
2. O IC95% da temperatura média é [28,469; 28,651]. Interprete corretamente e diga se a média 29 °C é plausível.
3. Explique o que é p-valor sem usar fórmulas e o que significa p = 0,03 com α = 0,05.
4. Um teste resultou em p = 0,40. A conclusão “comprovamos que não há diferença” está correta? Justifique.
5. Por que o p-valor do teste entre cheia e seca é praticamente zero, enquanto o dos dois sorteios é 0,90?

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Fórmula e interpretação do IC.
- [ ] Etapas de um teste de hipótese (H₀, H₁, α, p).
- [ ] Interpretação correta do p-valor e erros comuns.
- [ ] Efeito de n na largura do IC.
- [ ] `scipy.stats`: `t.interval` e `ttest_ind`.
- [ ] Revisar as Aulas 10 a 15 para a **AV3**.

---
[← Voltar ao índice](../../README.md)
