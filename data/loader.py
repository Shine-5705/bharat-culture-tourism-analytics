import pandas as pd
import numpy as np
import os
import snowflake.connector

def get_heritage_sites_data():
    """Get heritage sites data from Snowflake"""
    try:
        conn = snowflake.connector.connect(
            user='YUGAMWADHWA',
            password='Snowflakeproject1',
            account='avoweut-wp22365',
            warehouse='COMPUTE_WH',
            database='CULTURE_TOURISM_DB',
            schema='PUBLIC'
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM HERITAGE_SITES")
        
        # Fetch column names
        columns = [desc[0] for desc in cursor.description]
        
        # Fetch all data
        data = cursor.fetchall()
        
        # Create DataFrame
        heritage_df = pd.DataFrame(data, columns=columns)
        
        cursor.close()
        conn.close()
        
        return heritage_df
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        # Return empty DataFrame if connection fails
        return pd.DataFrame(columns=[
            'CITY_NAME', 'STATE', 'COUNTRY', 'ZONE_NAME', 
            'NAME_OF_HERITAGE', 'NATURE_OF_HERITAGE', 
            'HERITAGE_USE', 'AGE_OF_HERITAGE'
        ])

def generate_tourism_data():
    """Generate synthetic tourism data for India states"""
    # List of states and union territories
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir'
    ]
    
    # List of regions
    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    
    # Map states to regions
    state_regions = {
        'Jammu and Kashmir': 'North', 'Himachal Pradesh': 'North', 'Punjab': 'North',
        'Uttarakhand': 'North', 'Haryana': 'North', 'Delhi': 'North',
        'Rajasthan': 'North', 'Uttar Pradesh': 'North',
        
        'Kerala': 'South', 'Tamil Nadu': 'South', 'Karnataka': 'South',
        'Andhra Pradesh': 'South', 'Telangana': 'South',
        
        'West Bengal': 'East', 'Bihar': 'East', 'Odisha': 'East', 'Jharkhand': 'East',
        
        'Gujarat': 'West', 'Maharashtra': 'West', 'Goa': 'West',
        
        'Madhya Pradesh': 'Central', 'Chhattisgarh': 'Central',
        
        'Sikkim': 'Northeast', 'Arunachal Pradesh': 'Northeast', 'Assam': 'Northeast',
        'Meghalaya': 'Northeast', 'Manipur': 'Northeast', 'Mizoram': 'Northeast',
        'Nagaland': 'Northeast', 'Tripura': 'Northeast'
    }
    
    # Years
    years = [2020, 2021, 2022, 2023, 2024]
    
    # Create empty list to store data
    data = []
    
    # Generate tourism data for each state and year
    for state in states:
        base_visitors = np.random.randint(100000, 5000000)  # Base number of visitors
        for year in years:
            # Apply a growth factor based on year (COVID impact in 2020-2021)
            if year == 2020:
                growth_factor = 0.6  # 40% reduction due to COVID
            elif year == 2021:
                growth_factor = 0.8  # 20% reduction as recovery starts
            elif year == 2022:
                growth_factor = 1.1  # 10% growth as tourism recovers
            elif year == 2023:
                growth_factor = 1.2  # 20% growth
            else:  # 2024
                growth_factor = 1.3  # 30% growth
            
            # Adjust base visitors with some randomness
            visitors = int(base_visitors * growth_factor * np.random.uniform(0.9, 1.1))
            growth_rate = np.random.uniform(-5, 15)  # Growth rate percentage
            
            # Get the region for the state
            region = state_regions.get(state, 'Unknown')
            
            # Add to data list
            data.append({
                'state': state,
                'region': region,
                'year': year,
                'visitors': visitors,
                'growth_rate': growth_rate
            })
    
    # Create DataFrame
    tourism_df = pd.DataFrame(data)
    
    return tourism_df

