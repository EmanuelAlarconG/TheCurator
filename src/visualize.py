import plotly.graph_objects as go
from plotly.io import templates

templates["plotly_dark"]["layout"]["colorway"] = ["#BADD13"]
theme = "plotly_dark"

def plot_genre_distribution(genre_counts):

    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    genres = [genre for genre, _ in sorted_genres]
    counts = [count for _, count in sorted_genres]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=genres,
        y=counts,
        marker_color="#BADD13"
    ))

    fig.update_layout(
        template=theme,
        title="Distribución de géneros en la playlist",
        xaxis_title="Género",
        yaxis_title="Número de canciones",
        xaxis_tickangle=45,
        font=dict(size=12),
    )

    fig.show()