import pandas as pd
import numpy as np
import os

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
    # List of states
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir'
    ]
    
    # List of art forms with their type and state
    art_forms = [
        {'art_form': 'Bharatanatyam', 'type': 'Dance', 'state': 'Tamil Nadu', 
         'description': 'A classical dance form known for its grace, purity, and sculpturesque poses.'},
        {'art_form': 'Kathakali', 'type': 'Dance Drama', 'state': 'Kerala',
         'description': 'A stylized classical dance-drama noted for its elaborate costumes and makeup.'},
        {'art_form': 'Madhubani', 'type': 'Painting', 'state': 'Bihar',
         'description': 'A distinctive style of folk painting with geometric patterns and nature motifs.'},
        {'art_form': 'Warli', 'type': 'Painting', 'state': 'Maharashtra',
         'description': 'A tribal art form using basic geometric shapes and white pigment.'},
        {'art_form': 'Gond', 'type': 'Painting', 'state': 'Madhya Pradesh',
         'description': 'A form of painting from central India, reflecting the belief that viewing good images begets good luck.'},
        {'art_form': 'Kathak', 'type': 'Dance', 'state': 'Uttar Pradesh',
         'description': 'A classical dance form that tells stories through rhythmic foot movements and expressive gestures.'},
        {'art_form': 'Odissi', 'type': 'Dance', 'state': 'Odisha',
         'description': 'One of the oldest surviving dance forms in India with a strong foundation in Natya Shastra.'},
        {'art_form': 'Manipuri', 'type': 'Dance', 'state': 'Manipur',
         'description': 'A graceful dance form characterized by gentle movements and swaying.'},
        {'art_form': 'Kuchipudi', 'type': 'Dance', 'state': 'Andhra Pradesh',
         'description': 'A dance-drama performance with roots in ancient Hindu Sanskrit text of Natya Shastra.'},
        {'art_form': 'Sattriya', 'type': 'Dance', 'state': 'Assam',
         'description': 'A dance form that tells mythological stories, traditionally performed in monasteries.'},
        {'art_form': 'Phad', 'type': 'Painting', 'state': 'Rajasthan',
         'description': 'A style of scroll painting depicting folk epics and legends.'},
        {'art_form': 'Pattachitra', 'type': 'Painting', 'state': 'Odisha',
         'description': 'A cloth-based scroll painting with rich colorful application, creative motifs, and designs.'},
        {'art_form': 'Tanjore', 'type': 'Painting', 'state': 'Tamil Nadu',
         'description': 'A classical South Indian painting style characterized by rich, flat colors and gold foil.'},
        {'art_form': 'Kalamkari', 'type': 'Textile Art', 'state': 'Andhra Pradesh',
         'description': 'An ancient style of hand painting on cotton or silk fabric using natural dyes.'},
        {'art_form': 'Bandhani', 'type': 'Textile Art', 'state': 'Gujarat',
         'description': 'A tie and dye textile decorated with dots, waves, and stripes.'},
        {'art_form': 'Chikankari', 'type': 'Embroidery', 'state': 'Uttar Pradesh',
         'description': 'A traditional embroidery style known for its subtlety and grace.'},
        {'art_form': 'Pashmina', 'type': 'Textile Art', 'state': 'Jammu and Kashmir',
         'description': 'Fine cashmere wool textiles known for their softness, warmth, and lightweight quality.'},
        {'art_form': 'Meenakari', 'type': 'Jewelry', 'state': 'Rajasthan',
         'description': 'The art of coloring and ornamenting the surface of metals by fusing brilliant colors.'},
        {'art_form': 'Bidri', 'type': 'Metalwork', 'state': 'Karnataka',
         'description': 'A metal handicraft from Bidar known for its striking inlay artwork.'},
        {'art_form': 'Blue Pottery', 'type': 'Pottery', 'state': 'Rajasthan',
         'description': 'A Turko-Persian art form with Jaipur as its center, known for its vibrant blue dye.'},
        {'art_form': 'Chhau', 'type': 'Dance', 'state': 'West Bengal',
         'description': 'A semi-classical dance with martial, tribal, and folk traditions.'},
        {'art_form': 'Yakshagana', 'type': 'Theater', 'state': 'Karnataka',
         'description': 'A traditional theater form combining dance, music, dialogue, and costumes.'},
        {'art_form': 'Nautanki', 'type': 'Theater', 'state': 'Uttar Pradesh',
         'description': 'A popular folk operatic theater performance with elements of fantasy, romance, and social issues.'},
        {'art_form': 'Lavani', 'type': 'Dance', 'state': 'Maharashtra',
         'description': 'A traditional dance form combining song and dance, performed to the beats of a dholki.'},
        {'art_form': 'Ghoomar', 'type': 'Dance', 'state': 'Rajasthan',
         'description': 'A traditional folk dance performed by women in swirling robes.'},
        {'art_form': 'Bhangra', 'type': 'Dance', 'state': 'Punjab',
         'description': 'An energetic folk dance celebrating the harvest season.'},
        {'art_form': 'Thangka', 'type': 'Painting', 'state': 'Sikkim',
         'description': 'A Tibetan Buddhist painting on cotton or silk, usually depicting Buddhist deities.'},
        {'art_form': 'Rogan', 'type': 'Textile Art', 'state': 'Gujarat',
         'description': 'An art of cloth painting using a castor oil-based paint and stylus for drawing.'},
        {'art_form': 'Terracotta', 'type': 'Pottery', 'state': 'West Bengal',
         'description': 'Clay-based craft used for making sculptures and decorative items.'},
        {'art_form': 'Dokra', 'type': 'Metalwork', 'state': 'Chhattisgarh',
         'description': 'An ancient lost-wax casting technique for making brass artifacts.'}
    ]
    
    # Create data list
    data = []
    
    # Add each art form with a popularity score
    for art in art_forms:
        popularity = np.random.randint(6, 11)  # Popularity score from 6 to 10
        data.append({
            'art_form': art['art_form'],
            'type': art['type'],
            'state': art['state'],
            'popularity': popularity,
            'description': art['description']
        })
    
    # Generate more art forms for the remaining states
    art_types = ['Dance', 'Painting', 'Textile Art', 'Sculpture', 'Music', 'Theater', 'Pottery', 'Metalwork', 'Embroidery']
    
    for state in states:
        if state not in [art['state'] for art in art_forms]:
            # Add 1-3 art forms for states without any
            for _ in range(np.random.randint(1, 4)):
                art_type = np.random.choice(art_types)
                art_form = f"{state} {art_type}"
                popularity = np.random.randint(4, 9)  # Slightly lower popularity
                
                data.append({
                    'art_form': art_form,
                    'type': art_type,
                    'state': state,
                    'popularity': popularity,
                    'description': f"A traditional {art_type.lower()} form from {state}."
                })
    
    # Create DataFrame
    art_forms_df = pd.DataFrame(data)
    
    return art_forms_df

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
    
    # Save to CSV
    tourism_data.to_csv('data/csv/tourism_data.csv', index=False)
    art_forms_data.to_csv('data/csv/art_forms_data.csv', index=False)
    funding_data.to_csv('data/csv/funding_data.csv', index=False)
    monthly_data.to_csv('data/csv/monthly_data.csv', index=False)
    regional_data.to_csv('data/csv/regional_data.csv', index=False)

