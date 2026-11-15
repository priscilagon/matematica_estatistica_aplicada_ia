import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 18 — Produto escalar, features, funções lineares e não lineares
a = np.array([2, 1, 3]); b = np.array([4, 0, 5])
print("a . b =", np.dot(a, b), "(2*4 + 1*0 + 3*5)")

# Um "modelo" é um produto escalar: previsão = pesos . features + viés
x = np.array([24.0, 10.0, 28.0])           # [cota, chuva, temperatura] de um dia
w = np.array([0.5, 0.1, -0.2]); b0 = 3.0
print("previsão = w.x + b =", round(float(np.dot(w, x) + b0), 3))

# Relação linear x não linear: cota ao longo do ano
d = df[df["cota_metros"].between(10, 33)].copy()         # sem leituras atípicas
dia = d["data"].dt.dayofyear.to_numpy()
y = d["cota_metros"].to_numpy()

reta = np.polyfit(dia, y, 1)               # função linear
cubica = np.polyfit(dia, y, 3)             # função não linear (polinômio grau 3)
mse = lambda coef: np.mean((y - np.polyval(coef, dia)) ** 2)
print("\nEQM da reta   : %.3f" % mse(reta))
print("EQM do grau 3 : %.3f" % mse(cubica))

plt.scatter(dia, y, s=8, alpha=0.5)
xs = np.linspace(dia.min(), dia.max(), 200)
plt.plot(xs, np.polyval(reta, xs), label="linear")
plt.plot(xs, np.polyval(cubica, xs), label="grau 3")
plt.xlabel("Dia do ano"); plt.ylabel("Cota (m)"); plt.legend(); plt.show()
