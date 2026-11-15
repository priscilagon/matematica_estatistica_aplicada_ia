# Respostas das atividades de fixação (Aulas 1 a 20)

> **Uso exclusivo do professor.**

## Aula 1 — Abertura, dados, variáveis e escalas de medição

**1.** Preencha a tabela de classificação das 7 colunas do CSV (tipo, subtipo e escala): `data`, `cota_metros`, `chuva_mm`, `temperatura_c`, `alerta`, `periodo`, `especie_coleta`.

Tabela de classificação (a data admite discussão: é uma variável temporal em escala intervalar):

| Coluna | Tipo | Subtipo | Escala |
|---|---|---|---|
| data | Quantitativa (temporal) | Contínua* | Intervalar |
| cota_metros | Quantitativa | Contínua | Razão |
| chuva_mm | Quantitativa | Contínua | Razão |
| temperatura_c | Quantitativa | Contínua | Intervalar |
| alerta | Qualitativa | Ordinal | Ordinal |
| periodo | Qualitativa | Nominal | Nominal |
| especie_coleta | Qualitativa | Nominal | Nominal |

*Aceitar também “variável de data/tempo”, desde que o aluno justifique que a distância entre datas é constante mas o zero do calendário é convencional.

**2.** Quantas linhas e colunas tem a base? Quantos valores ausentes há em `especie_coleta` e por que existem?

**365 linhas × 7 colunas.** Há **312** valores ausentes em `especie_coleta`: a espécie só é registrada em coleta semanal (53 dias com registro). Ausente não é erro: é “sem coleta naquele dia”.

**3.** Classifique (tipo e escala): (a) número de embarcações no porto; (b) velocidade da correnteza em m/s; (c) cor predominante da água; (d) turbidez em baixa/média/alta; (e) o ano de cada medição.

**(a)** quantitativa discreta, razão; **(b)** quantitativa contínua, razão; **(c)** qualitativa nominal; **(d)** qualitativa ordinal; **(e)** quantitativa, intervalar (o ano 0 é convenção).

**4.** Por que não faz sentido calcular a “média” da coluna `alerta`? E da coluna `especie_coleta`? Qual medida resumiria cada uma?

Porque são qualitativas: as categorias não são números sobre os quais se possa somar e dividir. Em `alerta` (ordinal) cabe a mediana ou a moda; em `especie_coleta` (nominal) só a **moda** e as frequências. Aceitar justificativa equivalente.

## Aula 2 — Tabelas de frequência e gráficos (barras, linhas, histogramas, boxplot)

**1.** Monte a tabela de frequência (absoluta e relativa) das espécies registradas e indique a moda.

| Espécie | Freq. absoluta | Freq. relativa |
|---|---|---|
| tambaqui | 22 | 41,5% |
| tucunaré | 14 | 26,4% |
| matrinxã | 8 | 15,1% |
| pirarucu | 6 | 11,3% |
| pacu | 3 | 5,7% |
| **Total** | **53** | **100,0%** |

Moda: **tambaqui** (22 registros).

**2.** Agrupe a cota em classes de 4 m e indique em qual classe há mais dias. O que isso revela sobre o rio?

| Classe (m) | Nº de dias |
|---|---|
| (8, 12] | 1 |
| (12, 16] | 15 |
| (16, 20] | 125 |
| (20, 24] | 77 |
| (24, 28] | 102 |
| (28, 36] | 45 |

A classe **(16, 20]** concentra mais dias; a segunda maior é **(24, 28]**. Há dois “grupos” de dias — águas baixas e águas altas — o que reflete o ciclo sazonal do rio. Aceitar: “a distribuição tem dois picos”.

**3.** Associe cada pergunta ao gráfico mais adequado: (a) Qual espécie é mais registrada? (b) Como a cota evoluiu em 2025? (c) A cota se distribui de forma simétrica? (d) Qual período tem maior variabilidade de cota?

**(a)** barras; **(b)** linhas; **(c)** histograma; **(d)** boxplot por período (altura da caixa/comprimento dos bigodes).

**4.** Observe o gráfico de linhas e descreva, em duas frases, o padrão da cota ao longo do ano. Há algum ponto que parece “estranho”? Qual?

