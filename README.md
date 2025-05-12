# 🧠 Otimizador de Carteiras - Programação Funcional e Paralelismo

Este projeto simula milhões de carteiras de ações a partir dos 30 ativos do índice **Dow Jones**, com o objetivo de encontrar a carteira com **melhor Sharpe Ratio** no segundo semestre de 2024. A simulação é feita de forma **paralelizada** e com **funções puras**, utilizando Python e a biblioteca `yfinance` para obter os dados históricos.

---

## 📁 Estrutura do Projeto

```
prog-fung-proj/
├── main.py                         # Versão paralela completa
├── main_estimate_no_parallel.py    # Estimativa de tempo sequencial
├── data/
│   └── data.csv                    # Preços históricos das ações
├── data_loader.py                  # Função para ler os dados de data.csv
├── get_data.py                     # Script para baixar dados com yfinance
├── simulate.py                     # Simulação da melhor carteira
├── utils.py                        # Funções puras: Sharpe, retorno, pesos
├── test_q1_2025.py                 # Teste fora da amostra no Q1 de 2025
└── README.md                       # Este arquivo
└──requirements.txt                 # Dependências do projeto
```

---

## 📦 Como Instalar

Requisitos:
- Python 3.10 ou superior
- Pip

Instale as dependências com:

```bash
pip install -r requirements.txt
```
---

## ▶️ Como Executar

### 1. Baixar os dados (Ago-Dez/2024)

```bash
python data_loader/fetch_data.py
```

### 2. Rodar a versão paralela (ProcessPoolExecutor)

```bash
python main.py
```


### 3. Estimar o tempo da versão sequencial com 100 combinações

```bash
python main_estimate_no_parallel.py
```

### 4. Testar a melhor carteira fora da amostra (Jan-Mar/2025)

```bash
python test_q1_2025.py
```

---

## ✅ Requisitos do Projeto Atendidos

- ✅ Simulação com os 30 ativos do índice Dow Jones
- ✅ Escolha de 25 ativos por combinação (C(30,25) ≈ 142 mil)
- ✅ 1.000 simulações de pesos por combinação
- ✅ Restrição: pesos ≤ 20%, carteira long-only
- ✅ Cálculo do Sharpe Ratio, retorno e volatilidade com funções puras
- ✅ Paralelismo com `ProcessPoolExecutor`
- ✅ Obter os dados sob demanda via alguma API
- ✅ Teste fora da amostra no Q1 de 2025
- ✅ Comparação entre tempo com e sem paralelismo
- ✅ README completo com explicações e instruções

---

## 📊 Resultados

### Melhor Carteira (Ago-Dez 2024)

- **Sharpe Ratio**: `≈ 3.50`
- **Número de ativos**: 25
- **Limite por ativo**: 20%
- **Carteira long-only**: Sim

### Saída do Terminal

```bash

(env) ➜  prog-fung-proj git:(main) ✗ python3 main.py
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 142506/142506 [4:15:11<00:00,  9.31it/s]

🏆 Best Sharpe Ratio: 3.5076
📊 Assets and Weights:
AAPL: 0.0422
AXP: 0.0363
CAT: 0.0046
CRM: 0.1601
CSCO: 0.0052
CVX: 0.0156
DIS: 0.0665
GS: 0.0127
HD: 0.0175
IBM: 0.0195
JNJ: 0.0099
JPM: 0.0255
KO: 0.0777
MCD: 0.0291
MRK: 0.0050
MSFT: 0.0052
NKE: 0.0031
NVDA: 0.0442
PG: 0.0205
SHW: 0.0074
TRV: 0.0218
UNH: 0.0015
V: 0.1618
VZ: 0.0131
WMT: 0.1942
```

### Estimativa de Tempo Sequencial

#### Saída do Terminal

```bash
env➜  prog-fung-proj git:(main) ✗ python3 test.py 
🔎 Estimando tempo com 100 combinações...
Rodando amostra: 100%|████████████████| 100/100 [00:37<00:00,  2.66it/s]

🕒 Tempo estimado total (sem paralelismo): 14:53:08.453440 (893.14 minutos)
env➜  prog-fung-proj git:(main) ✗ 
```

### Performance fora da amostra (Jan-Mar 2025)

### Saída do Terminal

```bash

env➜  prog-fung-proj git:(main) ✗ python3 test_q1_2025.py
YF.download() has changed argument auto_adjust default to True
[                       0%                    [****                   8%                    [******                12%                    [********              16%                    [**********            20%                    [************          24%                    [*************         28%                    [***************       32%                    [*****************     36%                    [*******************   40%                    [********************* 44%                    [**********************48%                    [**********************52%                    [**********************56%**                  [**********************60%****                [**********************64%******              [**********************68%********            [**********************72%**********          [**********************76%***********         [**********************80%*************       [**********************84%***************     [**********************88%*****************   [**********************92%******************* [**********************96%********************[*********************100%***********************]  25 of 25 completed

📈 Desempenho no 1º trimestre de 2025:
🔹 Retorno anualizado: -0.1182
🔹 Volatilidade anualizada: 0.1549
🔹 Sharpe Ratio: -0.8925

```


---

## 🤝 Créditos

Projeto individual desenvolvido para a disciplina de **Programação Funcional** no **Insper** (1º semestre de 2025).  
Professor: Raul Ikeda
Aluno: Matheus Aguiar de Jesus



## 📜 Notas

Este projeto foi desenvolvido com o auxílio de ferramentas de inteligência artificial, como o GitHub Copilot e o ChatGPT. 
Essas ferramentas foram utilizadas para:

- Correção e criação de código.
- Auxílio no entendimento dos conceitos do projeto.
- Realização de correções ortográficas.

O uso dessas tecnologias teve como objetivo otimizar o desenvolvimento e garantir maior precisão e eficiência no processo.
