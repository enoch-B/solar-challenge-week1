import streamlit as st
from app.utils import load_data, plot_ghi_boxplot, get_top_regions

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("🌞 Solar Data Interactive Dashboard")

# Sidebar for country selection
countries = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries)

if not selected_countries:
    st.warning("Please select at least one country to view data.")
    st.stop()

# Load data
df = load_data(selected_countries)

if df.empty:
    st.warning("No data available for selected countries.")
    st.stop()

# Interactive Boxplot of GHI
st.subheader("GHI Distribution by Country")
fig = plot_ghi_boxplot(df)
if fig:
    st.plotly_chart(fig, use_container_width=True)

# Display Top Regions Table
st.subheader("Top Regions by Average GHI")
top_regions = get_top_regions(df)
st.table(top_regions)

# Additional interactive widgets can be added here
