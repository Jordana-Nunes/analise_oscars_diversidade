import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def make_plot_for_year(df, year, out_name):
    if year not in df['ano'].values:
        temp = df.set_index('ano')
        new_index = sorted(list(temp.index) + [year])
        temp = temp.reindex(new_index).interpolate(method='index')
        row = temp.loc[year]
    else:
        row = df[df['ano'] == year].iloc[0]

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

    labels = []
    nomes_pct = []
    venc_pct = []
    for label, col_nom, col_venc in grupos:
        labels.append(label)
        nomes_pct.append((row[col_nom] / total_nomeados) * 100 if total_nomeados > 0 else 0)
        venc_pct.append((row[col_venc] / total_vencedores) * 100 if total_vencedores > 0 else 0)

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, nomes_pct, width, label='Nomeados (%)', color='#1f77b4')
    ax.bar(x + width/2, venc_pct, width, label='Vencedores (%)', color='#ff7f0e')

    ax.set_ylabel('Percentual (%)')
    ax.set_title(f'Nomeados vs Vencedores ({year})', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    fig.savefig(out_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'OK - {out_name}')


def main():
    root = os.path.dirname(__file__)
    csv_path = os.path.join(root, 'analise_oscars_diversidade.csv')
    df = pd.read_csv(csv_path)

    out = os.path.join(root, 'image1977.png')
    make_plot_for_year(df, 1977, out)


if __name__ == '__main__':
    main()
