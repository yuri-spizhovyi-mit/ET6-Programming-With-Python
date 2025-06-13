import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Title
st.title("Canadian Housing Price Forecast Dashboard")


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(
        "C:/Users/yspizhoviy/ET6-Programming-With-Python/canadian-housing-analysis/data/processed/forecast_2023_2033.csv"
    )
    df["ds"] = pd.to_datetime(df["ds"])
    return df


df = load_data()

# Date range slider
min_year = df["ds"].dt.year.min()
max_year = df["ds"].dt.year.max()
year_range = st.slider(
    "Select forecast range:", min_year, max_year, (min_year, max_year)
)

# Filter data by selected year range
filtered_df = df[df["ds"].dt.year.between(year_range[0], year_range[1])]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.fill_between(
    filtered_df["ds"],
    filtered_df["yhat_lower"],
    filtered_df["yhat_upper"],
    color="skyblue",
    alpha=0.4,
    label="Confidence Interval",
)
ax.plot(filtered_df["ds"], filtered_df["yhat"], label="Forecast", color="blue")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_title("Forecasted Housing Prices (CAD $)")
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.grid(True)
ax.legend()
plt.tight_layout()

# Show plot in Streamlit
st.pyplot(fig)

# Show raw data toggle
if st.checkbox("Show raw forecast data"):
    st.dataframe(filtered_df[["ds", "yhat", "yhat_lower", "yhat_upper"]])
