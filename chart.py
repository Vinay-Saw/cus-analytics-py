import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer segments
segments = ['Premium', 'Regular', 'Occasional', 'New']
data = []

# Premium customers: Higher spending, less variability
premium_purchases = np.random.gamma(shape=8, scale=75, size=150)
data.extend([{'Segment': 'Premium', 'Purchase Amount ($)': amount} 
             for amount in premium_purchases])

# Regular customers: Moderate spending, moderate variability
regular_purchases = np.random.gamma(shape=5, scale=45, size=200)
data.extend([{'Segment': 'Regular', 'Purchase Amount ($)': amount} 
             for amount in regular_purchases])

# Occasional customers: Lower spending, high variability
occasional_purchases = np.random.gamma(shape=3, scale=30, size=180)
data.extend([{'Segment': 'Occasional', 'Purchase Amount ($)': amount} 
             for amount in occasional_purchases])

# New customers: Mixed spending, exploration phase
new_purchases = np.random.gamma(shape=4, scale=40, size=120)
data.extend([{'Segment': 'New', 'Purchase Amount ($)': amount} 
             for amount in new_purchases])

# Create DataFrame
df = pd.DataFrame(data)

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create boxplot with professional styling
ax = sns.boxplot(
    data=df,
    x='Segment',
    y='Purchase Amount ($)',
    palette='Set2',
    linewidth=2,
    fliersize=5,
    order=['Premium', 'Regular', 'New', 'Occasional']
)

# Customize the plot
plt.title('Purchase Amount Distribution by Customer Segment\n',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Customer Segment', fontsize=13, fontweight='bold')
plt.ylabel('Purchase Amount ($)', fontsize=13, fontweight='bold')

# Add grid for better readability
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0, ha='center')

# Add subtle styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white')
print("Chart successfully generated: chart.png (512x512 pixels)")

# Close the plot
plt.close()