# Aula 19 — Erro, derivada e gradiente descendente

| | |
|---|---|
| **Fase do projeto** | Fase 4 — Fundamentos matemáticos da IA e síntese |
| **Habilidade** | Aplicar conceitos de álgebra linear e cálculo em problemas simples de IA, interpretando o significado dos resultados. |
| **Objetos de conhecimento** | Função de perda (loss). Derivada como taxa de variação. Gradiente descendente. Taxa de aprendizado. |
| **Carga horária** | 3 horas (180 min) |
| **Avaliação** | Formativa (atividades de fixação + caderno de bordo) |

## 1. Procedimentos didáticos

| Tempo | Momento da aula |
|---|---|
| 15 min | **Retomada:** modelo linear e EQM. |
| 60 min | **Aula expositiva:** derivada como inclinação; gradiente descendente; taxa de aprendizado. |
| 75 min | **Prática em Python:** implementar o gradiente descendente do zero e testar taxas de aprendizado. |
| 30 min | **Sistematização:** o laço de treinamento (prever → medir erro → corrigir). |

## 2. Conteúdo

### 1. Treinar = reduzir o erro

A **função de perda (loss)** mede o quanto o modelo erra. Treinar é encontrar parâmetros que **minimizam** a loss. Usamos o EQM: **L = média de (ŷ − y)²**.

### 2. Derivada: a inclinação do erro

A **derivada** dL/dw diz **para onde** e **quanto** a loss varia quando mexemos em w: se for positiva, a loss cresce com w (devemos **diminuir** w); se for negativa, devemos **aumentar** w. Com vários parâmetros, o vetor das derivadas é o **gradiente**.

### 3. Gradiente descendente

```text
w_novo = w − α · dL/dw          (α = taxa de aprendizado)
```

> **📝 Exemplo resolvido: modelo ŷ = w·x com x = [1, 2, 3] e y = [2, 4, 6]; w inicial = 1; α = 0,1**
>
> **Erros** (ŷ − y) = −1, −2, −3. **Loss** L(1) = (1 + 4 + 9) ÷ 3 = **4,6667**.
>
> **Gradiente** dL/dw = 2·média(erro·x) = 2·(−1 − 4 − 9) ÷ 3 = **-9,3333** (negativo → aumentar w).
>
> **Novo w** = 1 − 0,1·(-9,3333) = **1,9333**. O valor ótimo é w = 2 (L = 0): em um passo, chegamos perto.

### 4. A taxa de aprendizado

![Efeito da taxa de aprendizado na queda da loss.](../../../figuras/f09_loss.png)

*Efeito da taxa de aprendizado na queda da loss.*

| Taxa α | Comportamento | Loss final (60 passos) |
|---|---|---|
| 0,01 | Muito lenta: após 60 passos ainda não chegou | 0,1733 |
| 0,1 | Boa: converge | 0,1144 |
| 1,0 | Passos grandes demais: oscila, não converge | 0,7801 |
| 1,1 | Diverge: a loss explode | ≈ 2 × 10⁹ |

No projeto, aprendemos a reta **temperatura = w·cota_padronizada + b**. O gradiente descendente chega a **w = -0,8159** e **b = 28,5599**, o mesmo da solução exata (mínimos quadrados). Como a cota foi padronizada, w significa: cada 1 desvio-padrão a mais de cota reduz a temperatura prevista em cerca de 0,82 °C.

> **💡 Dica: por que padronizar antes?**
>
> Features em escalas muito diferentes tornam o “vale” da loss alongado, e o gradiente descendente oscila ou demora. Padronizar (Aula 6) acelera e estabiliza o treino.

## 3. Prática em Python

Implemente o laço de treinamento do zero e compare com a solução exata.

- Script: [`aula_19.py`](aula_19.py)
- Notebook (Colab): [`aula_19.ipynb`](aula_19.ipynb) — [abrir no Colab](https://colab.research.google.com/github/priscilagon/matematica-estatistica-ia/blob/main/aulas/aula-19-erro-derivada-e-gradiente-descendente/aula_19.ipynb)
- Saída esperada: [`saida_esperada.txt`](saida_esperada.txt)

**O que observar**

- A loss cai de 0,7801 para 0,1144 e para de mudar: **convergência**.
- `w` caminha de 0 até −0,8159 e `b` já começa em 28,56 (média da temperatura).
- Mude `taxa` para 0.01, 1.0 e 1.1 e compare.

## 4. Atividades de fixação

1. Para ŷ = w·x com x = [1, 2, 3], y = [2, 4, 6] e w = 1: calcule a loss, o gradiente e o novo w com α = 0,1.
2. Para w = 2, quanto vale a loss? O que o gradiente vale nesse ponto?
3. Explique o que acontece se a taxa de aprendizado for muito pequena e se for muito grande.
4. O gradiente de uma loss em w é +5. Devemos aumentar ou diminuir w? Por quê?
5. No projeto, w = −0,8159 para a cota padronizada. Interprete.

> Respostas: pasta [`docente/`](../../docente/) (uso do professor).

## 5. Para estudar

- [ ] Definir loss/EQM e derivada como inclinação.
- [ ] Aplicar um passo do gradiente descendente à mão.
- [ ] Explicar o papel da taxa de aprendizado.
- [ ] Descrever o laço de treinamento (prever, medir erro, corrigir).
- [ ] Justificar a padronização antes do treino.

---
[← Voltar ao índice](../../README.md)