Modelo: “A cota sobe de janeiro a junho, atinge o pico próximo de 28 m e desce até outubro-novembro, quando fica próxima de 16 m.” Pontos estranhos: as duas “agulhas” — leituras de **8,90 m (18/03)** e **35,10 m (09/08)**, incompatíveis com a evolução do rio (investigadas na Aula 6).

## Aula 3 — Conclusão da Oficina 1 e mini-relatório parcial (AV1)

**1.** Gere a tabela-resumo por período e identifique o período com maior diferença entre máximo e mínimo. Essa diferença é “real” ou há algum problema nos dados?

Enchente: 8,90 a 26,70 m (diferença 17,80 m); vazante: 17,40 a 35,10 m (17,70 m). As maiores diferenças estão em enchente e vazante, mas **parte delas é artificial**: os extremos 8,90 m e 35,10 m são leituras atípicas. Cheia (2,22 m) e seca (1,35 m) têm diferenças pequenas.

**2.** Escreva, em até 4 frases e linguagem acessível, a interpretação do gráfico de linhas da cota para um gestor da Defesa Civil.

Resposta livre. Esperado: (1) descrever o ciclo (sobe, pico, desce, vale); (2) citar valores aproximados (pico ≈ 28 m; vale ≈ 16 m); (3) citar o período de maior estabilidade; (4) mencionar leituras atípicas ou os limites dos dados. Pontuar clareza e ausência de jargão (ver rubrica da AV1).

**3.** Liste três limitações do relatório que você produziu.

Exemplos aceitos: dados de um único ano; base didática/simulada; leituras atípicas não tratadas; só uma estação de medição; nenhuma variável explicando causas; classificação de alerta é didática e não oficial.

## Aula 4 — Medidas de tendência central: média, mediana e moda

**1.** Para os dados 20, 25, 25, 34, 36 (cota em m), calcule média, mediana, moda e amplitude.

Soma = 140; n = 5. **Média = 28 m**. Ordenados já estão: mediana = **25 m**. Moda = **25 m**. Amplitude = 36 − 20 = **16 m**.

**2.** Calcule média, mediana e moda de 21, 23, 23, 24, 25, 27 e explique o resultado em uma frase.

Média 23,83 m; mediana 23,5 m; moda 23 m. Interpretação: o nível típico nessa semana ficou entre 23 e 24 m; as três medidas são próximas porque não há valor extremo.

**3.** Adicione o valor 60 aos dados do exercício 2. Recalcule a média e a mediana e compare.

Novos dados (n = 7): 21, 23, 23, 24, 25, 27, 60. Soma = 203 → **média = 29,00 m** (subiu 5,17 m). Mediana = 4º valor = **24 m** (subiu só 0,5 m). A média é sensível ao valor extremo; a mediana é robusta.

**4.** No CSV, qual é a espécie mais registrada (moda) e o alerta mais frequente? Por que a média não se aplica a essas colunas?

Espécie: **tambaqui** (22 de 53). Alerta: **baixo** (141 dias, 38,6%). São variáveis qualitativas: não há soma com sentido numérico.

**5.** A média diária de chuva do ano é maior ou menor que a mediana? O que isso diz sobre a distribuição da chuva?

Média 6,27 mm > mediana 1,30 mm. A distribuição é **assimétrica à direita**: muitos dias com pouca/nenhuma chuva e alguns dias com chuva forte puxando a média.

## Aula 5 — Medidas de variação: amplitude, variância e desvio-padrão

**1.** Para 18, 21, 21, 24, 26, calcule amplitude, variância e DP populacionais e amostrais.

Média 22; SQ = 38. Amplitude = **8 m**. Var. pop. = **7,6 m²**; DP pop. = **2,76 m**. Var. amostral = **9,5 m²**; DP amostral = **3,08 m**.

**2.** Duas estações registram média de 24 m. A estação X tem DP de 0,3 m e a Y, DP de 3 m. Qual é mais previsível? O que você diria a um gestor?

A **estação X**: seus valores ficam muito próximos da média. Texto-modelo: “Em X, a cota normalmente varia ±0,3 m em torno de 24 m; em Y, varia ±3 m, portanto um valor de 24 m é um bom resumo para X, mas não para Y.”

**3.** Por que a variância amostral divide por n − 1? Em que situação a diferença entre dividir por n e por n − 1 é menos relevante?

