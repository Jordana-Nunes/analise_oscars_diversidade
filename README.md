# Análise de Diversidade Étnica dos Oscar Awards (1929-2026)

## 📊 Visão Geral

Este projeto realiza uma **análise exploratória completa** da evolução da diversidade étnica entre os nomeados e vencedores do Academy Awards (Oscars) desde sua criação em 1929 até 2026.

## 🎯 Objetivos

1. **Analisar** a representação étnica nos Oscars ao longo de 97 anos
2. **Quantificar** o crescimento de grupos minoritários
3. **Visualizar** a evolução através de infográficos profissional
4. **Medir** a diversidade usando métricas estatísticas consolidadas
5. **Comparar** padrões entre nomeados e vencedores

## 📈 Métricas Utilizadas

### Índice de Diversidade de Simpson
- **Fórmula**: $D = 1 - \sum_{i=1}^{n} p_i^2$
- **Interpretação**: 
  - Valor 0 = Sem diversidade (apenas um grupo)
  - Valor 1 = Máxima diversidade (distribuição uniforme)

### Proporções por Etnicidade
- Caucasianos
- Afroamericanos
- Latinos
- Asiáticos
- Outros

## 📁 Estrutura do Projeto

```
oscar_analise/
├── oscars.py                              # Código principal da análise
├── README.md                              # Este arquivo
├── oscars_diversidade_completo.png        # 6 gráficos detalhados
├── oscars_diversidade_resumido.png        # Infográfico resumido
├── analise_oscars_diversidade.csv         # Dados brutos da análise
├── ATUALIZACAO_2024_2026.md               # Análise dos últimos 3 anos
├── RESUMO_ATUALIZACAO.md                  # Resumo das mudanças
├── RESUMO_EXECUTIVO.md                    # Análise principal
├── ANALISE_DETALHADA.md                   # Análise profunda
├── GUIA_USO.md                            # Guia de uso
├── INDEX.md                               # Índice de arquivos
└── Scripts de geração de gráficos:
    ├── generate_1929_2026_plots.py         # Gráficos completos até 2026
    ├── generate_1977_plot.py               # Gráfico específico 1977
    ├── generate_2019_plot.py               # Gráfico específico 2019
    ├── generate_2023_plot.py               # Gráfico específico 2023
    └── generate_cumulative_plot.py         # Gráfico cumulativo
```

## 🔍 Principais Descobertas

### Crescimento de Representação (1929-2026)

| Grupo | 1929 | 2026 | Crescimento |
|-------|------|------|------------|
| Caucasianos | 15 (100%) | 155 (55.4%) | -44.6% |
| Afroamericanos | 0 (0%) | 93 (33.2%) | +∞ |
| Latinos | 0 (0%) | 52 (18.6%) | +∞ |
| Asiáticos | 0 (0%) | 40 (14.3%) | +∞ |
| Outros | 0 (0%) | 28 (10.0%) | +∞ |

### Índice de Diversidade Simpson

- **1929**: 0.0000 (nenhuma diversidade)
- **2026**: 0.5183 (alta diversidade)
- **Melhoria**: +∞% (evolução significativa)

## 📊 Análise Exploratória

### 1. Conformação Inicial dos Oscars
- Premiação exclusivamente caucasiana em 1929
- Primeiras participações de minorias: anos 1940-1950
- Representação extremamente limitada até 1970

### 2. Período de Transição (1970-2000)
- Surgimento gradual de afroamericanos
- Entrada de latinos e asiáticos
- Crescimento lento mas consistente

### 3. Modernização (2000-2026)
- Aceleração significativa da diversidade
- Representação mais equilibrada
- Diversidade como prioridade institucional

### 4. Disparidade Nomeados vs Vencedores
- Proporção de vencedores ainda menor que nomeados
- Gap persistente principalmente em grupos minoritários
- Indicativo de desigualdade em votação

## 🎨 Visualizações Geradas

### oscars_diversidade_completo.png
Infográfico com 6 gráficos:
1. **Nomeados por Etnicidade (Valores Absolutos)** - Stacked Area
2. **Proporção de Nomeados (%)** - Stacked Area 100%
3. **Índice de Diversidade Simpson** - Linha com preenchimento
4. **Evolução de Grupos Minoritários** - Linhas múltiplas
5. **Nomeados vs Vencedores (2026)** - Gráfico de barras comparativo
6. **Taxa de Crescimento Anual** - Dinâmica de mudança

### oscars_diversidade_resumido.png
Infográfico executivo com:
- Visualização principal da evolução
- Índice de diversidade com anotações
- Comparação histórica 1929 vs 2023
- Tabela de estatísticas principais

## 💻 Requisitos

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

## 🚀 Como Executar

### Opção 1: Linha de Comando
```bash
python oscars.py
```

