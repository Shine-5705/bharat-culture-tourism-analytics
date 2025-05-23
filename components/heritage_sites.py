import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def render_heritage_sites(heritage_data):
    """Render the heritage sites section"""
    st.header("🏛️ Heritage Sites of India")
    
    # Filter controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_zone = st.selectbox(
            "Select Zone",
            options=["All Zones"] + sorted(heritage_data["ZONE_NAME"].unique().tolist())
        )
    
    with col2:
        selected_nature = st.selectbox(
            "Heritage Type",
            options=["All Types"] + sorted(heritage_data["NATURE_OF_HERITAGE"].unique().tolist())
        )
    
    with col3:
        selected_use = st.selectbox(
            "Heritage Use",
            options=["All Uses"] + sorted(heritage_data["HERITAGE_USE"].unique().tolist())
        )
    
    # Filter data based on selections
    filtered_data = heritage_data.copy()
    if selected_zone != "All Zones":
        filtered_data = filtered_data[filtered_data["ZONE_NAME"] == selected_zone]
    if selected_nature != "All Types":
        filtered_data = filtered_data[filtered_data["NATURE_OF_HERITAGE"] == selected_nature]
    if selected_use != "All Uses":
        filtered_data = filtered_data[filtered_data["HERITAGE_USE"] == selected_use]
    
    # Create two columns for visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Heritage sites by state
        st.subheader("Heritage Sites by State")
        state_counts = filtered_data["STATE"].value_counts().reset_index()
        state_counts.columns = ["State", "Count"]
        
        fig1 = px.bar(
            state_counts,
            x="State",
            y="Count",
            color="Count",
            color_continuous_scale="Viridis",
            labels={"Count": "Number of Heritage Sites"},
            title="Distribution of Heritage Sites Across States"
        )
        
        fig1.update_layout(
            xaxis_tickangle=-45,
            height=400,
            margin=dict(l=20, r=20, t=50, b=100)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Heritage types distribution
        st.subheader("Types of Heritage Sites")
        type_counts = filtered_data["NATURE_OF_HERITAGE"].value_counts()
        
        fig2 = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Distribution by Heritage Type",
            hole=0.4
        )
        
        fig2.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Heritage sites table
    st.subheader("Heritage Sites Details")
    
    # Add search functionality
    search_term = st.text_input("Search Heritage Sites", "")
    
    if search_term:
        search_results = filtered_data[
            filtered_data["NAME_OF_HERITAGE"].str.contains(search_term, case=False) |
            filtered_data["CITY_NAME"].str.contains(search_term, case=False) |
            filtered_data["STATE"].str.contains(search_term, case=False)
        ]
    else:
        search_results = filtered_data
    
    # Display results in an interactive table
    st.dataframe(
        search_results[[
            "NAME_OF_HERITAGE", "CITY_NAME", "STATE", "NATURE_OF_HERITAGE",
            "HERITAGE_USE", "AGE_OF_HERITAGE"
        ]],
        hide_index=True,
        use_container_width=True
    )
    
    # Heritage age analysis
    st.subheader("Heritage Age Analysis")
    
    # Create age categories
    age_bins = [0, 100, 200, 500, 1000, float('inf')]
    age_labels = ['0-100 years', '101-200 years', '201-500 years', '501-1000 years', '1000+ years']
    
    filtered_data['age_category'] = pd.cut(
        pd.to_numeric(filtered_data['AGE_OF_HERITAGE'], errors='coerce'),
        bins=age_bins,
        labels=age_labels
    )
    
    age_dist = filtered_data['age_category'].value_counts().sort_index()
    
    fig3 = px.bar(
        x=age_dist.index,
        y=age_dist.values,
        labels={'x': 'Age Category', 'y': 'Number of Sites'},
        title="Age Distribution of Heritage Sites",
        color=age_dist.values,
        color_continuous_scale="Viridis"
    )
    
    fig3.update_layout(
        xaxis_tickangle=-45,
        height=400,
        margin=dict(l=20, r=20, t=50, b=100)
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Additional insights
    with st.expander("Heritage Sites Insights"):
        st.markdown(
            """
            ### Key Insights from Heritage Sites Data
            
            1. **Geographic Distribution**
               - Analyze the concentration of heritage sites across different zones
               - Identify states with the richest heritage presence
            
            2. **Heritage Types**
               - Understanding the diversity of heritage sites
               - Distribution of different types of heritage across regions
            
            3. **Age and Preservation**
               - Analysis of heritage site ages
               - Correlation between age and current use
            
            4. **Current Usage**
               - How heritage sites are being utilized today
               - Balance between preservation and practical use
            
            These insights help in:
            - Cultural preservation planning
            - Tourism development strategies
            - Resource allocation for heritage maintenance
            - Educational and cultural awareness programs
            """
        )