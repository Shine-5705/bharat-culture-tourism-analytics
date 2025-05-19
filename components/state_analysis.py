import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def render_state_analysis(tourism_data, art_forms_data, funding_data, monthly_data):
    """Render the state-wise cultural tourism analysis section"""
    st.header("🏞️ State-wise Cultural Tourism Analysis")
    
    # State selector
    selected_state = st.selectbox(
        "Select a state to explore its art forms and funding",
        options=tourism_data['state'].unique(),
        index=0,
        key="state_analysis_selector"
    )
    
    # Filter data for the selected state
    state_tourism = tourism_data[tourism_data['state'] == selected_state]
    state_art_forms = art_forms_data[art_forms_data['state'] == selected_state]
    state_funding = funding_data[funding_data['state'] == selected_state]
    state_monthly = monthly_data[monthly_data['state'] == selected_state]
    
    # Create two columns for the visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"Monthly Tourism Trends in {selected_state} (2024)")
        
        # Monthly trends for the selected state
        fig1 = px.line(
            state_monthly,
            x='month',
            y='visitors',
            markers=True,
            line_shape='spline',
            labels={'visitors': 'Tourist Visits', 'month': 'Month'},
            title=f"Monthly Tourism in {selected_state}"
        )
        
        fig1.update_layout(
            xaxis_title="Month",
            yaxis_title="Tourist Visits",
            height=350,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Get the region of the selected state
        state_region = tourism_data[tourism_data['state'] == selected_state]['region'].iloc[0]
        
        # Filter states in the same region
        region_states = tourism_data[tourism_data['region'] == state_region]['state'].unique()
        region_data = tourism_data[tourism_data['state'].isin(region_states)]
        
        # Group by state and sum visitors
        region_data = region_data.groupby('state')['visitors'].sum().reset_index()
        
        st.subheader(f"Comparing {selected_state} with Other States in {state_region} Region")
        
        # Create comparison chart
        fig2 = px.bar(
            region_data,
            x='state',
            y='visitors',
            color='visitors',
            color_continuous_scale='Blues',
            labels={'visitors': 'Tourist Visits', 'state': 'State/UT'},
            title=f"Tourism Comparison in {state_region} Region"
        )
        
        fig2.update_layout(
            xaxis_title="State/UT",
            yaxis_title="Tourist Visits",
            height=350,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        fig2.add_shape(
            type="rect",
            x0=region_data[region_data['state'] == selected_state].index[0] - 0.4,
            x1=region_data[region_data['state'] == selected_state].index[0] + 0.4,
            y0=0,
            y1=region_data[region_data['state'] == selected_state]['visitors'].iloc[0],
            line=dict(color="red", width=2),
            fillcolor="rgba(0,0,0,0)"
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Art forms in the selected state
    st.subheader(f"Art Forms in {selected_state}")
    
    if not state_art_forms.empty:
        # Display art forms in a grid
        art_cols = st.columns(3)
        
        for i, (_, art) in enumerate(state_art_forms.iterrows()):
            with art_cols[i % 3]:
                st.markdown(
                    f"""
                    <div class="art-card">
                        <h3>{art['art_form']}</h3>
                        <p><strong>Type:</strong> {art['type']}</p>
                        <p><strong>Popularity:</strong> {art['popularity']}/10</p>
                        <p>{art['description']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.info(f"No specific art forms data available for {selected_state}")