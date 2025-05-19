import streamlit as st
from components.sidebar import render_sidebar
from components.header import render_header
from components.tourism_map import render_tourism_map
from components.top_states import render_top_states
from components.state_analysis import render_state_analysis
from components.tourism_growth import render_tourism_growth
from components.art_showcase import render_art_showcase
from components.seasonal_patterns import render_seasonal_patterns
from components.advanced_analytics import render_advanced_analytics
from components.data_export import render_data_export
from data.loader import load_all_data

# Page configuration
st.set_page_config(
    page_title="India Art, Culture & Tourism Dashboard",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load all data
tourism_data, art_forms_data, funding_data, monthly_data, regional_data = load_all_data()

# Create session state for filters if it doesn't exist
if 'selected_state' not in st.session_state:
    st.session_state['selected_state'] = 'All India'
if 'selected_year' not in st.session_state:
    st.session_state['selected_year'] = 2024
if 'selected_region' not in st.session_state:
    st.session_state['selected_region'] = 'All Regions'

# Render sidebar with filters
render_sidebar()

# Header section
render_header(tourism_data)

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🗺️ Tourism Overview", 
    "🎭 Art & Culture", 
    "🌦️ Seasonal Patterns", 
    "🔍 Advanced Analytics",
    "📊 Data Export"
])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        render_tourism_map(tourism_data)
    
    with col2:
        render_top_states(tourism_data)
    
    render_state_analysis(tourism_data, art_forms_data, funding_data, monthly_data)
    render_tourism_growth(tourism_data)

with tab2:
    render_art_showcase(art_forms_data, funding_data)

with tab3:
    render_seasonal_patterns(monthly_data, regional_data)

with tab4:
    render_advanced_analytics(tourism_data, funding_data, monthly_data)

with tab5:
    render_data_export(tourism_data, art_forms_data, funding_data, monthly_data)

# Footer
st.markdown("---")
st.markdown(
    "<div class='footer'>© 2025 India Art, Culture & Tourism Dashboard | Data sourced from Ministry of Tourism and Ministry of Culture</div>", 
    unsafe_allow_html=True
)