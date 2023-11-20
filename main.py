import os
import pandas as pd

# Define the directory where the files are located
directory = '/path/to/your/directory'

# Create an empty dataframe to store patient names
hasta_isimleri = pd.DataFrame(columns=['Patient_Name'])

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx") and ('gaitx' in filename or 'gaitrite' in filename):
        # Extract patient name from the filename
        patient_name = filename.split('_')[0]
        # Append the patient name to the dataframe
        hasta_isimleri = hasta_isimleri.append({'Patient_Name': patient_name}, ignore_index=True)

        # Read the Excel file
        df = pd.read_excel(os.path.join(directory, filename))

        # Print the dataframe
        print(df)

# Print the patient names dataframe
print(hasta_isimleri)