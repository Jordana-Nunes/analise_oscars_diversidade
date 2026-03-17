# GUIA DE USO E PERSONALIZAÇÃO

## Como Usar Este Projeto

---

## 🚀 Execução Rápida

### Método 1: Linha de Comando
```bash
cd c:\Users\leona\oscar_analise
python oscars.py
```

**Saída Esperada**:
- Análise completa no console
- 2 imagens PNG (gráficos)
- 1 arquivo CSV (dados brutos)

### Método 2: Terminal PowerShell
```powershell
cd c:\Users\leona\oscar_analise
python .\oscars.py
```

### Método 3: Jupyter Notebook
```python
import subprocess
subprocess.run(['python', 'oscars.py'])
```

---

## 📝 Estrutura do Código Python

### Seção 1: Importações e Configuração
```python
import pandas as pd           # Manipulação de dados
import numpy as np           # Operações numéricas
import matplotlib.pyplot as plt  # Visualizações
import seaborn as sns        # Temas visuais
import warnings              # Controle de avisos
```

### Seção 2: Carregamento de Dados
```python
def carregar_dados_oscars():
    """
    Retorna DataFrame com estrutura:
    - ano: Anos de análise (1929-2023)
    - total_nomeados: Total de participantes
    - nomeados_[grupo]: Contagem por etnia
    - vencedores_[grupo]: Vencedores por etnia
    """
```

### Seção 3: Cálculo de Métricas
```python
def calcular_metricas(df):
    """
    Adiciona colunas:
    - prop_[grupo]: Proporções percentuais
    - indice_simpson: Índice de diversidade
    """
```

### Seção 4: Análise Exploratória
```python
def analise_dados(df):
    """
    Imprime:
    - Estatísticas básicas
    - Crescimento por grupo
    - Índices de diversidade
    - Proporções atuais
    """
```

### Seção 5: Criação de Gráficos
```python
def criar_graficos(df):
    """
    Gera:
    - oscars_diversidade_completo.png (6 gráficos)
    - oscars_diversidade_resumido.png (infográfico)
    """
```

---

## 🔧 PERSONALIZAÇÃO

### 1. Modificar Dados da Fonte

**Localização**: Função `carregar_dados_oscars()`

**Exemplo - Adicionar novo ano (2024)**:
```python
'ano': [..., 2023, 2024],  # Adicionar 2024
'total_nomeados': [..., 240, 245],  # Adicionar total
'nomeados_caucasianos': [..., 140, 142],  # Adicionar caucasianos
# ... e assim por diante para cada grupo
```

### 2. Mudar Cores dos Gráficos

**Localização**: Dicionário `cores` em `criar_graficos()`

**Exemplo**:
```python
cores = {
    'Caucasianos': '#1f77b4',      # Azul
    'Afroamericanos': '#ff7f0e',   # Laranja
    'Latinos': '#2ca02c',          # Verde
    'Asiaticos': '#d62728',        # Vermelho
    'Outros': '#9467bd'            # Roxo
}

# Mudar para cores diferentes:
cores = {
    'Caucasianos': '#000000',      # Preto
    'Afroamericanos': '#FFD700',   # Ouro
    'Latinos': '#00FF00',          # Verde neon
    'Asiaticos': '#FF1493',        # Rosa profundo
    'Outros': '#00CED1'            # Turquesa
}
```

### 3. Adicionar Novos Gráficos

**Exemplo - Adicionar gráfico de pizza**:
```python
def criar_graficos(df):
    # ... código existente ...
    
    # Novo gráfico de pizza
    ax7 = plt.subplot(2, 3, 7)
    labels = ['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros']
    sizes = [
        df['prop_caucasianos'].iloc[-1],
        df['prop_afroamericanos'].iloc[-1],
        df['prop_latinos'].iloc[-1],
        df['prop_asiaticos'].iloc[-1],
        df['prop_outros'].iloc[-1]
    ]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    ax7.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    ax7.set_title('Distribuição 2023 (Pizza)', fontweight='bold')
```

### 4. Adicionar Novas Métricas

**Exemplo - Calcular razão de representação**:
```python
def calcular_metricas(df):
    # ... código existente ...
    
    # Razão: proporção de vencedores / proporção de nomeados
    df['razao_vencedores_caucasianos'] = (
        df['prop_venc_caucasianos'] / 
        df['prop_caucasianos'].replace(0, 1)
    )
    
    df['razao_vencedores_afroamericanos'] = (
        df['prop_venc_afroamericanos'] / 
        df['prop_afroamericanos'].replace(0, 1)
    )
    
    return df
```

### 5. Mudar Período de Análise

**Exemplo - Focar apenas em 2000-2023**:
```python
def analise_dados(df):
    # Filtrar dados
    df_recente = df[df['ano'] >= 2000]
    
    # Usar df_recente em vez de df para todas operações
    print(f"Análise: {df_recente['ano'].min()} - {df_recente['ano'].max()}")
```

---

## 📈 EXEMPLOS DE ANÁLISES ADICIONAIS

### Análise 1: Diferenças Ano a Ano
```python
def calcular_diferenca_anual(df):
    """Calcula mudança de um ano para outro"""
    df['delta_caucasianos'] = df['nomeados_caucasianos'].diff()
    df['delta_afroamericanos'] = df['nomeados_afroamericanos'].diff()
    return df

# Encontrar maior crescimento
print(df[['ano', 'delta_afroamericanos']].nlargest(1, 'delta_afroamericanos'))
```

