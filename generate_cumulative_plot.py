import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    root = os.path.dirname(__file__)
    csv_path = os.path.join(root, 'analise_oscars_diversidade.csv')
    df = pd.read_csv(csv_path)

    # Filter period 1929-2026
    df = df[(df['ano'] >= 1929) & (df['ano'] <= 2026)].copy()

    # Columns for nomeados and vencedores
    nome_cols = ['nomeados_caucasianos', 'nomeados_afroamericanos', 'nomeados_latinos', 'nomeados_asiaticos', 'nomeados_outros']
    venc_cols = ['vencedores_caucasianos', 'vencedores_afroamericanos', 'vencedores_latinos', 'vencedores_asiaticos', 'vencedores_outros']

    sum_nome = df[nome_cols].sum()
    sum_venc = df[venc_cols].sum()

    total_nome = sum_nome.sum()
    total_venc = sum_venc.sum()

    labels = ['Caucasianos', 'Afroamericanos', 'Latinos', 'Asiaticos', 'Outros']
    nomes_pct = [(sum_nome[col] / total_nome) * 100 if total_nome > 0 else 0 for col in nome_cols]
    venc_pct = [(sum_venc[col] / total_venc) * 100 if total_venc > 0 else 0 for col in venc_cols]

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, nomes_pct, width, label='Nomeados (%)', color='#1f77b4')
    ax.bar(x + width/2, venc_pct, width, label='Vencedores (%)', color='#ff7f0e')

    ax.set_ylabel('Percentual (%)')
    ax.set_title('Nomeados vs Vencedores (Acumulado 1929-2026)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    out_path = os.path.join(root, 'image.png')
    plt.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f'OK - imagem acumulada salva em: {out_path}')


if __name__ == '__main__':
    main()
