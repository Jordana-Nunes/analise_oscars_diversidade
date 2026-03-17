import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    root = os.path.dirname(__file__)
    csv_path = os.path.join(root, 'analise_oscars_diversidade.csv')
    df = pd.read_csv(csv_path)

    # Ensure 'ano' is int and set index for interpolation
    df['ano'] = df['ano'].astype(int)
    df = df.set_index('ano')

    target_year = 2019
    if target_year not in df.index:
        # Reindex to include target year and interpolate numerics
        new_index = sorted(list(df.index) + [target_year])
        df = df.reindex(new_index)
        df = df.interpolate(method='index')

    row = df.loc[target_year]

    # Compute percentual de nomeados (por grupo)
    grupos = [
        ('Caucasianos', 'nomeados_caucasianos', 'vencedores_caucasianos'),
        ('Afroamericanos', 'nomeados_afroamericanos', 'vencedores_afroamericanos'),
        ('Latinos', 'nomeados_latinos', 'vencedores_latinos'),
        ('Asiaticos', 'nomeados_asiaticos', 'vencedores_asiaticos'),
        ('Outros', 'nomeados_outros', 'vencedores_outros'),
    ]

    total_nomeados = row['total_nomeados']
    total_vencedores = (
        row['vencedores_caucasianos'] + row['vencedores_afroamericanos'] +
        row['vencedores_latinos'] + row['vencedores_asiaticos'] + row['vencedores_outros']
    )

    nomes_pct = []
    venc_pct = []
    labels = []
    for label, col_nom, col_venc in grupos:
        labels.append(label)
        nomes_pct.append((row[col_nom] / total_nomeados) * 100 if total_nomeados > 0 else 0)
        venc_pct.append((row[col_venc] / total_vencedores) * 100 if total_vencedores > 0 else 0)

    # Plot
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, nomes_pct, width, label='Nomeados (%)', color='#1f77b4')
    ax.bar(x + width/2, venc_pct, width, label='Vencedores (%)', color='#ff7f0e')

    ax.set_ylabel('Percentual (%)')
    ax.set_title(f'Nomeados vs Vencedores ({target_year})', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    out_path = os.path.join(root, 'image.png')
    plt.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f'OK - imagem salva em: {out_path}')


if __name__ == '__main__':
    main()
