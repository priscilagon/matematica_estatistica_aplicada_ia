"""Gera a base didática 'rio_negro_cotas.csv' (SIMULADA, inspirada no regime do Rio Negro em Manaus)."""
import numpy as np, pandas as pd

rng = np.random.default_rng(2026)
datas = pd.date_range("2025-01-01", "2025-12-31", freq="D")
doy = datas.dayofyear.values

PICO, VALE = 28.4, 15.9          # metros (didático)
def hidrograma(d):
    # enchente longa (~245 dias) e vazante mais curta (~120 dias): pico ~dia 180, vale ~dia 300
    if d <= 180:
        f = (d + 65) / 245
        return VALE + (PICO - VALE) * (1 - np.cos(np.pi * f)) / 2
    if d <= 300:
        f = (d - 180) / 120
        return PICO - (PICO - VALE) * (1 - np.cos(np.pi * f)) / 2
    f = (d - 300) / 245
    return VALE + (PICO - VALE) * (1 - np.cos(np.pi * f)) / 2

base = np.array([hidrograma(d) for d in doy])
ruido = np.zeros(len(doy))
for i in range(1, len(doy)):
    ruido[i] = 0.85 * ruido[i-1] + rng.normal(0, 0.06)
cota = base + ruido

# chuva diária (mm): muitos dias com zero na estiagem
p_chuva = {1:.75,2:.78,3:.80,4:.78,5:.70,6:.50,7:.40,8:.30,9:.30,10:.40,11:.55,12:.70}
chuva = np.zeros(len(datas))
for i, d in enumerate(datas):
    if rng.random() < p_chuva[d.month]:
        chuva[i] = rng.gamma(1.3, 9.0)
chuva = np.round(chuva, 1)

# temperatura da água (°C): mais quente na seca (águas baixas), mais amena na cheia
temp = 29.8 - 2.4 * (cota - VALE) / (PICO - VALE) + rng.normal(0, 0.30, len(datas))

df = pd.DataFrame({"data": datas.strftime("%Y-%m-%d"),
                   "cota_metros": np.round(cota, 2),
                   "chuva_mm": chuva,
                   "temperatura_c": np.round(temp, 1)})

# leituras atípicas (erros de sensor/digitação) para a aula de outliers
df.loc[df["data"] == "2025-03-18", "cota_metros"] = 8.90
df.loc[df["data"] == "2025-08-09", "cota_metros"] = 35.10
df.loc[df["data"] == "2025-10-22", "temperatura_c"] = 38.5

# alerta didático (ordinal) pela cota
def alerta(c):
    return "baixo" if c < 20 else ("médio" if c < 25 else "alto")
df["alerta"] = df["cota_metros"].apply(alerta)

# período hidrológico didático (nominal)
def periodo(m):
    if m in (12,1,2,3,4): return "enchente"
    if m in (5,6,7):      return "cheia"
    if m in (8,9):        return "vazante"
    return "seca"
df["periodo"] = pd.to_datetime(df["data"]).dt.month.apply(periodo)

# espécie registrada em coleta semanal (nominal; ausente nos demais dias)
esp = ["tambaqui","pirarucu","tucunaré","matrinxã","pacu"]
pesos = [.30,.15,.25,.18,.12]
df["especie_coleta"] = ""
idx = np.arange(0, len(df), 7)
df.loc[idx, "especie_coleta"] = rng.choice(esp, size=len(idx), p=pesos)

df.to_csv("rio_negro_cotas.csv", index=False, encoding="utf-8")
print(df.shape); print(df.head(3)); print(df.describe().round(2))
