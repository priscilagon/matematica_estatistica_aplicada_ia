import pandas as pd
import numpy as np
df = pd.read_csv("rio_negro_cotas.csv", parse_dates=["data"])
d = [15, 17, 17, 20, 21, 25]
x = np.array(d)
print("média", x.mean(), "mediana", np.median(x), "amplitude", x.max() - x.min())
print("var pop %.4f | var am %.4f" % (np.var(x, ddof=0), np.var(x, ddof=1)))
print("dp pop %.4f | dp am %.4f" % (np.std(x, ddof=0), np.std(x, ddof=1)))
q1, q3 = df["cota_metros"].quantile([.25, .75]); print("Q1 %.2f Q3 %.2f" % (q1, q3))
t = df["temperatura_c"]
q1, q3 = t.quantile([.25, .75]); iqr = q3 - q1
li, ls = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("limites temperatura: %.2f ; %.2f" % (li, ls)); print(df[(t < li) | (t > ls)][["data", "temperatura_c"]])
v = df[df["temperatura_c"] < 35]
print("r cota x temp: %.3f" % v["cota_metros"].corr(v["temperatura_c"]))
for p in ["cheia", "seca"]:
    c = df[df["periodo"] == p]["cota_metros"]
    print(p, "média %.2f | dp %.3f" % (c.mean(), c.std(ddof=1)))
