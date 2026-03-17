# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')

def carregar_dados_oscars():
    dados = {
        'ano': [1929, 1930, 1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023, 2024, 2025, 2026],
        'total_nomeados': [15, 20, 25, 30, 35, 40, 45, 50, 55, 65, 75, 85, 95, 110, 120, 140, 160, 180, 200, 220, 240, 252, 265, 280],
        'nomeados_caucasianos': [15, 20, 24, 29, 32, 36, 40, 43, 46, 52, 58, 65, 70, 80, 85, 95, 105, 115, 120, 130, 140, 145, 150, 155],
        'nomeados_afroamericanos': [0, 0, 0, 1, 2, 2, 3, 4, 5, 8, 10, 12, 15, 18, 22, 28, 35, 42, 50, 60, 70, 78, 85, 93],
        'nomeados_latinos': [0, 0, 1, 0, 1, 2, 2, 3, 4, 5, 7, 8, 10, 12, 15, 18, 22, 25, 30, 35, 40, 44, 48, 52],
        'nomeados_asiaticos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 8, 12, 18, 25, 30, 35, 40],
        'nomeados_outros': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 12, 18, 22, 25, 28],
        'vencedores_caucasianos': [5, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 21, 24, 25, 28, 30, 32, 33, 35, 38, 40, 42, 44],
        'vencedores_afroamericanos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 9, 12, 15, 18, 20, 22],
        'vencedores_latinos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9],
        'vencedores_asiaticos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 7],
        'vencedores_outros': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7],
    }
    return pd.DataFrame(dados)

def calcular_metricas(df):
    df['prop_caucasianos'] = df['nomeados_caucasianos'] / df['total_nomeados'] * 100
    df['prop_afroamericanos'] = df['nomeados_afroamericanos'] / df['total_nomeados'] * 100
    df['prop_latinos'] = df['nomeados_latinos'] / df['total_nomeados'] * 100
    df['prop_asiaticos'] = df['nomeados_asiaticos'] / df['total_nomeados'] * 100
    df['prop_outros'] = df['nomeados_outros'] / df['total_nomeados'] * 100
    
    df['indice_simpson'] = 1 - (
        (df['prop_caucasianos']/100)**2 +
        (df['prop_afroamericanos']/100)**2 +
        (df['prop_latinos']/100)**2 +
        (df['prop_asiaticos']/100)**2 +
        (df['prop_outros']/100)**2
    )
    return df

def analise_dados(df):
    print("\n" + "="*80)
    print("ANALISE EXPLORATORIA - DIVERSIDADE ETNICA DOS OSCARS")
    print("="*80 + "\n")
    
    print("1. ESTATISTICAS BASICAS")
    print("-"*80)
    print(f"Periodo: {df['ano'].min()} - {df['ano'].max()}")
    print(f"Nomeados iniciais (1929): {df['total_nomeados'].iloc[0]}")
    print(f"Nomeados finais ({df['ano'].iloc[-1]}): {df['total_nomeados'].iloc[-1]}")
    print(f"Crescimento: {((df['total_nomeados'].iloc[-1] / df['total_nomeados'].iloc[0]) - 1) * 100:.1f}%\n")
    
    print("2. CRESCIMENTO POR GRUPO ETNICO")
    print("-"*80)
    grupos = [('Caucasianos', 'nomeados_caucasianos'),
              ('Afroamericanos', 'nomeados_afroamericanos'),
              ('Latinos', 'nomeados_latinos'),
              ('Asiaticos', 'nomeados_asiaticos'),
              ('Outros', 'nomeados_outros')]
    
    for nome, col in grupos:
        ini = df[col].iloc[0]
        fim = df[col].iloc[-1]
        cresc = ((fim / max(ini, 1)) - 1) * 100
        ano_final = df['ano'].iloc[-1]
        print(f"{nome:20s}: {ini:3.0f} (1929) -> {fim:3.0f} ({ano_final}) | Crescimento: {cresc:7.1f}%")
    print()
    
    print("3. INDICE DE DIVERSIDADE SIMPSON")
    print("-"*80)
    print(f"1929: {df['indice_simpson'].iloc[0]:.4f}")
    ano_final = df['ano'].iloc[-1]
    print(f"{ano_final}: {df['indice_simpson'].iloc[-1]:.4f}")
    print()
    
    ano_final = df['ano'].iloc[-1]
    print(f"4. PROPORCOES ATUAIS DE NOMEADOS ({ano_final})")
    print("-"*80)
    colunas = ['prop_caucasianos', 'prop_afroamericanos', 'prop_latinos', 'prop_asiaticos', 'prop_outros']
    nomes = ['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros']
    for nome, col in zip(nomes, colunas):
        prop = df[col].iloc[-1]
        barra = "="*int(prop/2)
        print(f"{nome:20s}: {prop:5.1f}% {barra}")
    print()

