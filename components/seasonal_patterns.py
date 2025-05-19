import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render_seasonal_patterns(monthly_data, regional_data):
    """Render the seasonal tourism patterns section"""
    st.header("🌦️ Seasonal Tourism Patterns")
    
    # Create columns for the two charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Tourism Across Regions")
        
        # Group by region and month, calculate average visitors
        region_monthly = monthly_data.groupby(['region', 'month'])['visitors'].mean().reset_index()
        
        # Create line chart for each region
        fig1 = px.line(
            region_monthly,
            x='month',
            y='visitors',
            color='region',
            markers=True,
            line_shape='spline',
            labels={'visitors': 'Average Tourist Visits', 'month': 'Month', 'region': 'Region'},
            title="Monthly Tourism Patterns by Region"
        )
        
        fig1.update_layout(
            xaxis_title="Month",
            yaxis_title="Average Tourist Visits",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20),
            legend_title="Region"
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Peak Tourism Months by Region")
        
        # Get the month with maximum visitors for each region
        peak_months = region_monthly.loc[region_monthly.groupby('region')['visitors'].idxmax()]
        
        # Create bar chart
        fig2 = px.bar(
            peak_months,
            x='region',
            y='visitors',
            color='month',
            text='month',
            labels={'visitors': 'Peak Tourist Visits', 'region': 'Region', 'month': 'Peak Month'},
            title="Peak Tourism Months by Region"
        )
        
        fig2.update_layout(
            xaxis_title="Region",
            yaxis_title="Peak Tourist Visits",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20),
            legend_title="Month"
        )
        
        fig2.update_traces(textposition='inside')
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Seasonal factors heatmap
    st.subheader("Seasonal Factors Impact on Tourism")
    
    # Create a heatmap showing how different factors affect tourism in different seasons
    seasons = ['Winter (Dec-Feb)', 'Spring (Mar-May)', 'Summer (Jun-Aug)', 'Autumn (Sep-Nov)']
    factors = ['Weather Comfort', 'Cultural Festivals', 'Holiday Season', 'Accessibility', 'Accommodation Rates']
    
    # Sample impact scores (0-10)
    impact_scores = [
        [9, 7, 4, 8],  # Weather Comfort
        [8, 6, 5, 9],  # Cultural Festivals
        [7, 5, 8, 6],  # Holiday Season
        [6, 8, 7, 8],  # Accessibility
        [5, 7, 9, 6]   # Accommodation Rates
    ]
    
    # Create heatmap
    fig3 = go.Figure(data=go.Heatmap(
        z=impact_scores,
        x=seasons,
        y=factors,
        colorscale='Viridis',
        hoverongaps=False,
        text=impact_scores,
        texttemplate="%{text}",
        colorbar=dict(title="Impact Score")
    ))
    
    fig3.update_layout(
        title="Impact of Seasonal Factors on Tourism (0-10 scale)",
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Seasonal recommendations
    with st.expander("Seasonal Tourism Recommendations"):
        st.markdown(
            """
            ### Recommendations for Seasonal Tourism
            
            Based on the seasonal patterns observed, here are some recommendations for tourists:
            
            **Winter (December-February):**
            - Ideal for visiting Southern and Western India (Kerala, Goa, Gujarat)
            - Perfect for cultural festivals like Pongal, Lohri, and Desert Festival
            - Avoid extreme northern areas unless interested in snow activities
            
            **Spring (March-May):**
            - Great for visiting Eastern and Northeastern states (Odisha, Assam, Meghalaya)
            - Ideal for witnessing spring festivals like Holi and Baisakhi
            - Avoid extremely hot destinations in Central India
            
            **Summer (June-August):**
            - Perfect time for Northern hill stations (Himachal Pradesh, Uttarakhand)
            - Monsoon tourism in Western Ghats and Kerala
            - Cultural experiences in Northeast during local festivals
            
            **Autumn (September-November):**
            - Ideal for visiting North and Central India (Rajasthan, Madhya Pradesh)
            - Perfect for cultural festivals like Diwali, Durga Puja, and Navratri
            - Great weather for heritage site visits across the country
            """
        )