def generate_art_forms_data():
    """Generate synthetic art forms data for India"""
    # List of art forms with their details
    art_forms_data = [
        # Classical Dance Forms
        ('Bharatanatyam', 'Dance', 'Tamil Nadu', 9.2, 'Ancient classical dance from Tamil Nadu, known for its grace and sculptural poses'),
        ('Kathakali', 'Dance', 'Kerala', 8.8, 'Traditional dance-drama known for elaborate costumes and facial expressions'),
        ('Odissi', 'Dance', 'Odisha', 8.9, 'One of the oldest surviving dance forms of India'),
        ('Kathak', 'Dance', 'Uttar Pradesh', 9.0, 'Classical dance form that tells stories through rhythmic foot movements'),
        ('Manipuri', 'Dance', 'Manipur', 8.5, 'Classical dance from Manipur characterized by gentle and graceful movements'),
        
        # Music Traditions
        ('Carnatic', 'Music', 'Tamil Nadu', 9.0, 'Classical music tradition of South India'),
        ('Hindustani', 'Music', 'Uttar Pradesh', 9.1, 'Classical music tradition of North India'),
        ('Dhrupad', 'Music', 'Bihar', 8.7, 'Ancient classical music form of North India'),
        ('Qawwali', 'Music', 'Delhi', 8.6, 'Devotional music of the Sufis'),
        
        # Visual Arts
        ('Madhubani', 'Painting', 'Bihar', 8.5, 'Folk art from the Mithila region using natural dyes'),
        ('Tanjore', 'Painting', 'Tamil Nadu', 8.6, 'Classical South Indian painting style using gold foil'),
        ('Warli', 'Painting', 'Maharashtra', 8.4, 'Tribal art form using basic geometric shapes'),
        ('Gond', 'Painting', 'Madhya Pradesh', 8.3, 'Traditional art of the Gond tribe'),
        ('Kalamkari', 'Painting', 'Andhra Pradesh', 8.7, 'Hand-painted or block-printed cotton textile'),
        
        # Performing Arts
        ('Yakshagana', 'Theatre', 'Karnataka', 8.2, 'Traditional theatre form combining dance, music, and dialogue'),
        ('Chhau', 'Dance', 'West Bengal', 8.4, 'Semi-classical dance with martial art movements'),
        ('Koodiyattam', 'Theatre', 'Kerala', 8.1, 'Sanskrit theatre tradition'),
        ('Nautanki', 'Theatre', 'Uttar Pradesh', 7.9, 'Folk theatre performance'),
        
        # Crafts
        ('Bidri', 'Craft', 'Karnataka', 8.3, 'Metal handicraft with silver inlay work'),
        ('Pashmina', 'Craft', 'Jammu and Kashmir', 8.8, 'Fine cashmere wool textile'),
        ('Zardozi', 'Craft', 'Uttar Pradesh', 8.5, 'Metallic thread embroidery'),
        ('Phulkari', 'Craft', 'Punjab', 8.4, 'Traditional embroidery technique'),
        
        # Additional art forms for more states
        ('Bamboo Craft', 'Craft', 'Assam', 8.0, 'Traditional bamboo crafting'),
        ('Thangka', 'Painting', 'Sikkim', 8.2, 'Buddhist scroll painting'),
        ('Dokra', 'Craft', 'Chhattisgarh', 8.1, 'Non-ferrous metal casting using lost-wax technique'),
        ('Pattachitra', 'Painting', 'Odisha', 8.6, 'Traditional cloth-based scroll painting'),
        ('Puppetry', 'Theatre', 'Rajasthan', 7.8, 'Traditional string puppet theatre'),
        ('Roghan', 'Painting', 'Gujarat', 8.2, 'Traditional cloth painting using castor oil paste'),
        ('Tholu Bommalata', 'Theatre', 'Andhra Pradesh', 7.9, 'Traditional leather puppet theatre')
    ]
    
    # Create DataFrame
    df = pd.DataFrame(art_forms_data, columns=['art_form', 'type', 'state', 'popularity', 'description'])
    
    return df

