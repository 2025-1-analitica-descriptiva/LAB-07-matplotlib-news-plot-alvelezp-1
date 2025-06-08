"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    df = pd.read_csv('files/input/news.csv', index_col=0)
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'gray',
        'Internet': 'tab:blue',
        'Radio': 'lightgray',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }
    
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2,
    }
    
    plt.Figure()

    for col in df.columns:
        plt.plot(
            df.index, 
            df[col], 
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
        )
    
    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col]
        )

        plt.text(
            x=first_year - 0.2,
            y=df[col][first_year],
            s=f'{col} {df[col][first_year]}%',
            color=colors[col],
            fontsize=10,
            ha='right',
            va='center',
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col]
        )

        plt.text(
            x=last_year + 0.2,
            y=df[col][last_year],
            s=f'{df[col][last_year]}%',
            color=colors[col],
            fontsize=10,
            ha='left',
            va='center',
        )

    plt.tight_layout()
    os.makedirs('files/plots', exist_ok=True)
    plt.savefig('files/plots/news.png', dpi=300, bbox_inches='tight')

pregunta_01()