Porque a média usada no cálculo vem da própria amostra, o que subestima a dispersão; n − 1 corrige o viés (estimador não viciado da variância populacional). A diferença é pouco relevante quando n é **grande** (ex.: 365 ou 151 observações).

**4.** Por que o desvio-padrão é mais fácil de interpretar do que a variância?

Porque está na **mesma unidade** dos dados (metros), enquanto a variância está em unidade ao quadrado (m²).

**5.** Use a tabela por período: qual período é o mais previsível e qual o menos previsível? Qual medida você usou e por quê?

Mais previsível: **seca** (DP 0,334 m), seguida de cheia (0,594 m). Menos previsível: **enchente** (DP 3,303 m), seguida de vazante (3,181 m). Usa-se o DP por estar em metros e não depender só de dois valores como a amplitude. (Ressalva: enchente e vazante contêm leituras atípicas, que aumentam o DP.)

## Aula 6 — Quartis, outliers, normalização e padronização

**1.** Para 12, 14, 15, 16, 17, 18, 19, 21, 45, calcule Q1, Q3, IQR e os limites de Tukey. Existe outlier?

Q1 = 14,5; Q3 = 20,0; IQR = 5,5; limites = **6,25** e **28,25**. Sim: **45** é outlier. (Com o método do pandas: Q1 15, Q3 19, IQR 4, limites 9 e 25 — mesma conclusão.)

**2.** Normalize pelo método min-máx os valores 10, 20, 30, 50.

(x − 10) ÷ 40: **0,00; 0,25; 0,50; 1,00**.

**3.** Padronize os valores 10, 20, 30, 50 (use DP amostral).

Média = 27,5; DP amostral = 14,79. z = **-1,183; -0,507; 0,169; 1,521**. Aceitar pequenas diferenças de arredondamento; com DP populacional os valores são ligeiramente maiores em módulo.

**4.** Aplique a regra do IQR à temperatura da água. Quais são os limites e o que você faria com o valor atípico?

Q1 = 27,80; Q3 = 29,30; IQR = 1,50; limites **25,55** e **31,55 °C**. Atípico: **38,5 °C (22/10)**. Conduta esperada: verificar o sensor/anotação; sendo implausível para a água do rio, tratar como erro (corrigir ou excluir) e registrar a decisão no caderno de bordo.

**5.** O dia 18/03 tem cota de 8,90 m, e o dia seguinte, 23,80 m. É um outlier “real”? Justifique.

Não. A diferença de 14,9 m em 1 dia é fisicamente impossível; trata-se de **erro de leitura/registro**. Pontuar: uso do teste de plausibilidade, distinção entre atípico e erro e decisão de tratamento registrada.

**6.** Por que a normalização min-máx é mais sensível a outliers do que a mediana e o IQR?

Porque depende **diretamente** do mínimo e do máximo; um único valor extremo altera o denominador e comprime todos os demais em uma faixa estreita. Mediana e IQR dependem das posições centrais e ignoram os extremos.

## Aula 7 — Dispersão entre duas variáveis e covariância

**1.** Calcule a covariância amostral entre X = 1, 2, 3, 4, 5 e Y = 2, 4, 5, 4, 5.

Soma dos produtos dos desvios = 6; cov amostral = 6 ÷ 4 = **1,5** (populacional: 1,2).

**2.** O que significa uma covariância negativa entre cota e temperatura da água? Isso prova que a cota diminui a temperatura?

Significa que, em geral, quando a cota está acima da média, a temperatura está abaixo da média (e vice-versa). **Não prova causa**: só descreve a associação (a estação do ano pode explicar ambas; ver Aula 9).

**3.** Por que a covariância entre cota (em cm) e temperatura é 100 vezes maior que com a cota em metros? Qual medida resolve esse problema?

Porque a covariância carrega as unidades das duas variáveis (m·°C ou cm·°C). A **correlação de Pearson** divide pelos desvios-padrão e é adimensional.

**4.** Qual é o valor da diagonal da matriz de covariância e o que ele representa?

É a variância de cada variável consigo mesma (ex.: 20,528 m² para a cota).

## Aula 8 — Correlação de Pearson

**1.** Calcule r para X = 1,2,3,4,5 e Y = 2,4,5,4,5 e classifique a relação.

r = 1,5 ÷ (1,5811 × 1,2247) = **0,7746** ≈ 0,77 → **forte e positiva**.