def generate_funding_data():
    """Generate synthetic funding data for cultural preservation"""
    # List of states
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir'
    ]
    
    # Regions
    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    
    # Map states to regions
    state_regions = {
        'Jammu and Kashmir': 'North', 'Himachal Pradesh': 'North', 'Punjab': 'North',
        'Uttarakhand': 'North', 'Haryana': 'North', 'Delhi': 'North',
        'Rajasthan': 'North', 'Uttar Pradesh': 'North',
        
        'Kerala': 'South', 'Tamil Nadu': 'South', 'Karnataka': 'South',
        'Andhra Pradesh': 'South', 'Telangana': 'South',
        
        'West Bengal': 'East', 'Bihar': 'East', 'Odisha': 'East', 'Jharkhand': 'East',
        
        'Gujarat': 'West', 'Maharashtra': 'West', 'Goa': 'West',
        
        'Madhya Pradesh': 'Central', 'Chhattisgarh': 'Central',
        
        'Sikkim': 'Northeast', 'Arunachal Pradesh': 'Northeast', 'Assam': 'Northeast',
        'Meghalaya': 'Northeast', 'Manipur': 'Northeast', 'Mizoram': 'Northeast',
        'Nagaland': 'Northeast', 'Tripura': 'Northeast'
    }
    
    # Art forms by type
    art_types = {
        'Dance': ['Bharatanatyam', 'Kathakali', 'Kathak', 'Odissi', 'Manipuri', 'Kuchipudi', 'Sattriya', 'Chhau', 'Ghoomar', 'Bhangra', 'Lavani'],
        'Painting': ['Madhubani', 'Warli', 'Gond', 'Phad', 'Pattachitra', 'Tanjore', 'Thangka'],
        'Textile Art': ['Kalamkari', 'Bandhani', 'Pashmina', 'Rogan'],
        'Embroidery': ['Chikankari', 'Phulkari', 'Kantha', 'Zardozi'],
        'Metalwork': ['Meenakari', 'Bidri', 'Dokra', 'Bell Metal Craft'],
        'Pottery': ['Blue Pottery', 'Terracotta', 'Khavda Pottery', 'Black Pottery'],
        'Theater': ['Yakshagana', 'Nautanki', 'Jatra', 'Ramleela'],
        'Music': ['Hindustani', 'Carnatic', 'Folk Music', 'Tribal Music'],
        'Sculpture': ['Stone Carving', 'Wood Carving', 'Bronze Casting', 'Clay Modeling']
    }
    
    # Create empty list to store data
    data = []
    
    # Generate funding data for each state
    for state in states:
        # Get the region for the state
        region = state_regions.get(state, 'Unknown')
        
        # Number of funding entries for this state (between 2-5)
        num_entries = np.random.randint(2, 6)
        
        # Select random art types and forms for this state
        selected_types = np.random.choice(list(art_types.keys()), size=num_entries, replace=False)
        
        for art_type in selected_types:
            # Select a random art form of this type
            if art_types[art_type]:
                art_form = np.random.choice(art_types[art_type])
            else:
                art_form = f"{state} {art_type}"
            
            # Generate funding amount (in lakhs)
            funding_amount = np.random.randint(20, 200)
            
            # Generate year
            year = np.random.choice([2020, 2021, 2022, 2023, 2024])
            
            # Add to data list
            data.append({
                'state': state,
                'region': region,
                'art_form': art_form,
                'art_type': art_type,
                'funding_amount': funding_amount,
                'year': year
            })
    
    # Create DataFrame
    funding_df = pd.DataFrame(data)
    
    return funding_df

def generate_monthly_data():
    """Generate monthly tourism data for each state"""
    # List of states
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir'
    ]
    
    # Regions
    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    
    # Map states to regions
    state_regions = {
        'Jammu and Kashmir': 'North', 'Himachal Pradesh': 'North', 'Punjab': 'North',
        'Uttarakhand': 'North', 'Haryana': 'North', 'Delhi': 'North',
        'Rajasthan': 'North', 'Uttar Pradesh': 'North',
        
        'Kerala': 'South', 'Tamil Nadu': 'South', 'Karnataka': 'South',
        'Andhra Pradesh': 'South', 'Telangana': 'South',
        
        'West Bengal': 'East', 'Bihar': 'East', 'Odisha': 'East', 'Jharkhand': 'East',
        
        'Gujarat': 'West', 'Maharashtra': 'West', 'Goa': 'West',
        
        'Madhya Pradesh': 'Central', 'Chhattisgarh': 'Central',
        
        'Sikkim': 'Northeast', 'Arunachal Pradesh': 'Northeast', 'Assam': 'Northeast',
        'Meghalaya': 'Northeast', 'Manipur': 'Northeast', 'Mizoram': 'Northeast',
        'Nagaland': 'Northeast', 'Tripura': 'Northeast'
    }
    
    # Months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Years
    years = [2023, 2024]
    
    # Create empty list to store data
    data = []
    
    # Regional seasonality patterns (peak month indexes)
    regional_peaks = {
        'North': [11, 0, 1, 2, 3],  # Winter (Nov-Mar)
        'South': [10, 11, 0, 6, 7],  # Winter & Monsoon
        'East': [9, 10, 11, 0],  # Autumn & Winter
        'West': [10, 11, 0, 1],  # Winter
        'Central': [9, 10, 1, 2],  # Winter & Spring
        'Northeast': [3, 4, 9, 10]  # Spring & Autumn
    }
    
    # Generate monthly data for each state
    for state in states:
        # Get region
        region = state_regions.get(state, 'Unknown')
        
        # Base monthly visitors (used as a reference)
        base_monthly = np.random.randint(10000, 300000)
        
        for year in years:
            for i, month in enumerate(months):
                # Apply seasonal pattern based on region
                peak_months = regional_peaks.get(region, [])
                
                if i in peak_months:
                    # Peak month - higher visitors
                    seasonal_factor = np.random.uniform(1.3, 1.8)
                elif (i + 1) % 12 in peak_months or (i - 1) % 12 in peak_months:
                    # Shoulder month - medium visitors
                    seasonal_factor = np.random.uniform(1.0, 1.3)
                else:
                    # Off-peak month - lower visitors
                    seasonal_factor = np.random.uniform(0.5, 0.9)
                
                # Apply year factor (growth from 2023 to 2024)
                year_factor = 1.0 if year == 2023 else 1.15
                
                # Calculate visitors with some randomness
                visitors = int(base_monthly * seasonal_factor * year_factor * np.random.uniform(0.9, 1.1))
                
                # Add to data list
                data.append({
                    'state': state,
                    'region': region,
                    'year': year,
                    'month': month,
                    'month_num': i + 1,
                    'visitors': visitors
                })
    
    # Create DataFrame
    monthly_df = pd.DataFrame(data)
    
    return monthly_df

