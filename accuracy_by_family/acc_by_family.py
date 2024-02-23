import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files into DataFrames
accuracy_data = pd.read_csv("../results.csv")
malware_data = pd.read_csv("../malware.csv")

# Group the accuracy data by 'Tool'
grouped_accuracy = accuracy_data.groupby('Tool')

# Define a function to calculate Accuracy
def calculate_accuracy(tp, tn, fp, fn):
    return (tp + tn) / (  fp + fn)

# Iterate over each group (Tool)
for tool, group in grouped_accuracy:
    # Initialize lists to store malware families and accuracies
    malware_families = []
    accuracies = []
    
    # Get the accuracy values for the current tool
    tp = group['True Positives (TP)'].values[0]
    tn = group['True Negatives (TN)'].values[0]/6
    fp = group['False Positives (FP)'].values[0]/6
    fn = group['False Negatives (FN)'].values[0]
    
    # Calculate Accuracy for each malware family
    for index, row in malware_data.iterrows():
        malware_family = row['malware_family']
        malware_tp = row['positive'] if row['tool'] == tool else 0
        malware_fn = row['sample_size'] - malware_tp if row['tool'] == tool else 0
        
        accuracy = calculate_accuracy( malware_tp, tn, 50, 50)
        malware_families.append(malware_family)
        accuracies.append(accuracy)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(malware_families, accuracies, color='lightgreen')
    plt.title(f"Accuracy for {tool}")
    plt.xlabel('Malware Family')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    
    # Save the plot as an image file
    plt.savefig(f"{tool}_accuracy.png")
    
    # Close the plot to avoid displaying it inline
    plt.close()