**2.** Classifique cada relação: r = +0,95; r = −0,35; r = 0,05; r = −0,82.

+0,95: forte, positiva; −0,35: fraca, negativa; 0,05: praticamente nula (sem relação linear); −0,82: forte, negativa.

**3.** Entre cota e temperatura o r é -0,924. Qual o valor de r² e o que significa?

r² = 0,854 ≈ **0,854**. Aproximadamente 85% da variação da cota é acompanhada linearmente pela temperatura (associação, não causa).

**4.** Cota × chuva (mesmo dia) tem r ≈ −0,09. Podemos concluir que a chuva não afeta o nível do rio? Justifique.

Não. r mede apenas relação **linear** e **simultânea**. A chuva age sobre o rio de forma acumulada e defasada: a correlação com a chuva acumulada dos 30 dias anteriores é 0,135, e mesmo assim é fraca, porque a cota do Rio Negro depende de toda a bacia, não só da chuva local.

**5.** Explique por que um único valor atípico pode alterar bastante r. Cite o exemplo do projeto.

r usa médias e desvios, que são sensíveis a extremos. Ao incluir a leitura de 38,5 °C, r(cota, temperatura) muda de -0,924 para -0,830.

## Aula 9 — Correlação não é causalidade — Oficina 2 e AV2

**1.** Um estudo encontrou correlação r = 0,85 entre o número de jogadores online e as quedas de energia em uma cidade. Liste duas explicações não causais possíveis.

Exemplos: variável de confusão (horário noturno e calor aumentam tanto o uso de jogos quanto a demanda de energia); coincidência/tendência temporal (ambas crescem com a população). Aceitar respostas equivalentes.

**2.** Explique, com suas palavras, o que é variável de confusão e dê um exemplo do Rio Negro.

É uma terceira variável que influencia as outras duas e cria uma associação aparente entre elas. Exemplo: o período hidrológico (estação) afeta a cota e a temperatura da água; sem controlá-lo, parece que a cota “causa” a temperatura.

**3.** Reescreva a frase “o aumento da temperatura reduz a cota do rio” de modo cientificamente mais cuidadoso.

“Nos dados de 2025, cota e temperatura da água apresentaram forte correlação negativa (r = -0,92), possivelmente devido à sazonalidade; os dados não permitem afirmar que uma causa a outra.”

**4.** Cite três condições que reforçam um argumento de causalidade.

Ordem temporal; mecanismo plausível; experimento controlado/randomizado; controle de variáveis de confusão; consistência em vários estudos. (Quaisquer três.)

## Aula 10 — Probabilidade: eventos, regra da soma e regra do produto

**1.** Um dado de 6 faces é lançado. Calcule P(par), P(maior que 4) e P(par ou maior que 4).

P(par) = 3/6 = 0,5; P(>4) = 2/6 ≈ 0,3333; P(par e >4) = 1/6 (o 6). P(par ou >4) = 3/6 + 2/6 − 1/6 = **4/6 ≈ 0,6667**.

**2.** No CSV, calcule P(alerta alto) e P(não alto). Explique em uma frase.

P(alto) = 125/365 = **0,3425** (34,3%); P(não alto) = **0,6575**. Cerca de 1 em cada 3 dias do ano teve alerta alto.

**3.** Calcule P(alto ou choveu) e confira com a contagem direta.

P = 0,3425 + 0,5342 − 0,1671 = **0,7096**; contagem direta: 259 dias em 365.

**4.** Se “alerta alto” e “choveu” fossem independentes, quantos dias com os dois eventos esperaríamos? Compare com o observado.

Esperado: 0,1830 × 365 ≈ **66,8 dias**; observado: **61**. Pequena diferença: não há evidência forte contra a independência (o formalismo vem na Aula 16).

**5.** Explique a diferença entre eventos mutuamente exclusivos e eventos independentes. Dê um exemplo de cada.

Exclusivos: não ocorrem juntos (alerta baixo e alerta alto no mesmo dia). Independentes: um não altera a probabilidade do outro (duas moedas lançadas). Exclusivos com probabilidade positiva são dependentes.

## Aula 11 — Probabilidade condicional

**1.** Em uma urna há 4 bolas azuis e 6 vermelhas. Retiram-se duas bolas sem reposição. Qual a probabilidade de a segunda ser azul dado que a primeira foi azul?

