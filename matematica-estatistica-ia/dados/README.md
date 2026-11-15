# Dados do projeto integrador

`rio_negro_cotas.csv` — **base simulada com finalidade didática** (365 dias de 2025). Reproduz o ciclo sazonal do Rio Negro em Manaus, com problemas propositais (3 leituras atípicas e dados ausentes). **Não são medições oficiais**, e os limiares de alerta (20 e 25 m) são didáticos.

| Coluna | Descrição | Tipo | Escala |
|---|---|---|---|
| data | Data da leitura (2025-01-01 a 2025-12-31) | Quantitativa (temporal) | Intervalar |
| cota_metros | Nível do rio na régua, em metros | Quantitativa contínua | Razão |
| chuva_mm | Chuva diária, em mm (0 = não choveu) | Quantitativa contínua | Razão |
| temperatura_c | Temperatura da água, em °C | Quantitativa contínua | Intervalar |
| alerta | baixo (cota < 20 m), médio (20 a < 25 m), alto (≥ 25 m) — limiares didáticos, não oficiais | Qualitativa ordinal | Ordinal |
| periodo | enchente (dez.–abr.), cheia (mai.–jul.), vazante (ago.–set.), seca (out.–nov.) | Qualitativa nominal | Nominal |
| especie_coleta | Espécie registrada na coleta semanal (vazia nos demais dias) | Qualitativa nominal | Nominal |

## Leituras atípicas inseridas de propósito

| Data | Variável | Valor |
|---|---|---|
| 2025-03-18 | cota_metros | 8,90 |
| 2025-08-09 | cota_metros | 35,10 |
| 2025-10-22 | temperatura_c | 38,5 |

## Reprodutibilidade

`python3 gerar_dados.py` recria o arquivo (semente fixa 2026). **Todos os gabaritos dependem deste CSV exato**: não o altere.