def generate_regional_data():
    """Generate regional tourism data with seasonal patterns"""
    # Regions
    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    
    # Months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Create empty list to store data
    data = []
    
    # Regional seasonal patterns (coefficients for each month)
    seasonal_patterns = {
        'North': [0.9, 0.85, 0.7, 0.6, 0.5, 0.7, 0.8, 0.7, 0.8, 0.9, 1.0, 1.0],
        'South': [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0],
        'East': [0.8, 0.7, 0.65, 0.7, 0.75, 0.7, 0.65, 0.6, 0.7, 0.9, 1.0, 0.9],
        'West': [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0],
        'Central': [0.9, 0.95, 0.9, 0.8, 0.6, 0.5, 0.4, 0.5, 0.7, 0.9, 1.0, 0.95],
        'Northeast': [0.7, 0.75, 0.9, 1.0, 0.95, 0.8, 0.7, 0.6, 0.8, 0.9, 0.8, 0.7]
    }
    
    # Generate data for each region
    for region in regions:
        # Base visitors for the region
        base_visitors = np.random.randint(500000, 2000000)
        
        for i, month in enumerate(months):
            # Apply seasonal pattern
            pattern = seasonal_patterns.get(region, [1.0] * 12)
            seasonal_factor = pattern[i]
            
            # Calculate visitors with some randomness
            visitors = int(base_visitors * seasonal_factor * np.random.uniform(0.95, 1.05))
            
            # Add to data list
            data.append({
                'region': region,
                'month': month,
                'month_num': i + 1,
                'visitors': visitors,
                'season_index': seasonal_factor
            })
    
    # Create DataFrame
    regional_df = pd.DataFrame(data)
    
    return regional_df

def get_states_list():
    """Return a list of all states"""
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir'
    ]
    return states

def get_regions_list():
    """Return a list of all regions"""
    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    return regions

def get_years_list():
    """Return a list of all years"""
    years = [2020, 2021, 2022, 2023, 2024]
    return years

def save_data_to_csv():
    """Generate and save all datasets to CSV files"""
    # Create data directory if it doesn't exist
    os.makedirs('data/csv', exist_ok=True)
    
    # Generate datasets
    tourism_data = generate_tourism_data()
    art_forms_data = generate_art_forms_data()
    funding_data = generate_funding_data()
    monthly_data = generate_monthly_data()
    regional_data = generate_regional_data()
    heritage_data = get_heritage_sites_data()
    
    # Save to CSV
    tourism_data.to_csv('data/csv/tourism_data.csv', index=False)
    art_forms_data.to_csv('data/csv/art_forms_data.csv', index=False)
    funding_data.to_csv('data/csv/funding_data.csv', index=False)
    monthly_data.to_csv('data/csv/monthly_data.csv', index=False)
    regional_data.to_csv('data/csv/regional_data.csv', index=False)
    heritage_data.to_csv('data/csv/heritage_data.csv', index=False)

def load_all_data():
    """Load all datasets"""
    # Check if data directory exists, if not create it
    os.makedirs('data/csv', exist_ok=True)
    
    # Get heritage sites data from Snowflake
    heritage_data = get_heritage_sites_data()
    
    # Load or generate other datasets
    tourism_data = generate_tourism_data()
    art_forms_data = generate_art_forms_data()
    funding_data = generate_funding_data()
    monthly_data = generate_monthly_data()
    regional_data = generate_regional_data()
    
    return tourism_data, art_forms_data, funding_data, monthly_data, regional_data, heritage_data

# If run directly, generate and save datasets
if __name__ == "__main__":
    save_data_to_csv()