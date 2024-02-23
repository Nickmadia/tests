import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv("../malware.csv")

# Group the data by 'tool'
grouped_data = data.groupby('tool')

# Define a function to calculate Sensitivity
def calculate_sensitivity(tp, fn):
    return tp / (tp + fn)

# Iterate over each group (tool)
for tool, group in grouped_data:
    # Initialize lists to store malware families and sensitivities
    malware_families = []
    sensitivities = []
    
    # Calculate True Positives (TP) and False Negatives (FN) for each malware family
    for malware_family, family_group in group.groupby('malware_family'):
        tp = family_group['positive'].sum()
        fn = family_group['sample_size'].sum() - tp
        sensitivity = calculate_sensitivity(tp, fn)
        
        malware_families.append(malware_family)
        sensitivities.append(sensitivity)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(malware_families, sensitivities, color='skyblue')
    plt.title(f"Sensitivity for {tool}")
    plt.xlabel('Malware Family')
    plt.ylabel('Sensitivity')
    plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    
    # Save the plot as an image file
    plt.savefig(f"{tool}_sensitivity.png")
    
    # Close the plot to avoid displaying it inline
    plt.close()

