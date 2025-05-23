import streamlit as st
import pandas as pd
import base64

def render_data_export(tourism_data, art_forms_data, funding_data, monthly_data, heritage_data):
    """Render the data export section"""
    st.header("📊 Data Export")
    
    st.info(
        "Download the datasets used in this dashboard for your own analysis and research. "
        "All datasets are available in CSV format."
    )
    
    # Create tabs for different datasets
    export_tab1, export_tab2, export_tab3, export_tab4, export_tab5 = st.tabs([
        "Tourism Data", 
        "Art Forms Data", 
        "Funding Data", 
        "Monthly Tourism Data",
        "Heritage Sites Data"
    ])
    
    with export_tab1:
        st.subheader("Tourism Data")
        st.dataframe(tourism_data)
        
        csv = tourism_data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="tourism_data.csv" class="download-button">Download Tourism Data</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    with export_tab2:
        st.subheader("Art Forms Data")
        st.dataframe(art_forms_data)
        
        csv = art_forms_data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="art_forms_data.csv" class="download-button">Download Art Forms Data</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    with export_tab3:
        st.subheader("Funding Data")
        st.dataframe(funding_data)
        
        csv = funding_data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="funding_data.csv" class="download-button">Download Funding Data</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    with export_tab4:
        st.subheader("Monthly Tourism Data")
        st.dataframe(monthly_data)
        
        csv = monthly_data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="monthly_tourism_data.csv" class="download-button">Download Monthly Tourism Data</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    with export_tab5:
        st.subheader("Heritage Sites Data")
        st.dataframe(heritage_data)
        
        csv = heritage_data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="heritage_sites_data.csv" class="download-button">Download Heritage Sites Data</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    # Combined dataset
    st.subheader("Combined Dataset")
    
    # Create combined dataset description
    st.markdown(
        """
        The combined dataset includes merged information from all the individual datasets, 
        creating a comprehensive view of India's cultural tourism landscape. This consolidated 
        dataset is ideal for in-depth analysis and correlation studies.
        """
    )
    
    # Sample of combined data
    st.dataframe(pd.merge(
        tourism_data,
        pd.merge(
            art_forms_data.groupby('state')['art_form'].count().reset_index().rename(columns={'art_form': 'art_forms_count'}),
            pd.merge(
                funding_data.groupby('state')['funding_amount'].sum().reset_index(),
                heritage_data.groupby('STATE').size().reset_index().rename(columns={0: 'heritage_sites_count', 'STATE': 'state'}),
                on='state',
                how='outer'
            ),
            on='state',
            how='outer'
        ),
        on='state',
        how='outer'
    ).head(10))
    
    # Create combined dataset
    combined_data = pd.merge(
        tourism_data,
        pd.merge(
            art_forms_data.groupby('state')['art_form'].count().reset_index().rename(columns={'art_form': 'art_forms_count'}),
            pd.merge(
                funding_data.groupby('state')['funding_amount'].sum().reset_index(),
                heritage_data.groupby('STATE').size().reset_index().rename(columns={0: 'heritage_sites_count', 'STATE': 'state'}),
                on='state',
                how='outer'
            ),
            on='state',
            how='outer'
        ),
        on='state',
        how='outer'
    )
    
    csv = combined_data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="combined_tourism_culture_data.csv" class="download-button">Download Combined Dataset</a>'
    st.markdown(href, unsafe_allow_html=True)
    
    # Data citation and terms
    st.markdown("---")
    st.subheader("Data Citation & Terms of Use")
    
    st.markdown(
        """
        When using this data in your research or applications, please cite as:
        
        > India Art, Culture & Tourism Dashboard (2025). Cultural Tourism Dataset, Ministry of Tourism and Ministry of Culture, Government of India.
        
        **Terms of Use:**
        
        This data is provided for informational and research purposes. While effort has been made to ensure accuracy, the creators of this dashboard make no representations or warranties regarding the completeness or accuracy of the data.
        """
    )