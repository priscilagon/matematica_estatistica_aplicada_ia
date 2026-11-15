# Matemática e Estatística Aplicada à IA

**Curso Técnico de Nível Médio em Inteligência Artificial · CETAM · 60 h (20 aulas de 3 h)**
Professora: Priscila Gonçalves · Manaus, Amazonas

Projeto integrador: **Painel de Indicadores Hidrológicos e Ambientais do Rio Negro**

> ⚠️ **Dados simulados.** A base `dados/rio_negro_cotas.csv` foi criada para o ensino: reproduz o ciclo sazonal do Rio Negro, mas **não são medições oficiais**. Não use para decisões reais.

## O que há aqui

- **20 aulas** com procedimentos didáticos, conteúdo, prática em Python (script + notebook para o Colab) e atividades de fixação.
- **4 avaliações** (AV1 a AV4), cada uma com 8 objetivas, 2 discursivas e prática em Python.
- **Área do docente** com gabarito oficial, rubricas e soluções.
- **Recursos**: formulário, glossário, referências ABNT, caderno de bordo e a apostila em .docx.

## Como começar (aluno)

1. Abra o notebook da aula no Colab (link dentro de cada pasta) — o CSV é baixado automaticamente.
2. Ou clone o repositório e rode localmente:

```bash
git clone https://github.com/priscilagon/matematica-estatistica-ia.git
cd matematica-estatistica-ia
pip install -r requirements.txt
python aulas/aula-01-*/aula_01.py
```

## Estrutura do repositório

```text
matematica-estatistica-ia/
├── README.md
├── requirements.txt
├── LICENSE
├── dados/                    # CSV do projeto + gerador + dicionário de dados
├── figuras/                  # figuras usadas nas aulas
├── aulas/
│   ├── aula-01-.../          # README.md · aula_01.py · aula_01.ipynb · saida_esperada.txt
│   ├── ...
│   └── aula-20-.../
├── avaliacoes/
│   ├── av1-.../              # enunciado (README.md) + modelo da Parte C
│   ├── av2-... · av3-... · av4-...
├── recursos/                 # formulário · glossário · referências · caderno de bordo
├── docs/                     # apostila em .docx
└── docente/                  # ⚠️ respostas (manter privado)
    ├── Gabarito_Oficial_*.docx
    ├── aulas/respostas_atividades_de_fixacao.md
    └── avaliacoes/av1..av4/  # gabarito.md · solucao_parte_c.py · saida_esperada.txt
```

## Índice das aulas

### Fase 1 — Exploração e leitura de dados

| Aula | Tema | Avaliação |
|---|---|---|
| 1 | [Abertura, dados, variáveis e escalas de medição](aulas/aula-01-abertura-dados-variaveis-e-escalas-de-medicao/README.md) | Formativa |
| 2 | [Tabelas de frequência e gráficos (barras, linhas, histogramas, boxplot)](aulas/aula-02-tabelas-de-frequencia-e-graficos-barras-linhas-his/README.md) | Formativa |
| 3 | [Conclusão da Oficina 1 e mini-relatório parcial (AV1)](aulas/aula-03-conclusao-da-oficina-1-e-mini-relatorio-parcial-av/README.md) | **AV1** |

### Fase 2 — Estatística descritiva e relações entre variáveis

| Aula | Tema | Avaliação |
|---|---|---|
| 4 | [Medidas de tendência central: média, mediana e moda](aulas/aula-04-medidas-de-tendencia-central-media-mediana-e-moda/README.md) | Formativa |
| 5 | [Medidas de variação: amplitude, variância e desvio-padrão](aulas/aula-05-medidas-de-variacao-amplitude-variancia-e-desvio-p/README.md) | Formativa |
| 6 | [Quartis, outliers, normalização e padronização](aulas/aula-06-quartis-outliers-normalizacao-e-padronizacao/README.md) | Formativa |
| 7 | [Dispersão entre duas variáveis e covariância](aulas/aula-07-dispersao-entre-duas-variaveis-e-covariancia/README.md) | Formativa |
| 8 | [Correlação de Pearson](aulas/aula-08-correlacao-de-pearson/README.md) | Formativa |
| 9 | [Correlação não é causalidade — Oficina 2 e AV2](aulas/aula-09-correlacao-nao-e-causalidade-oficina-2-e-av2/README.md) | **AV2** |