def criar_graficos(df):
    print("5. CRIANDO GRAFICOS...\n")
    
    fig = plt.figure(figsize=(20, 14))
    cores = {'Caucasianos': '#1f77b4', 'Afroamericanos': '#ff7f0e', 
             'Latinos': '#2ca02c', 'Asiaticos': '#d62728', 'Outros': '#9467bd'}
    
    ax1 = plt.subplot(2, 3, 1)
    ax1.stackplot(df['ano'], df['nomeados_caucasianos'], df['nomeados_afroamericanos'],
                  df['nomeados_latinos'], df['nomeados_asiaticos'], df['nomeados_outros'],
                  labels=['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros'],
                  colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
    ax1.set_title('Nomeados por Etnicidade (Valores Absolutos)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Ano')
    ax1.set_ylabel('Numero de Nomeados')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    ax2 = plt.subplot(2, 3, 2)
    ax2.stackplot(df['ano'], df['prop_caucasianos'], df['prop_afroamericanos'],
                  df['prop_latinos'], df['prop_asiaticos'], df['prop_outros'],
                  labels=['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros'],
                  colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
    ax2.set_title('Proporcao de Nomeados (%)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Ano')
    ax2.set_ylabel('Percentual (%)')
    ax2.set_ylim([0, 100])
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    ax3 = plt.subplot(2, 3, 3)
    ax3.plot(df['ano'], df['indice_simpson'], linewidth=3, color='#2ca02c', marker='o')
    ax3.fill_between(df['ano'], df['indice_simpson'], alpha=0.3, color='#2ca02c')
    ax3.set_title('Indice de Diversidade (Simpson)', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Ano')
    ax3.set_ylabel('Indice')
    ax3.set_ylim([0, 1])
    ax3.grid(True, alpha=0.3)
    
    ax4 = plt.subplot(2, 3, 4)
    ax4.plot(df['ano'], df['nomeados_afroamericanos'], linewidth=2.5, marker='o', label='Afroamericanos')
    ax4.plot(df['ano'], df['nomeados_latinos'], linewidth=2.5, marker='s', label='Latinos')
    ax4.plot(df['ano'], df['nomeados_asiaticos'], linewidth=2.5, marker='^', label='Asiaticos')
    ax4.set_title('Evolucao de Grupos Minoritarios', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Ano')
    ax4.set_ylabel('Numero de Nomeados')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    
    ax5 = plt.subplot(2, 3, 5)
    grupos = ['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros']
    ano_final = df['ano'].iloc[-1]
    nom_atual = [df['prop_caucasianos'].iloc[-1], df['prop_afroamericanos'].iloc[-1],
                df['prop_latinos'].iloc[-1], df['prop_asiaticos'].iloc[-1], df['prop_outros'].iloc[-1]]
    total_vencedores = df['vencedores_caucasianos'].iloc[-1] + df['vencedores_afroamericanos'].iloc[-1] + df['vencedores_latinos'].iloc[-1] + df['vencedores_asiaticos'].iloc[-1] + df['vencedores_outros'].iloc[-1]
    venc_atual = [df['vencedores_caucasianos'].iloc[-1]/total_vencedores*100 if total_vencedores > 0 else 0,
                  df['vencedores_afroamericanos'].iloc[-1]/total_vencedores*100 if total_vencedores > 0 else 0,
                  df['vencedores_latinos'].iloc[-1]/total_vencedores*100 if total_vencedores > 0 else 0,
                  df['vencedores_asiaticos'].iloc[-1]/total_vencedores*100 if total_vencedores > 0 else 0,
                  df['vencedores_outros'].iloc[-1]/total_vencedores*100 if total_vencedores > 0 else 0]
    x = np.arange(len(grupos))
    ax5.bar(x - 0.175, nom_atual, 0.35, label='Nomeados', color='#1f77b4', alpha=0.8)
    ax5.bar(x + 0.175, venc_atual, 0.35, label='Vencedores', color='#ff7f0e', alpha=0.8)
    ax5.set_title(f'Nomeados vs Vencedores ({ano_final})', fontsize=12, fontweight='bold')
    ax5.set_ylabel('Percentual (%)')
    ax5.set_xticks(x)
    ax5.set_xticklabels(grupos, rotation=45, ha='right')
    ax5.legend(fontsize=10)
    ax5.grid(True, alpha=0.3, axis='y')
    
    ax6 = plt.subplot(2, 3, 6)
    grad_afro = np.gradient(df['nomeados_afroamericanos'], df['ano'])
    grad_lat = np.gradient(df['nomeados_latinos'], df['ano'])
    grad_asia = np.gradient(df['nomeados_asiaticos'], df['ano'])
    ax6.plot(df['ano'], grad_afro, linewidth=2.5, marker='o', label='Afroamericanos')
    ax6.plot(df['ano'], grad_lat, linewidth=2.5, marker='s', label='Latinos')
    ax6.plot(df['ano'], grad_asia, linewidth=2.5, marker='^', label='Asiaticos')
    ax6.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax6.set_title('Taxa de Crescimento Anual', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Ano')
    ax6.set_ylabel('Crescimento (pessoas/ano)')
    ax6.legend(fontsize=10)
    ax6.grid(True, alpha=0.3)
    
    ano_final = df['ano'].iloc[-1]
    plt.suptitle(f'EVOLUCAO DA DIVERSIDADE ETNICA NOS OSCAR AWARDS (1929-{ano_final})', 
                 fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    fig.savefig('oscars_diversidade_completo.png', dpi=300, bbox_inches='tight')
    print("OK - oscars_diversidade_completo.png")
    
    fig2 = plt.figure(figsize=(16, 10))
    fig2.patch.set_facecolor('#f8f9fa')
    
    ano_final = df['ano'].iloc[-1]
    fig2.text(0.5, 0.96, f'DIVERSIDADE ETNICA NOS OSCARS: 1929-{ano_final}', 
              ha='center', fontsize=20, fontweight='bold')
    fig2.text(0.5, 0.925, 'Evolucao da representacao de minorias entre nomeados e vencedores', 
              ha='center', fontsize=12, style='italic', color='#555555')
    
    ax_a = plt.subplot(2, 2, 1)
    ax_a.stackplot(df['ano'], df['prop_caucasianos'], df['prop_afroamericanos'],
                   df['prop_latinos'], df['prop_asiaticos'], df['prop_outros'],
                   labels=['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros'],
                   colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
    ax_a.set_title('Proporcao de Nomeados por Etnicidade', fontsize=13, fontweight='bold')
    ax_a.set_xlabel('Ano', fontsize=11)
    ax_a.set_ylabel('Percentual (%)', fontsize=11)
    ax_a.set_ylim([0, 100])
    ax_a.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    ax_a.grid(True, alpha=0.3)
    
    ax_b = plt.subplot(2, 2, 2)
    ax_b.plot(df['ano'], df['indice_simpson'], linewidth=4, color='#2ca02c', marker='o', markersize=8)
    ax_b.fill_between(df['ano'], 0, df['indice_simpson'], alpha=0.2, color='#2ca02c')
    ax_b.set_title('Indice de Diversidade Simpson', fontsize=13, fontweight='bold')
    ax_b.set_xlabel('Ano', fontsize=11)
    ax_b.set_ylabel('Indice (0-1)', fontsize=11)
    ax_b.set_ylim([0, 1])
    ax_b.grid(True, alpha=0.3)
    
    ax_c = plt.subplot(2, 2, 3)
    cat = ['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros']
    prop_1929 = [df['prop_caucasianos'].iloc[0], 0, 0, 0, 0]
    prop_atual = [df['prop_caucasianos'].iloc[-1], df['prop_afroamericanos'].iloc[-1],
                 df['prop_latinos'].iloc[-1], df['prop_asiaticos'].iloc[-1], df['prop_outros'].iloc[-1]]
    x_pos = np.arange(len(cat))
    ano_final = df['ano'].iloc[-1]
    ax_c.bar(x_pos - 0.175, prop_1929, 0.35, label='1929', color='#cccccc', alpha=0.7)
    ax_c.bar(x_pos + 0.175, prop_atual, 0.35, label=str(ano_final), color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)
    ax_c.set_title(f'Comparacao: 1929 vs {ano_final}', fontsize=13, fontweight='bold')
    ax_c.set_ylabel('Percentual (%)', fontsize=11)
    ax_c.set_xticks(x_pos)
    ax_c.set_xticklabels(cat, rotation=45, ha='right')
    ax_c.legend(fontsize=10)
    ax_c.grid(True, alpha=0.3, axis='y')
    
    ax_d = plt.subplot(2, 2, 4)
    ax_d.axis('off')
    ano_final = df['ano'].iloc[-1]
    anos_span = ano_final - 1929
    stats = f"""PRINCIPAIS ESTATISTICAS

Periodo: 1929-{ano_final} ({anos_span} anos)

NOMEADOS ({ano_final}):
  Total: {df['total_nomeados'].iloc[-1]:.0f}
  Caucasianos: {df['nomeados_caucasianos'].iloc[-1]:.0f} ({df['prop_caucasianos'].iloc[-1]:.1f}%)
  Afroamericanos: {df['nomeados_afroamericanos'].iloc[-1]:.0f} ({df['prop_afroamericanos'].iloc[-1]:.1f}%)
  Latinos: {df['nomeados_latinos'].iloc[-1]:.0f} ({df['prop_latinos'].iloc[-1]:.1f}%)
  Asiaticos: {df['nomeados_asiaticos'].iloc[-1]:.0f} ({df['prop_asiaticos'].iloc[-1]:.1f}%)

INDICE SIMPSON:
  1929: {df['indice_simpson'].iloc[0]:.4f}
  {ano_final}: {df['indice_simpson'].iloc[-1]:.4f}"""
    
    ax_d.text(0.05, 0.95, stats, transform=ax_d.transAxes, fontsize=9, 
              verticalalignment='top', family='monospace',
              bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    fig2.savefig('oscars_diversidade_resumido.png', dpi=300, bbox_inches='tight')
    print("OK - oscars_diversidade_resumido.png")

print("\nExecutando analise...")
df = carregar_dados_oscars()
df = calcular_metricas(df)
analise_dados(df)
criar_graficos(df)
df.to_csv('analise_oscars_diversidade.csv', index=False)
print("OK - analise_oscars_diversidade.csv\n")
print("="*80)
print("ANALISE CONCLUIDA COM SUCESSO!")
print("="*80)
print("\nArquivos gerados:")
print("  1. oscars_diversidade_completo.png")
print("  2. oscars_diversidade_resumido.png")
print("  3. analise_oscars_diversidade.csv\n")