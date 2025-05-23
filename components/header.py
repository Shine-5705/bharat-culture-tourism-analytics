import streamlit as st
import pandas as pd

def render_header(tourism_data, heritage_data):
    """Render the header section with key metrics"""
    st.title("🏮 Art, Culture & Tourism in India")
    
    # Calculate key metrics
    total_tourists = tourism_data['visitors'].sum()
    total_states = tourism_data['state'].nunique()
    total_art_forms = 75  # Predefined value
    total_funding = 5  # In crores, predefined value
    total_heritage_sites = len(heritage_data)
    
    # Create metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Total Tourist Visits",
            value=f"{total_tourists:,}",
            delta=f"{round((total_tourists / 40000000 - 1) * 100, 1)}% from last year"
        )
    
    with col2:
        st.metric(
            label="States & UTs",
            value=f"{total_states}"
        )
        
    with col3:
        st.metric(
            label="Art Forms",
            value=f"{total_art_forms}"
        )
        
    with col4:
        st.metric(
            label="Total Funding",
            value=f"₹{total_funding} Cr"
        )
        
    with col5:
        st.metric(
            label="Heritage Sites",
            value=f"{total_heritage_sites}"
        )
    
    # Info box about the dashboard
    with st.expander("About This Dashboard"):
        st.markdown(
            """
            This dashboard provides a comprehensive view of India's cultural tourism landscape, 
            featuring data on tourist visits, popular art forms, and government funding for 
            cultural preservation.
            
            **Key Features:**
            - State-wise tourism analysis
            - Art form popularity and distribution
            - Seasonal tourism patterns
            - Correlation between tourism and cultural funding
            - Heritage sites mapping and analysis
            
            The data is synthesized from various government sources including the Ministry of 
            Tourism and the Ministry of Culture, with heritage site data from the Archaeological Survey of India.
            """
        )