Restam 9 bolas, sendo 3 azuis: P = 3/9 = **1/3 ≈ 0,3333**.

**2.** Use a tabela cruzada do projeto e calcule P(alto | choveu) e P(choveu | alto).

P(alto | choveu) = 61/195 = **0,3128**; P(choveu | alto) = 61/125 = **0,4880**.

**3.** Compare P(alto | choveu) com P(alto). Há indício de dependência?

P(alto) = 0,3425 e P(alto | choveu) = 0,3128: diferença de 3,0 pontos percentuais; pequena. Indício **fraco** de dependência (a conclusão formal exige um teste estatístico).

**4.** Em qual período a chance de chover é maior? Qual é menor? Cite as probabilidades.

Maior: enchente (0,755). Menor: vazante (0,180).

**5.** Explique, com um exemplo seu, por que P(A|B) ≠ P(B|A).

Resposta livre. Esperado: exemplo em que as duas condicionais tenham valores claramente diferentes (ex.: todo tambaqui é peixe, mas nem todo peixe é tambaqui).

## Aula 12 — Teorema de Bayes (intuição) — Oficina 3

**1.** Refaça o alarme de cheia com P(cheia) = 0,20, sensibilidade 0,95 e falso positivo 0,10. Calcule P(alarme) e P(cheia | alarme).

P(alarme) = 0,95×0,20 + 0,10×0,80 = 0,19 + 0,08 = **0,27**; P(cheia | alarme) = 0,19 ÷ 0,27 = **0,7037** (≈ 70,4%).

**2.** Explique por que o mesmo alarme é menos confiável quando o evento é raro.

Porque, sendo o evento raro, a maioria dos dias é “normal”; mesmo uma pequena taxa de falsos positivos produz muitos alarmes falsos, que superam os poucos alarmes verdadeiros. A posteriori depende da a priori.

**3.** Verifique, no projeto, que P(alto | chuva > 10) por Bayes coincide com a contagem direta.

Bayes: 0,272 × 0,3425 ÷ 0,2521 ≈ **0,3696**; direto: **0,3696**.

**4.** Cite duas aplicações de Bayes em IA.

Filtro de spam (Naive Bayes); diagnóstico/triagem automatizada; classificação de textos; sistemas de recomendação; detecção de fraude. (Quaisquer duas.)

## Aula 13 — Distribuição Normal

**1.** Se X ~ N(28; 2), calcule o escore z de x = 30 e de x = 25. Interprete.

z(30) = (30 − 28) ÷ 2 = **+1**; z(25) = (25 − 28) ÷ 2 = **−1,5**. O valor 30 está 1 DP acima da média; o 25, 1,5 DP abaixo.

**2.** Se X ~ N(28; 2), qual a proporção aproximada de valores entre 26 e 30? Qual o valor de P(X < 30)?

Entre μ − 1σ e μ + 1σ → **≈ 68%** (valor exato 0,6827). P(X < 30) = P(Z < 1) = **0,8413** (≈ 84,1%).

**3.** Com a temperatura ~ N(28,56; 0,884), calcule P(T < 28) e P(T > 30). O que significa o resultado em linguagem simples?

P(T < 28) ≈ **0,2634**: em cerca de 26% dos dias, a água estaria abaixo de 28 °C. P(T > 30) ≈ **0,0517**: água acima de 30 °C é rara (≈ 1 dia em 20).

**4.** A chuva diária pode ser modelada por uma normal? Justifique com base no histograma e nas medidas descritivas.

Não é adequado: média (6,27) muito maior que a mediana (1,30), assimetria à direita, muitos zeros e valores nunca negativos. A normal é simétrica e admite valores negativos.

## Aula 14 — Distribuições Binomial e de Poisson

**1.** Em 10 lançamentos de uma moeda justa, calcule P(X = 5) e P(X ≥ 8).

P(X = 5) = **0,2461**; P(X ≥ 8) = **0,0547**.

**2.** Para X ~ Bin(30; 0,3425), calcule a média e o desvio-padrão e interprete.

μ = 30 × 0,3425 ≈ **10,3 dias**; σ = √(30 × 0,3425 × 0,6575) ≈ **2,6 dias**. Em um mês de 30 dias esperam-se cerca de 10 dias de alerta alto, com variação típica de ±2,6 dias.

