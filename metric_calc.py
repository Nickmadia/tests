import pandas as pd
import matplotlib.pyplot as plt

# Read the results CSV file
results_df = pd.read_csv('results.csv')

# Calculate Sensitivity, Specificity, and Accuracy for each tool
results_df['Sensitivity'] = results_df['True Positives (TP)'] / (results_df['True Positives (TP)'] + results_df['False Negatives (FN)']) * 100
results_df['Specificity'] = results_df['True Negatives (TN)'] / (results_df['True Negatives (TN)'] + results_df['False Positives (FP)']) * 100
results_df['Accuracy'] = (results_df['True Positives (TP)'] + results_df['True Negatives (TN)']) / (results_df['True Positives (TP)'] + results_df['True Negatives (TN)'] + results_df['False Positives (FP)'] + results_df['False Negatives (FN)']) * 100

# Set the tool as the index for easier plotting
results_df.set_index('Tool', inplace=True)

# Plot Sensitivity for each tool
plt.figure(figsize=(10, 6))
results_df['Sensitivity'].plot(kind='bar', color='skyblue')
plt.title('Sensitivity by Tool')
plt.xlabel('Tool')
plt.ylabel('Sensitivity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sensitivity_by_tool.png')

# Plot Specificity for each tool
plt.figure(figsize=(10, 6))
results_df['Specificity'].plot(kind='bar', color='salmon')
plt.title('Specificity by Tool')
plt.xlabel('Tool')
plt.ylabel('Specificity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('specificity_by_tool.png')

# Plot Accuracy for each tool
plt.figure(figsize=(10, 6))
results_df['Accuracy'].plot(kind='bar', color='lightgreen')
plt.title('Accuracy by Tool')
plt.xlabel('Tool')
plt.ylabel('Accuracy')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('accuracy_by_tool.png')
