import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mental Health Analytics",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------------------------------------
# SIMPLE STYLING
# ---------------------------------------------------------
st.markdown("""
<style>
.block-container {padding-top: 1.5rem;}
.metric-box {
    background: #f4f7fb;
    padding: 16px;
    border-radius: 10px;
    border-left: 4px solid #6366f1;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
st.title("🧠 Mental Health Analytics Dashboard")
st.caption("Global prevalence, population coverage, depressive symptoms and data availability")

# ---------------------------------------------------------
# LOAD DATASETS
# Put the four CSV files next to dashboard.py OR upload them.
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "Prevalence": "1- mental-illnesses-prevalence.csv",
    "Population coverage": "4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv",
    "Depressive symptoms": "6- depressive-symptoms-across-us-population.csv",
    "Country data availability": "7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv"
}

def load_dataset(label, filename):
    uploaded = st.sidebar.file_uploader(
        f"Upload {label} CSV",
        type="csv",
        key=label
    )
    if uploaded is not None:
        return pd.read_csv(uploaded)

    for candidate in [
        os.path.join(BASE_DIR, filename),
        os.path.join(BASE_DIR, "archive", filename)
    ]:
        if os.path.exists(candidate):
            return pd.read_csv(candidate)
    return None

st.sidebar.header("📂 Datasets")
df1 = load_dataset("Prevalence", FILES["Prevalence"])
df2 = load_dataset("Population coverage", FILES["Population coverage"])
df3 = load_dataset("Depressive symptoms", FILES["Depressive symptoms"])
df4 = load_dataset("Country data availability", FILES["Country data availability"])

if df1 is None:
    st.info("Upload the **Prevalence CSV** in the sidebar to begin. Other datasets are optional.")
    st.stop()

# ---------------------------------------------------------
# PREPARE PREVALENCE DATA
# ---------------------------------------------------------
df1.columns = df1.columns.str.strip()

rename_map = {
    "Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized": "Schizophrenia",
    "Depressive disorders (share of population) - Sex: Both - Age: Age-standardized": "Depressive disorders",
    "Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized": "Anxiety disorders",
    "Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized": "Bipolar disorders",
    "Eating disorders (share of population) - Sex: Both - Age: Age-standardized": "Eating disorders"
}
df1 = df1.rename(columns=rename_map)

disorder_cols = [
    "Schizophrenia", "Depressive disorders", "Anxiety disorders",
    "Bipolar disorders", "Eating disorders"
]
disorder_cols = [c for c in disorder_cols if c in df1.columns]

# ---------------------------------------------------------
# FILTERS
# ---------------------------------------------------------
st.sidebar.header("🔎 Filters")

if "Year" in df1.columns:
    years = sorted(pd.to_numeric(df1["Year"], errors="coerce").dropna().unique())
    selected_year = st.sidebar.selectbox("Year", years, index=len(years)-1 if years else 0)
    df_filtered = df1[pd.to_numeric(df1["Year"], errors="coerce") == selected_year]
else:
    selected_year = None
    df_filtered = df1.copy()

if "Entity" in df_filtered.columns:
    entities = sorted(df_filtered["Entity"].dropna().astype(str).unique())
    selected_entities = st.sidebar.multiselect("Countries / Regions", entities, default=entities)
    df_filtered = df_filtered[df_filtered["Entity"].astype(str).isin(selected_entities)]

# ---------------------------------------------------------
# KPI ROW
# ---------------------------------------------------------
st.subheader("📊 Overview")
a, b, c, d = st.columns(4)
a.metric("Records", f"{len(df_filtered):,}")
b.metric("Countries / Regions", df_filtered["Entity"].nunique() if "Entity" in df_filtered else "—")
c.metric("Year selected", selected_year if selected_year is not None else "All")
d.metric("Disorders available", len(disorder_cols))

st.divider()

# ---------------------------------------------------------
# PREVALENCE CHARTS
# ---------------------------------------------------------
st.subheader("📈 Mental Disorder Prevalence")

if disorder_cols and "Entity" in df_filtered.columns:
    chart_df = df_filtered[["Entity"] + disorder_cols].copy()
    chart_df[disorder_cols] = chart_df[disorder_cols].apply(pd.to_numeric, errors="coerce")
    chart_df = chart_df.melt(
        id_vars="Entity", value_vars=disorder_cols,
        var_name="Disorder", value_name="Prevalence"
    ).dropna()

    left, right = st.columns(2)
    with left:
        fig = px.bar(
            chart_df.sort_values("Prevalence", ascending=False).head(20),
            x="Prevalence", y="Entity", color="Disorder",
            orientation="h", title="Highest prevalence values (top 20 records)"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

    with right:
        mean_df = chart_df.groupby("Disorder", as_index=False)["Prevalence"].mean()
        fig2 = px.bar(
            mean_df, x="Disorder", y="Prevalence", color="Disorder",
            title="Average prevalence by disorder"
        )
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, width="stretch")

    if "Year" in df1.columns:
        trend = df1.copy()
        trend["Year"] = pd.to_numeric(trend["Year"], errors="coerce")
        for col in disorder_cols:
            trend[col] = pd.to_numeric(trend[col], errors="coerce")
        trend = trend.groupby("Year", as_index=False)[disorder_cols].mean()
        trend_long = trend.melt(
            id_vars="Year", value_vars=disorder_cols,
            var_name="Disorder", value_name="Prevalence"
        ).dropna()
        fig3 = px.line(
            trend_long, x="Year", y="Prevalence", color="Disorder",
            markers=True, title="Global average prevalence trend"
        )
        st.plotly_chart(fig3, width="stretch")
else:
    st.warning("Could not find expected prevalence columns in the uploaded file.")

# ---------------------------------------------------------
# POPULATION COVERAGE
# ---------------------------------------------------------
if df2 is not None:
    st.divider()
    st.subheader("🌍 Adult Population Coverage")
    df2.columns = df2.columns.str.strip()
    coverage_cols = [c for c in df2.columns if c not in ["Entity", "Code", "Year"]]
    numeric_col = st.selectbox("Coverage indicator", coverage_cols, key="coverage_col")
    temp = df2.copy()
    temp[numeric_col] = pd.to_numeric(temp[numeric_col].astype(str).str.replace("<", ""), errors="coerce")
    top = temp.sort_values(numeric_col, ascending=False).head(15)
    fig4 = px.bar(top, x=numeric_col, y="Entity", orientation="h",
                   title=f"Top 15: {numeric_col}")
    fig4.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig4, width="stretch")

# ---------------------------------------------------------
# DEPRESSIVE SYMPTOMS
# ---------------------------------------------------------
if df3 is not None:
    st.divider()
    st.subheader("🇺🇸 Depressive Symptoms Across US Population")
    df3.columns = df3.columns.str.strip()
    symptom_cols = [c for c in df3.columns if c not in ["Entity", "Code", "Year"]]
    symptom_cols = [c for c in symptom_cols if pd.api.types.is_numeric_dtype(df3[c])]
    if symptom_cols:
        symptom = st.selectbox("Symptom frequency", symptom_cols)
        fig5 = px.line(df3, x="Year" if "Year" in df3 else df3.index,
                       y=symptom, markers=True, title=f"Trend: {symptom}")
        st.plotly_chart(fig5, width="stretch")
    else:
        st.dataframe(df3.head(10), width="stretch")

# ---------------------------------------------------------
# DATA AVAILABILITY
# ---------------------------------------------------------
if df4 is not None:
    st.divider()
    st.subheader("🗺️ Countries with Prevalence Data")
    df4.columns = df4.columns.str.strip()
    candidates = [c for c in df4.columns if c not in ["Entity", "Code", "Year"]]
    if candidates:
        availability_col = candidates[0]
        df4[availability_col] = pd.to_numeric(df4[availability_col], errors="coerce")
        fig6 = px.line(df4, x="Year" if "Year" in df4 else df4.index,
                       y=availability_col, markers=True,
                       title="Countries with primary prevalence data over time")
        st.plotly_chart(fig6, width="stretch")

# ---------------------------------------------------------
# TABLE + DOWNLOAD
# ---------------------------------------------------------
st.divider()
st.subheader("📋 Prevalence Dataset Preview")
st.dataframe(df_filtered.head(100), width="stretch")

st.download_button(
    "⬇️ Download filtered prevalence data",
    data=df_filtered.to_csv(index=False).encode("utf-8"),
    file_name="filtered_mental_health_prevalence.csv",
    mime="text/csv"
)

st.caption("Mental Health Analytics | Python • Pandas • Streamlit • Plotly")
