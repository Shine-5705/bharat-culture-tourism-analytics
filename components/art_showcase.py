import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def render_art_showcase(art_forms_data, funding_data):
    """Render the art and culture showcase section"""
    st.header("🎭 Art and Culture Showcase")
    
    # Create columns for the two charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Most Popular Art Forms in India")
        
        # Get the top 10 art forms by popularity
        top_art_forms = art_forms_data.sort_values('popularity', ascending=False).head(10)
        
        # Create horizontal bar chart
        fig1 = px.bar(
            top_art_forms,
            y='art_form',
            x='popularity',
            orientation='h',
            color='type',
            labels={'popularity': 'Popularity Score', 'art_form': 'Art Form', 'type': 'Art Type'},
            title="Most Popular Art Forms in India",
            hover_data=['description', 'state']
        )
        
        fig1.update_layout(
            yaxis={'categoryorder': 'total ascending'},
            xaxis_title="Popularity Score (out of 10)",
            yaxis_title="Art Form",
            height=500,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Funding Distribution by Art Form")
        
        # Group by art form and sum funding
        funding_by_art = funding_data.groupby('art_form')['funding_amount'].sum().reset_index()
        
        # Sort by funding amount
        funding_by_art = funding_by_art.sort_values('funding_amount', ascending=False)
        
        # Create pie chart
        fig2 = px.pie(
            funding_by_art,
            values='funding_amount',
            names='art_form',
            title="Distribution of Cultural Funding",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig2.update_traces(
            textposition='inside',
            textinfo='percent+label'
        )
        
        fig2.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Art forms by region
    st.subheader("Art Forms Distribution by Region")
    
    # Join art forms with tourism data to get region
    art_with_region = pd.merge(
        art_forms_data,
        funding_data[['state', 'region']].drop_duplicates(),
        on='state'
    )
    
    # Group by region and type, count art forms
    art_by_region = art_with_region.groupby(['region', 'type']).size().reset_index(name='count')
    
    # Create grouped bar chart
    fig3 = px.bar(
        art_by_region,
        x='region',
        y='count',
        color='type',
        barmode='group',
        labels={'count': 'Number of Art Forms', 'region': 'Region', 'type': 'Art Type'},
        title="Art Forms by Region and Type"
    )
    
    fig3.update_layout(
        xaxis_title="Region",
        yaxis_title="Number of Art Forms",
        legend_title="Art Type",
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Cultural preservation initiatives
    with st.expander("Cultural Preservation Initiatives"):
        st.markdown(
            """
            ### Major Cultural Preservation Initiatives in India
            
            The Government of India, through the Ministry of Culture, has implemented several initiatives to preserve and promote traditional art forms:
            
            1. **National Mission on Cultural Mapping**: Documenting and preserving India's diverse cultural heritage.
            
            2. **Scheme for Safeguarding the Intangible Cultural Heritage**: Identifying and protecting intangible cultural expressions.
            
            3. **Cultural Function and Production Grant**: Financial support for cultural events and productions.
            
            4. **Scheme for Promotion of Culture of Science**: Bridging traditional knowledge with modern science.
            
            5. **Zonal Cultural Centres**: Promoting regional cultural forms and creating platforms for artists.
            
            These initiatives aim to document, preserve, and promote India's rich cultural heritage while ensuring the continuity of traditional art forms.
            """
        )