import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

def render_tourism_map(tourism_data):
    """Render the tourism map of India"""
    st.header("🗺️ Tourism Map of India")
    
    # Create a copy of the data for visualization
    map_data = tourism_data.copy()
    
    # Filter data based on session state
    if st.session_state['selected_state'] != 'All India':
        map_data = map_data[map_data['state'] == st.session_state['selected_state']]
    
    if st.session_state['selected_year'] != 'All Years':
        map_data = map_data[map_data['year'] == st.session_state['selected_year']]
    
    # Create a map with Plotly
    fig = px.choropleth(
        map_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='visitors',
        color_continuous_scale='Reds',
        range_color=(0, map_data['visitors'].max()),
        hover_data=['state', 'visitors', 'growth_rate'],
        labels={
            'visitors': 'Tourist Visits',
            'state': 'State/UT',
            'growth_rate': 'Growth Rate (%)'
        },
        title='Tourist Visits by State/UT'
    )
    
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )
    
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Tourist Visits",
            thicknessmode="pixels", thickness=20,
            lenmode="pixels", len=300
        ),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Additional map info
    with st.expander("Map Insights"):
        st.markdown(
            """
            This map visualizes tourist visits across India's states and union territories.
            
            **Key Observations:**
            - Northern and Western states generally attract more tourists
            - Coastal states show higher international tourism
            - States with UNESCO heritage sites have higher visitor counts
            - Growth rates vary significantly across regions
            """
        )