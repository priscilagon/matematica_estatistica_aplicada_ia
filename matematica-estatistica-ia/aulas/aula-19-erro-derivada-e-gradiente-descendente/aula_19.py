import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 19 — Erro (loss), derivada e gradiente descendente
# Objetivo: aprender a reta  temperatura = w * cota + b   minimizando o erro
d = df[df["temperatura_c"] < 35]
x = ((d["cota_metros"] - d["cota_metros"].mean()) / d["cota_metros"].std(ddof=0)).to_numpy()
y = d["temperatura_c"].to_numpy()

w, b = 0.0, float(y.mean())            # ponto de partida
taxa = 0.1                             # taxa de aprendizado
historico = []
for passo in range(61):
    previsao = w * x + b
    erro = previsao - y
    loss = np.mean(erro ** 2)                 # erro quadrático médio (EQM)
    dw = 2 * np.mean(erro * x)                # derivada da loss em relação a w
    db = 2 * np.mean(erro)                    # derivada da loss em relação a b
    w, b = w - taxa * dw, b - taxa * db       # passo na direção que REDUZ o erro
    historico.append(loss)
    if passo in (0, 1, 2, 5, 10, 30, 60):
        print("passo %2d | loss = %.4f | w = %.4f | b = %.4f" % (passo, loss, w, b))

# Conferência com a solução exata (mínimos quadrados)
w_ex, b_ex = np.polyfit(x, y, 1)
print("\nSolução exata:  w = %.4f | b = %.4f" % (w_ex, b_ex))

plt.plot(historico)
plt.xlabel("passo"); plt.ylabel("loss (EQM)"); plt.title("A loss cai a cada passo")
plt.show()
