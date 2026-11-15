import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 9 — Correlação não é causalidade (Oficina 2)
d = df[df["temperatura_c"] < 35].copy()

# 1) Uma correlação FORTE nos dados do projeto
print("cota x temperatura: r = %.3f" % d["cota_metros"].corr(d["temperatura_c"]))
print("  -> a temperatura 'causa' a cota? Improvável: a ESTAÇÃO do ano move as duas.")

# 2) Uma correlação FRACA nos dados do projeto
print("\ncota x chuva (mesmo dia): r = %.3f" % d["cota_metros"].corr(d["chuva_mm"]))
d["chuva_30d"] = d["chuva_mm"].rolling(30).sum()
print("cota x chuva acumulada dos 30 dias anteriores: r = %.3f" % d["cota_metros"].corr(d["chuva_30d"]))
print("  -> r perto de zero mede só a relação LINEAR; não prova que 'não há relação'.")

# 3) Séries que apenas "andam juntas" com o tempo
d["dia_do_ano"] = d["data"].dt.dayofyear
subida = d[d["dia_do_ano"] <= 180]
print("\ncota x dia do ano (da enchente até o pico): r = %.3f" %
      subida["cota_metros"].corr(subida["dia_do_ano"]))

# 4) Variável de confusão — experimento SIMULADO (dados fictícios)
rng = np.random.default_rng(9)
calor = rng.normal(30, 4, 200)                           # causa comum (oculta)
sorvete = 20 + 3 * calor + rng.normal(0, 8, 200)         # vendas de sorvete
afogamentos = 0.5 * calor + rng.normal(0, 3, 200)        # acidentes na água
print("\nsorvete x afogamentos: r = %.3f" % np.corrcoef(sorvete, afogamentos)[0, 1])

def residuo(y, x):                                       # tira o efeito de x sobre y
    a, b = np.polyfit(x, y, 1)
    return y - (a * x + b)

r_ctrl = np.corrcoef(residuo(sorvete, calor), residuo(afogamentos, calor))[0, 1]
print("controlando o calor:     r = %.3f" % r_ctrl)
