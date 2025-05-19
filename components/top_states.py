import streamlit as st
import pandas as pd
import plotly.express as px

def render_top_states(tourism_data):
    """Render the top 10 tourist states visualization"""
    st.header("🏆 Top 10 Tourist States")
    
    # Create a copy of the data for visualization
    top_states_data = tourism_data.copy()
    
    # Filter by year if selected
    if st.session_state['selected_year'] != 'All Years':
        top_states_data = top_states_data[top_states_data['year'] == st.session_state['selected_year']]
    
    # Group by state and sum visitors
    top_states_data = top_states_data.groupby('state')['visitors'].sum().reset_index()
    
    # Get top 10 states
    top_states_data = top_states_data.sort_values('visitors', ascending=False).head(10)
    
    # Create bar chart
    fig = px.bar(
        top_states_data,
        x='visitors',
        y='state',
        orientation='h',
        color='visitors',
        color_continuous_scale='Oranges',
        labels={'visitors': 'Tourist Visits', 'state': 'State/UT'},
        text='visitors'
    )
    
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title="Number of Tourist Visits",
        yaxis_title="State/UT",
        height=400,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    
    fig.update_traces(
        texttemplate='%{text:,}',
        textposition='outside'
    )
    
    st.plotly_chart(fig, use_container_width=True)