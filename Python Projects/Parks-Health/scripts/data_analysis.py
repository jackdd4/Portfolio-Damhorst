import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the integrated data set
df = pd.read_csv('data/integrated.csv')

# Create a scatterplot of obesity rate vs. parking ranking, labeled by state
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Obesity among adults", y="Rank", data=df, s=100, color='blue')

# Add state labels to each point
for i in range(len(df)):
    plt.text(
        x=df["Obesity among adults"][i] + 0.1,
        y=df["Rank"][i],
        s=df["stateabbr"][i],
        horizontalalignment='left',
        size='medium',
        color='black'
    )
    
# Configure plot appearance
plt.title("Obesity Rate vs Park Score Ranking by State")
plt.xlabel("Obesity Rate (%)")
plt.ylabel("Rank")
plt.gca().invert_yaxis()
plt.grid(True)

# Save the plot to a file
plt.savefig('results/obesity_vs_park_score.png', dpi=300, bbox_inches='tight')