**3.** Se chegam em média 2 alertas por semana a um centro de monitoramento (Poisson), qual a probabilidade de uma semana sem nenhum alerta? E de 2 ou mais?

P(0) = e⁻² = **0,1353** (≈ 13,5%); P(≥ 2) = **0,5940** (≈ 59,4%).

**4.** Chuvas fortes ocorrem em média λ = 0,583 dias por mês. Calcule P(0) e P(≥ 3).

P(0) = **0,5580**; P(≥ 3) = **0,0215** (≈ 2,2%).

**5.** Por que o modelo binomial para “dias com alerta alto” é só uma aproximação?

Porque exige ensaios independentes e p constante; os dias do rio são **dependentes** (autocorrelação) e p varia com a estação.

## Aula 15 — População, amostra, viés de amostragem e erro-padrão

**1.** Defina população e amostra e dê um exemplo para cada um no contexto do Rio Negro.

População: todas as leituras diárias de cota feitas em Manaus em todos os anos; amostra: as leituras de julho de 2025. (Aceitar variações coerentes.)

**2.** Uma amostra de n = 36 tem desvio-padrão populacional σ = 3. Calcule o erro-padrão. O que acontece com ele se n for quadruplicado (144)?

EP = 3 ÷ √36 = **0,5**; com n = 144: 3 ÷ 12 = **0,25** (cai à metade).

**3.** Um pesquisador mediu a temperatura apenas na seca e concluiu que a água do rio “é quente o ano todo”. Qual é o problema?

Viés de seleção: a amostra cobre apenas a seca (média 29,68 °C), que é o período mais quente; a média anual é 28,56 °C e a cheia é mais fria (27,49 °C).

**4.** Aumentar o tamanho de uma amostra viciada resolve o viés? Justifique.

Não. Mais dados do mesmo processo enviesado apenas reduzem a variação aleatória; o erro sistemático permanece.

**5.** Cite duas formas de reduzir o viés de amostragem ao planejar uma coleta.

Amostragem aleatória; amostragem estratificada (por período/estação); coleta ao longo de todo o ciclo; padronização de instrumentos; evitar voluntários. (Quaisquer duas.)

## Aula 16 — Intervalo de confiança, hipóteses e p-valor — AV3

**1.** Uma amostra de n = 25 tem x̄ = 50 e s = 10. Construa o IC de 95% para a média.

EP = 10 ÷ 5 = 2; t(24 g.l.) = 2,0639; margem ≈ 4,13. **IC95% = [45,87 ; 54,13]**. (Aceitar o uso de z = 1,96, que dá [46,08 ; 53,92].)

**2.** O IC95% da temperatura média é [28,469; 28,651]. Interprete corretamente e diga se a média 29 °C é plausível.

O método gera intervalos que capturam a média verdadeira em 95% das amostras; a estimativa vai de 28,47 a 28,65 °C. O valor 29 °C está **fora** do intervalo, portanto é pouco compatível com os dados.

**3.** Explique o que é p-valor sem usar fórmulas e o que significa p = 0,03 com α = 0,05.

Probabilidade de obter dados tão extremos quanto os observados se H₀ fosse verdadeira. Com p = 0,03 < 0,05, rejeita-se H₀ (há evidência estatística contra ela), mas isso não mede a importância prática.

**4.** Um teste resultou em p = 0,40. A conclusão “comprovamos que não há diferença” está correta? Justifique.

Não. p = 0,40 indica apenas que **não há evidência suficiente** para rejeitar H₀; ausência de evidência não é evidência de ausência (a amostra pode ser pequena).

**5.** Por que o p-valor do teste entre cheia e seca é praticamente zero, enquanto o dos dois sorteios é 0,90?

Entre cheia e seca há diferença real (27,49 × 29,68 °C, ≈ 2,2 °C) com muitos dados e baixa variação, o que torna o t muito grande. Nos sorteios do mesmo conjunto, não há diferença real, e o p-valor é alto.

## Aula 17 — Vetores e matrizes: dados como números organizados

**1.** Dados C = [[2, 0], [1, 3]] e D = [[1, 4], [2, 5]], calcule C + D, 2·C e C·D.

