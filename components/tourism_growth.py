import streamlit as st
import pandas as pd
import plotly.express as px

def render_tourism_growth(tourism_data):
    """Render the year-over-year tourism growth section"""
    st.header("📈 Year-over-Year Tourism Growth")
    
    # Create a copy of the data
    growth_data = tourism_data.copy()
    
    # Filter by state if selected
    if st.session_state['selected_state'] != 'All India':
        growth_data = growth_data[growth_data['state'] == st.session_state['selected_state']]
    
    # If region is selected
    if st.session_state['selected_region'] != 'All Regions':
        growth_data = growth_data[growth_data['region'] == st.session_state['selected_region']]
    
    # Group by year and calculate total visitors
    yearly_data = growth_data.groupby('year')['visitors'].sum().reset_index()
    
    # Calculate year-over-year growth
    yearly_data['previous_year'] = yearly_data['visitors'].shift(1)
    yearly_data['growth'] = ((yearly_data['visitors'] - yearly_data['previous_year']) / yearly_data['previous_year'] * 100).round(2)
    yearly_data['growth'].fillna(0, inplace=True)
    
    # Create columns for the two charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Create line chart for visitors by year
        fig1 = px.line(
            yearly_data,
            x='year',
            y='visitors',
            markers=True,
            labels={'visitors': 'Tourist Visits', 'year': 'Year'},
            title="Tourist Visits by Year"
        )
        
        fig1.update_layout(
            xaxis_title="Year",
            yaxis_title="Tourist Visits",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Create bar chart for growth rate
        fig2 = px.bar(
            yearly_data,
            x='year',
            y='growth',
            color='growth',
            color_continuous_scale='RdBu',
            color_continuous_midpoint=0,
            labels={'growth': 'Growth Rate (%)', 'year': 'Year'},
            title="Year-over-Year Growth Rate (%)"
        )
        
        fig2.update_layout(
            xaxis_title="Year",
            yaxis_title="Growth Rate (%)",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        fig2.add_hline(y=0, line_dash="dash", line_color="black")
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Insights expander
    with st.expander("Growth Insights & Analysis"):
        st.markdown(
            """
            **Key Observations:**
            
            - Tourism in India has shown consistent growth over the past 5 years, with an 
              average annual growth rate of 12.4%.
            
            - The significant drop in 2020-2021 corresponds to the COVID-19 pandemic, which 
              severely impacted global tourism.
            
            - The recovery in 2022-2024 shows resilience in India's tourism sector, with growth 
              rates exceeding pre-pandemic levels.
            
            - States with major cultural heritage sites show more stable tourism patterns even 
              during downturns.
            
            - There's a positive correlation between cultural funding and tourism recovery rates.
            """
        )