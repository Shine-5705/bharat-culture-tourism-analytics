import streamlit as st
import pandas as pd
import snowflake.connector


import streamlit as st
import pandas as pd
import snowflake.connector
import altair as alt

# Streamlit UI
st.title("🕌 Discover India's Cultural Heritage")
st.set_page_config(page_title="India's Cultural Heritage", layout="wide")


# Connect to Snowflake
conn = snowflake.connector.connect(
    user='yugamwadhwa',
    password='Snowflakeproject1',
    account='QO59102',  # e.g. abcde-xy12345
    warehouse='COMPUTE_WH',
    database='CULTURE_TOURISM_DB',
    schema='PUBLIC'
)

# Fetch data
@st.cache_data
# @st.cache_resource
def load_data():
    query = "SELECT * FROM HERITAGE_SITES"
    return pd.read_sql(query, conn)

df = load_data()
# st.dataframe(df)

# --- FILTERS ---
st.sidebar.header("🔍 Filter Sites")
states = st.sidebar.multiselect("Select State(s):", options=df['STATE'].unique())
zones = st.sidebar.multiselect("Select Zone(s):", options=df['ZONE_NAME'].unique())

filtered_df = df.copy()

if states:
    filtered_df = filtered_df[filtered_df['STATE'].isin(states)]

if zones:
    filtered_df = filtered_df[filtered_df['ZONE_NAME'].isin(zones)]

# --- METRICS ---
st.markdown("### 📊 Summary")
st.write(f"Total heritage sites in view: **{len(filtered_df)}**")
