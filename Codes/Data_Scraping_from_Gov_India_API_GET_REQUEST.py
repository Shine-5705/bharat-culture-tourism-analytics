



import pandas as pd
import requests

API_KEY = "579b464db66ec23bdd0000018f277462e8cb454b5e2f84c9b4bd931a"
RESOURCE_ID = "84e62989-74c9-442d-a460-3b949ccd53ed"
url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=csv&limit=1000"

# Download CSV using requests
response = requests.get(url, verify=False)  # Use verify=False temporarily if SSL fails

# Save the file locally
with open("tourist_data.csv", "wb") as f:
    f.write(response.content)

# Load CSV into DataFrame
df = pd.read_csv("tourist_data.csv")
print(df.head())