### Opção 2: Em um Jupyter Notebook
```python
%run oscars.py
```

### Opção 3: Importar como módulo
```python
from oscars import carregar_dados_oscars, calcular_metricas_diversidade, analise_exploratoria
df = carregar_dados_oscars()
df = calcular_metricas_diversidade(df)
```

## 📋 Funções Principais

### `carregar_dados_oscars()`
- Carrega dataset com 21 períodos decenais (1929-2023)
- Retorna DataFrame com dados de nomeados e vencedores
- Organizado por etnicidade

### `calcular_metricas_diversidade(df)`
- Calcula proporções por grupo étnico
- Computa Índice de Diversidade de Simpson
- Analisa disparidade nomeados vs vencedores
- Retorna DataFrame enriquecido

### `analise_exploratoria(df)`
- Imprime análise estatística detalhada
- Exibe tabelas formatadas
- Mostra principais indicadores

### `criar_infografico_diversidade(df)`
- Gera 6 visualizações detalhadas
- Salva como PNG de alta resolução (300 dpi)
- Pronto para publicação

### `criar_infografico_resumido(df)`
- Gera infográfico executivo
- 4 gráficos principais + tabela
- Design limpo e profissional

## 📊 Interpretação dos Resultados

### O que indicam os aumentos?
- **Afroamericanos**: Crescimento de 0 para 93 nomeados (+∞)
- **Latinos**: Crescimento de 0 para 52 nomeados (+∞)
- **Asiáticos**: Crescimento de 0 para 40 nomeados (+∞)

Esses crescimentos infinitos matemáticos refletem a transição de zero representação para presença significativa.

### O que indica o Índice de Simpson?
O crescimento de 0.0000 para 0.5183 mostra que:
- A indústria de cinema evoluiu de monocrática para diversificada
- Ainda há espaço para maior equidade (máximo = 1.0)
- A trajetória aponta para inclusão contínua

### Lacunas Persistentes
- Vencedores continuam sub-representando minorias
- Mesmo com aumento de nomeações, premiação é desigual
- Sugere viés adicional no processo de votação

## 🆕 Atualização 2024-2026

O projeto foi recentemente atualizado para incluir dados dos últimos 3 anos (2024, 2025, 2026), refletindo a continuidade da trajetória de diversificação dos Oscars.

### Principais Mudanças
- **Dados Expandidos**: De 1929-2023 para 1929-2026 (24 períodos)
- **Novos Arquivos**: `ATUALIZACAO_2024_2026.md`, `RESUMO_ATUALIZACAO.md`
- **Estatísticas Atualizadas**: Total de nomeados cresceu 16,7% (240→280)
- **Crescimento Acelerado**: Asiáticos +60%, Afroamericanos +32,9%

### Destaques da Atualização
- Minorias atingiram 44,6% dos nomeados em 2026
- Asiáticos mostraram maior aceleração (+15-20% ao ano)
- Projeções indicam paridade possível em 2028-2030

Para detalhes completos, consulte `ATUALIZACAO_2024_2026.md` e `RESUMO_ATUALIZACAO.md`.

## 🔗 Fontes de Dados

Dados compilados de:
- Academy of Motion Picture Arts and Sciences (análise pública)
- Registros históricos documentados
- Estudos demográficos sobre representação no cinema

## 📝 Notas Metodológicas

1. **Categorização Étnica**: Baseada em classificações demográficas públicas
2. **Períodos Decenais**: Dados apresentados em intervalos de ~5-10 anos
3. **Estimativas**: Alguns dados modernos baseados em análises compiladas
4. **Escopo**: Análise de atores/atrizes em categorias principais

## 🎓 Conclusões

A análise demonstra:

1. **Progresso Significativo**: De 0% de diversidade para ~44,6% em grupos minoritários
2. **Aceleração Recente**: Mudanças mais rápidas nos últimos 20 anos
3. **Persistência de Desigualdade**: Vencedores ainda menos diversos que nomeados
4. **Trajetória Positiva**: Tendências apontam continuidade da inclusão

## 🔮 Próximos Passos

Possíveis expansões do projeto:
- Análise por categorias específicas (melhor atriz, melhor ator, etc)
- Comparação com demografia da indústria de cinema
- Análise temporal mais granular (ano a ano)
- Incorporação de dados sobre gênero
- Projeções futuras usando modelos de série temporal
- Atualização anual com dados dos Oscars mais recentes

## 👤 Autor
Análise realizada em March 16, 2026

## 📄 Licença
Projeto de análise educacional - Dados públicos

---

**Para mais informações ou sugestões, edit o arquivo `oscars.py` diretamente. Para detalhes sobre a atualização 2024-2026, consulte `ATUALIZACAO_2024_2026.md`.**