### Fase 3 — Probabilidade e inferência

| Aula | Tema | Avaliação |
|---|---|---|
| 10 | [Probabilidade: eventos, regra da soma e regra do produto](aulas/aula-10-probabilidade-eventos-regra-da-soma-e-regra-do-pro/README.md) | Formativa |
| 11 | [Probabilidade condicional](aulas/aula-11-probabilidade-condicional/README.md) | Formativa |
| 12 | [Teorema de Bayes (intuição) — Oficina 3](aulas/aula-12-teorema-de-bayes-intuicao-oficina-3/README.md) | Formativa |
| 13 | [Distribuição Normal](aulas/aula-13-distribuicao-normal/README.md) | Formativa |
| 14 | [Distribuições Binomial e de Poisson](aulas/aula-14-distribuicoes-binomial-e-de-poisson/README.md) | Formativa |
| 15 | [População, amostra, viés de amostragem e erro-padrão](aulas/aula-15-populacao-amostra-vies-de-amostragem-e-erro-padrao/README.md) | Formativa |
| 16 | [Intervalo de confiança, hipóteses e p-valor — AV3](aulas/aula-16-intervalo-de-confianca-hipoteses-e-p-valor-av3/README.md) | **AV3** |

### Fase 4 — Fundamentos matemáticos da IA e síntese

| Aula | Tema | Avaliação |
|---|---|---|
| 17 | [Vetores e matrizes: dados como números organizados](aulas/aula-17-vetores-e-matrizes-dados-como-numeros-organizados/README.md) | Formativa |
| 18 | [Produto escalar, funções lineares e não lineares](aulas/aula-18-produto-escalar-funcoes-lineares-e-nao-lineares/README.md) | Formativa |
| 19 | [Erro, derivada e gradiente descendente](aulas/aula-19-erro-derivada-e-gradiente-descendente/README.md) | Formativa |
| 20 | [Síntese do projeto: painel de indicadores e mini-relatório final — AV4](aulas/aula-20-sintese-do-projeto-painel-de-indicadores-e-mini-re/README.md) | **AV4** |

## Avaliações

| Avaliação | Aula | Conteúdo | Enunciado |
|---|---|---|---|
| AV1 | 3 | Aulas 1 a 3 | [avaliacoes/av1-aulas-1-a-3](avaliacoes/av1-aulas-1-a-3/README.md) |
| AV2 | 9 | Aulas 4 a 9 | [avaliacoes/av2-aulas-4-a-9](avaliacoes/av2-aulas-4-a-9/README.md) |
| AV3 | 16 | Aulas 10 a 16 | [avaliacoes/av3-aulas-10-a-16](avaliacoes/av3-aulas-10-a-16/README.md) |
| AV4 | 20 | Aulas 17 a 20 e projeto integrador | [avaliacoes/av4-aulas-17-a-20-e-projeto-integrador](avaliacoes/av4-aulas-17-a-20-e-projeto-integrador/README.md) |

Cada AV vale 10,0 pontos. Composição da nota final conforme o regulamento da instituição.

## Publicando

```bash
cd matematica-estatistica-ia
git init -b main
git add .
git commit -m "Material de Matemática e Estatística Aplicada à IA"
git remote add origin https://github.com/priscilagon/matematica-estatistica-ia.git
git push -u origin main
```

**Sobre o gabarito:** a pasta `docente/` contém respostas. Opções: (a) criar o repositório como **privado**; (b) publicar o repositório público **sem** a pasta (`git rm -r --cached docente` e manter `docente/` no `.gitignore`); (c) usar dois repositórios (um do aluno e um do professor). Antes de tornar público, confira também `avaliacoes/`.

## Tecnologias

Python 3.10+ · pandas · NumPy · Matplotlib · SciPy · Google Colab

## Licença

Texto e materiais didáticos: **CC BY-NC-SA 4.0**. Código: **MIT**. Veja [LICENSE](LICENSE).
