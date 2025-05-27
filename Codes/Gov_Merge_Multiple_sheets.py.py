import os
import pandas as pd
from pathlib import Path

# Folder path
folder_path = Path(r"C:\Users\Administrator\Desktop\Project\Data\Cultural Heritage")
output_file = folder_path / "merged_output.xlsx"

# List to hold dataframes
all_data = []

for file in folder_path.iterdir():
    # Skip the output file itself
    if file.name == "merged_output.xlsx":
        continue

    try:
        if file.suffix.lower() in ['.xlsx', '.xls', '.xlsm']:
            df = pd.read_excel(file, engine='openpyxl' if file.suffix.lower() == '.xlsx' else None)
        elif file.suffix.lower() == '.csv':
            df = pd.read_csv(file)
        else:
            continue  # skip unsupported file types

        df['SourceFile'] = file.stem  # Add source file name as a column
        all_data.append(df)
        print(f"✅ Loaded: {file.name}")

    except Exception as e:
        print(f"❌ Failed to read {file.name}: {e}")

# Combine all dataframes into one
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_excel(output_file, sheet_name='MergedData', index=False)
    print(f"\n✅ All data saved to: {output_file}")
else:
    print("⚠️ No valid files were loaded.")










# import os
# import pandas as pd

# from pathlib import Path

# # Set the folder containing your Excel and CSV files
# folder_path = Path(r"C:\Users\Administrator\Desktop\Project\Data\Cultural Heritage")
# output_file = folder_path / "merged_output.xlsx"

# # Create an Excel writer
# with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
#     for file in folder_path.iterdir():
#         if file.suffix.lower() in ['.xlsx', '.xls', '.xlsm']:
#             try:
#                 df = pd.read_excel(file)
#                 sheet_name = file.stem[:31]  # Sheet name max 31 chars
#                 df.to_excel(writer, sheet_name=sheet_name, index=False)
#                 print(f"Added Excel file: {file.name}")
#             except Exception as e:
#                 print(f"Failed to read Excel file {file.name}: {e}")

#         elif file.suffix.lower() == '.csv':
#             try:
#                 df = pd.read_csv(file)
#                 sheet_name = file.stem[:31]
#                 df.to_excel(writer, sheet_name=sheet_name, index=False)
#                 print(f"Added CSV file: {file.name}")
#             except Exception as e:
#                 print(f"Failed to read CSV file {file.name}: {e}")

# print(f"\n✅ Merged file saved as: {output_file}")
