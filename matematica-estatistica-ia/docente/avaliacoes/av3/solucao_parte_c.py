import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv("rio_negro_cotas.csv", parse_dates=["data"])
A = df["alerta"] == "alto"
E = df["chuva_mm"] > 10
print("P(alto) = %.4f" % A.mean())
print("P(chuva>10) = %.4f" % E.mean())
print("P(alto | chuva>10) = %.4f" % ((A & E).mean() / E.mean()))
print("P(chuva>10 | alto) = %.4f" % ((A & E).mean() / A.mean()))
c = df[df["periodo"] == "cheia"]["cota_metros"]
n, m, s = len(c), c.mean(), c.std(ddof=1)
ic = stats.t.interval(0.95, df=n - 1, loc=m, scale=s / np.sqrt(n))
print("cheia: n=%d média=%.3f dp=%.3f IC95%%=[%.3f ; %.3f]" % (n, m, s, ic[0], ic[1]))
print("P(X>=15 dias altos em 30) = %.4f" % stats.binom.sf(14, 30, A.mean()))
