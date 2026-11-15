import pandas as pd
import numpy as np
df = pd.read_csv("rio_negro_cotas.csv", parse_dates=["data"])
C = np.array([[2, 0], [1, 3]]); D = np.array([[1, 4], [2, 5]])
print(C @ D)
x = np.array([1., 2., 3.]); y = np.array([2., 4., 6.])
w, alfa = 1.0, 0.1
for i in range(3):
    erro = w * x - y
    loss = np.mean(erro ** 2); grad = 2 * np.mean(erro * x)
    print("passo %d: w=%.4f loss=%.4f grad=%.4f" % (i, w, loss, grad))
    w = w - alfa * grad
print("w após 3 passos: %.4f" % w)
d = df[(df["temperatura_c"] < 35) & (df["cota_metros"].between(10, 33))]
print(d.groupby("periodo")["cota_metros"].agg(["count", "mean", "median", "std"]).round(2))
print("r = %.3f" % d["cota_metros"].corr(d["temperatura_c"]))