### Análise 2: Taxa de Crescimento Exponencial
```python
import math

def calcular_taxa_exponencial(df):
    """Estima se crescimento é exponencial"""
    inicial = df['nomeados_afroamericanos'].iloc[0]
    final = df['nomeados_afroamericanos'].iloc[-1]
    anos = df['ano'].iloc[-1] - df['ano'].iloc[0]
    
    # Fórmula exponencial: final = inicial * e^(r*anos)
    r = math.log(final / max(inicial, 1)) / anos
    
    return r

taxa = calcular_taxa_exponencial(df)
print(f"Taxa de crescimento anual: {taxa:.2%}")
```

### Análise 3: Projeção Futura
```python
def projetar_futuro(df, anos_futuros=10):
    """Projeta diversidade para próximos N anos"""
    ultimo_idx = df['indice_simpson'].iloc[-1]
    ultimo_ano = df['ano'].iloc[-1]
    
    # Modelo simples: crescimento linear reduzido
    taxa_anual = 0.01  # 1% ao ano
    
    projections = []
    for i in range(1, anos_futuros + 1):
        ano_proj = ultimo_ano + i
        idx_proj = min(ultimo_idx + (taxa_anual * i), 1.0)  # Máximo = 1.0
        projections.append({'ano': ano_proj, 'indice_simpson_proj': idx_proj})
    
    df_proj = pd.DataFrame(projections)
    return df_proj
```

### Análise 4: Investigar Disparidades
```python
def analise_disparidade(df):
    """Identifica grupos com maior gap vencedor/nomeado"""
    
    grupos = ['caucasianos', 'afroamericanos', 'latinos', 'asiaticos', 'outros']
    
    for grupo in grupos:
        # Calcular gap médio ao longo do tempo
        prop_nom = df[f'prop_{grupo}'].mean()
        vencedores_total = sum(df[f'vencedores_{grupo}'])
        nomeados_total = sum(df[f'nomeados_{grupo}'])
        
        if nomeados_total > 0:
            taxa_vitoria = (vencedores_total / nomeados_total) * 100
            print(f"{grupo}: {taxa_vitoria:.1f}% de nomeados viram vencedores")
```

---

## 🔍 TROUBLESHOOTING

### Problema 1: "ModuleNotFoundError: No module named 'pandas'"

**Solução**:
```bash
pip install pandas numpy matplotlib seaborn
```

### Problema 2: "Encoding Error" ao executar

**Solução**:
```bash
# No PowerShell:
$env:PYTHONIOENCODING = "utf-8"
python oscars.py

# Ou adicione ao topo do arquivo:
# -*- coding: utf-8 -*-
```

### Problema 3: Gráficos não aparecem

**Solução**:
```python
# Adicionar ao final do arquivo:
plt.show()
```

### Problema 4: CSV não é gerado

**Solução**:
```python
# Verificar permissões do diretório
import os
print(os.access('.', os.W_OK))  # Deve retornar True

# Ou salvar em diferente local
df.to_csv(r'C:\Users\[user]\Desktop\analise.csv')
```

---

## 📊 EXPORTAR PARA OUTROS FORMATOS

### Exportar para Excel
```python
# Adicionar ao código principal
df.to_excel('analise_oscars_diversidade.xlsx', index=False)
```

**Requer**: `pip install openpyxl`

### Exportar para HTML
```python
html_table = df.to_html()
with open('tabela_oscars.html', 'w') as f:
    f.write(html_table)
```

### Exportar Gráficos em PDF
```python
# Mudar:
fig.savefig('oscars_diversidade_completo.png', ...)

# Para:
fig.savefig('oscars_diversidade_completo.pdf', ...)
```

---

## 🎓 APRENDER MAIS

### Conceitos Utilizados
- **Análise Exploratória de Dados (EDA)**: Técnica base
- **Índice Simpson**: Diversidade biológica/demográfica
- **Visualização de Dados**: Matplotlib/Seaborn
- **Série Temporal**: Padrões ao longo do tempo

### Recursos Recomendados
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Índice Simpson Explicado](https://en.wikipedia.org/wiki/Simpson%27s_diversity_index)

### Cursos Relacionados
- "Data Analysis with Python" (Udacity)
- "Data Visualization with Matplotlib" (DataCamp)
- "Statistical Analysis Python" (Coursera)

---

## 💡 DICAS AVANÇADAS

### Usar com Jupyter Notebook
```python
# Célula 1: Importações
%matplotlib inline
import pandas as pd
# ... etc

# Célula 2: Carregar e processar
df = carregar_dados_oscars()
df = calcular_metricas(df)

# Célula 3: Visualizar
criar_graficos(df)

# Célula 4: Exportar
df.to_csv('resultado.csv')
```

### Integrar com Dashboard (Plotly/Dash)
```python
import plotly.express as px

def criar_dashboard(df):
    fig = px.area(df, x='ano', y=['prop_caucasianos', 'prop_afroamericanos', 
                                   'prop_latinos', 'prop_asiaticos', 'prop_outros'])
    fig.show()
```

### Automatizar Execução (Windows Task Scheduler)
```batch
# arquivo: executar_analise.bat
@echo off
cd C:\Users\leona\oscar_analise
python oscars.py
pause
```

Agendar para rodar automaticamente diariamente/semanalmente.

---

**Última Atualização**: Março 16, 2026
**Versão do Código**: 1.0
**Compatibilidade**: Python 3.8+
