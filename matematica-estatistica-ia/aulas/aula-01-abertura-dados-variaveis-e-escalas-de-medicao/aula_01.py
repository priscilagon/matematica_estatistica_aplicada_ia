import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 1 — Lendo e classificando os dados do projeto
print("Linhas x colunas:", df.shape)
print(df.head())
print()
print(df.dtypes)          # tipo que o Python reconheceu (pode aparecer 'object' ou 'str')
print()

# valores distintos das variáveis categóricas
print("alerta .....:", sorted(df["alerta"].unique()))
print("periodo ....:", sorted(df["periodo"].unique()))
print("espécies ...:", sorted(df["especie_coleta"].dropna().unique()))

# dados ausentes por coluna (especie_coleta só existe em dias de coleta)
print()
print(df.isna().sum())
