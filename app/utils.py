import pandas as pd
import plotly.express as px
import os

# Paths to data files
DATA_FILES = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_leone_clean.csv",
    "Togo": "data/togo_clean.csv"
}

def load_data(selected_countries):
    dfs = []
    for country in selected_countries:
        path = DATA_FILES.get(country)
        if path and os.path.exists(path):
            df = pd.read_csv(path, parse_dates=['date'])
            df['country'] = country
            dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()

def plot_ghi_boxplot(df):
    if df.empty:
        return None
    fig = px.box(df, x='country', y='GHI', points='all',
                 title='Distribution of Global Horizontal Irradiance (GHI) by Country')
    return fig

def get_top_regions(df, n=10):
    if df.empty:
        return pd.DataFrame()
    top_regions = df.groupby(['country', 'region'])['GHI'].mean().reset_index()
    top_regions = top_regions.sort_values(by='GHI', ascending=False).head(n)
    return top_regions
