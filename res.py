import pandas as pd

# Read the CSV files into DataFrames
malware_df = pd.read_csv("malware.csv")
benign_df = pd.read_csv("benign.csv")

# Group the malware data by tool
malware_grouped_by_tool = malware_df.groupby('tool')

# Group the benign data by tool
benign_grouped_by_tool = benign_df.groupby('tool')

results = []

# Calculate TP, TN, FP, FN for each tool
for tool, malware_data in malware_grouped_by_tool:
    benign_data = benign_grouped_by_tool.get_group(tool)

    # Calculate True Positives (TP)
    true_positives = malware_data['positive'].sum()

    # Calculate False Negatives (FN)
    false_negatives = (malware_data['sample_size'] - malware_data['positive']).sum()

    # Calculate False Positives (FP)
    false_positives = (benign_data['sample_size'] - benign_data['correctly_identified']).sum()

    # Calculate True Negatives (TN)
    true_negatives = benign_data['correctly_identified'].sum()

    # Append results for each tool
    results.append({
        'Tool': tool,
        'True Positives (TP)': true_positives,
        'False Negatives (FN)': false_negatives,
        'False Positives (FP)': false_positives,
        'True Negatives (TN)': true_negatives
    })

# Create a DataFrame from the results
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('results.csv', index=False)

print("Results saved to results.csv")
