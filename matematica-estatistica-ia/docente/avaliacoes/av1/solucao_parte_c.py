import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("rio_negro_cotas.csv", parse_dates=["data"])
print(df.shape)
print(df.isna().sum())
ordem = ["enchente", "cheia", "vazante", "seca"]
resumo = df.groupby("periodo")["cota_metros"].agg(dias="count", minimo="min", maximo="max", media="mean").reindex(ordem).round(2)
print(resumo)
print(df["alerta"].value_counts())
fig, ax = plt.subplots()
df.boxplot(column="cota_metros", by="periodo", ax=ax)
ax.set_title("Cota por período"); plt.suptitle("")
fig.savefig("av1_boxplot.png", dpi=150)