def load_all_data():
    """Load all datasets"""
    # Check if data directory exists, if not create it
    os.makedirs('data/csv', exist_ok=True)
    
    # Check if CSV files exist, if not generate them
    if not (os.path.exists('data/csv/tourism_data.csv') and
            os.path.exists('data/csv/art_forms_data.csv') and
            os.path.exists('data/csv/funding_data.csv') and
            os.path.exists('data/csv/monthly_data.csv') and
            os.path.exists('data/csv/regional_data.csv')):
        save_data_to_csv()
    
    # Load datasets
    try:
        tourism_data = pd.read_csv('data/csv/tourism_data.csv')
        art_forms_data = pd.read_csv('data/csv/art_forms_data.csv')
        funding_data = pd.read_csv('data/csv/funding_data.csv')
        monthly_data = pd.read_csv('data/csv/monthly_data.csv')
        regional_data = pd.read_csv('data/csv/regional_data.csv')
    except:
        # If loading fails, generate new data
        tourism_data = generate_tourism_data()
        art_forms_data = generate_art_forms_data()
        funding_data = generate_funding_data()
        monthly_data = generate_monthly_data()
        regional_data = generate_regional_data()
        
        # Save the generated data
        tourism_data.to_csv('data/csv/tourism_data.csv', index=False)
        art_forms_data.to_csv('data/csv/art_forms_data.csv', index=False)
        funding_data.to_csv('data/csv/funding_data.csv', index=False)
        monthly_data.to_csv('data/csv/monthly_data.csv', index=False)
        regional_data.to_csv('data/csv/regional_data.csv', index=False)
    
    return tourism_data, art_forms_data, funding_data, monthly_data, regional_data

# If run directly, generate and save datasets
if __name__ == "__main__":
    save_data_to_csv()