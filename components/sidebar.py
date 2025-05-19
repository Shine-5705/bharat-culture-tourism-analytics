import streamlit as st
from data.loader import get_states_list, get_regions_list, get_years_list

def render_sidebar():
    """Render the sidebar filters"""
    st.sidebar.image("assets/logo.png", width=200)
    
    st.sidebar.title("📌 Filters")
    
    # State filter
    states = get_states_list()
    selected_state = st.sidebar.selectbox(
        "Select State/UT",
        options=["All India"] + states,
        index=0,
        key="sidebar_state"
    )
    st.session_state['selected_state'] = selected_state
    
    # Year filter
    years = get_years_list()
    selected_year = st.sidebar.selectbox(
        "Select Year",
        options=years,
        index=years.index(2024) if 2024 in years else 0,
        key="sidebar_year"
    )
    st.session_state['selected_year'] = selected_year
    
    # Region filter
    regions = get_regions_list()
    selected_region = st.sidebar.selectbox(
        "Select Region",
        options=["All Regions"] + regions,
        index=0,
        key="sidebar_region"
    )
    st.session_state['selected_region'] = selected_region
    
    # About section
    st.sidebar.markdown("---")
    st.sidebar.title("ℹ️ About")
    st.sidebar.info(
        "This dashboard visualizes India's art, culture, and tourism data "
        "to promote responsible tourism and cultural preservation. "
        "Explore the rich diversity of India's artistic heritage and "
        "discover cultural experiences across the country."
    )
    
    # Resource links
    st.sidebar.title("🔗 Resources")
    st.sidebar.markdown(
        """
        - [Ministry of Tourism](https://tourism.gov.in/)
        - [Ministry of Culture](https://www.indiaculture.gov.in/)
        - [Archaeological Survey of India](https://asi.nic.in/)
        - [Incredible India](https://www.incredibleindia.org/)
        """
    )