C + D = [[3, 4], [3, 8]]; 2·C = [[4, 0], [2, 6]]; C·D = [[2, 8], [7, 19]].

**2.** Calcule D·C e compare com C·D. O que se conclui?

D·C = [[1·2+4·1, 1·0+4·3], [2·2+5·1, 2·0+5·3]] = **[[6, 12], [9, 15]]**, diferente de C·D = [[2, 8], [7, 19]]. O produto de matrizes **não é comutativo**.

**3.** Uma matriz tem dimensão 5 × 3 e outra 3 × 4. É possível multiplicá-las? Qual a dimensão do resultado? E na ordem inversa?

Sim: colunas da 1ª (3) = linhas da 2ª (3) → resultado **5 × 4**. Na ordem inversa (3×4 por 5×3) **não é possível**: 4 ≠ 5.

**4.** Qual é a dimensão da matriz X do projeto e o que representam suas linhas e colunas?

364 × 3: 364 observações (dias com leituras válidas) por 3 *features* (cota, chuva, temperatura).

**5.** Escreva a transposta de A = [[1, 2, 3], [4, 5, 6]] e informe sua dimensão.

Aᵀ = [[1, 4], [2, 5], [3, 6]], dimensão 3 × 2.

## Aula 18 — Produto escalar, funções lineares e não lineares

**1.** Calcule [1, −2, 3] · [4, 0, −1].

1·4 + (−2)·0 + 3·(−1) = 4 + 0 − 3 = **1**.

**2.** Um modelo tem w = [0,5; 0,1; −0,2] e b = 3. Calcule a previsão para o dia x = [22; 8; 25].

0,5·22 + 0,1·8 + (−0,2)·25 + 3 = 11 + 0,8 − 5 + 3 = **9,8**.

**3.** Classifique como linear ou não linear: (a) y = 3x + 2; (b) y = x²; (c) y = 5; (d) y = 2ˣ.

(a) linear; (b) não linear; (c) linear (constante, reta horizontal); (d) não linear (exponencial).

**4.** Por que uma reta não é um bom modelo para a cota ao longo do ano? Use o EQM.

Porque a cota sobe e desce (ciclo sazonal), e uma reta tem taxa constante. EQM da reta = 15,85 contra 2,81 do grau 3: o erro é cerca de 5,6 vezes maior.

**5.** O que é *overfitting* e por que avaliar o modelo com dados novos?

Quando o modelo se ajusta tanto aos dados de treino (inclusive ao ruído) que perde capacidade de generalizar. Avaliar em dados novos mostra o desempenho real.

## Aula 19 — Erro, derivada e gradiente descendente

**1.** Para ŷ = w·x com x = [1, 2, 3], y = [2, 4, 6] e w = 1: calcule a loss, o gradiente e o novo w com α = 0,1.

L = 4,6667; gradiente = -9,3333; novo w = **1,9333**.

**2.** Para w = 2, quanto vale a loss? O que o gradiente vale nesse ponto?

L(2) = **0** (erros nulos) e o gradiente é **0**: é o mínimo; o gradiente descendente para.

**3.** Explique o que acontece se a taxa de aprendizado for muito pequena e se for muito grande.

Muito pequena: convergência lentíssima (muitos passos). Muito grande: ultrapassa o mínimo, oscila ou diverge (a loss cresce).

**4.** O gradiente de uma loss em w é +5. Devemos aumentar ou diminuir w? Por quê?

**Diminuir**: gradiente positivo significa que a loss cresce quando w cresce; andamos no sentido contrário (w − α·5).

**5.** No projeto, w = −0,8159 para a cota padronizada. Interprete.

A cada aumento de 1 desvio-padrão na cota, a temperatura prevista cai cerca de 0,82 °C (associação, não causalidade).

## Aula 20 — Síntese do projeto: painel de indicadores e mini-relatório final — AV4

**1.** Rode o código e reproduza a tabela de indicadores. Qual período tem maior e qual tem menor DP depois do tratamento?

Maior DP: enchente (3,16 m); menor: seca (0,33 m).

**2.** Escreva um parágrafo de conclusão (5 a 7 linhas) que use pelo menos três medidas do painel e uma ressalva.

Resposta livre. Verificar: uso correto de ≥ 3 medidas; linguagem de associação; menção ao tratamento e às limitações (base simulada, um ano).
