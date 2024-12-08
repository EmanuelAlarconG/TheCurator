import plotly.graph_objects as go
import plotly.express as px
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

def plot_avg_duration_by_genre(avg_durations):

    sorted_durations = sorted(avg_durations.items(), key=lambda x: x[1], reverse=True)
    genres = [item[0] for item in sorted_durations]
    durations = [item[1] for item in sorted_durations]

    fig = px.bar(
        x=genres,
        y=durations,
        labels={
            "x": "Género",
            "y": "Duración Pomedio (min)"
        },
        title="Duración Promedio por Género",
        color_discrete_sequence=["#BADD13"],
        template=theme
    )
    fig.update_xaxes(tickangle=45)
    fig.show()

def plot_release_year_distribution(year_counts):
    
    sorted_years = sorted(year_counts.items(), key=lambda x: x[0])
    years = [item[0] for item in sorted_years]
    counts = [item[1] for item in sorted_years]

    fig = px.bar(
        x=years,
        y=counts,
        labels={
            "x": "Año",
            "y": "Número de canciones"
        },
        title="Distribución de años de lanzamiento",
        color_discrete_sequence=["#BADD13"],
        template=theme
    )
    fig.show()

def plot_top_artists(artist_counts):

    artists = list(artist_counts.keys())
    counts = list(artist_counts.values())

    fig = px.bar(
        x=artists,
        y=counts,
        labels={
            "x": "Artista",
            "y": "Número de Canciones"
        },
        title="Artistas más Frecuentes en la Playlist",
        color_discrete_sequence=["#BADD13"],
        template=theme
    )
    fig.update_xaxes(tickangle=45)
    fig.show()