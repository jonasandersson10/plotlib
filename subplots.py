from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_subplots(df, rows, cols):
    fig = make_subplots(rows=rows, cols=cols)
    r = c = 0
    for i in range(df.shape[1]):
        if (r % 6) == 0 and r > 0:
            c += 1
            r = 0

        fig.add_traces(go.Histogram(x=df[df.columns[i]]), rows=r + 1, cols=c + 1)
        r += 1
    fig.show()
    return fig
