import matplotlib.pyplot as plt
import numpy as np

# Simulated data for energy consumption patterns and clustering
clusters = {
    0: np.random.normal(loc=50, scale=5, size=100),  # Cluster 0
    1: np.random.normal(loc=70, scale=5, size=100),  # Cluster 1
    2: np.random.normal(loc=90, scale=5, size=100),  # Cluster 2
}

# Anomalies
anomalies = np.random.normal(loc=120, scale=10, size=10)

# Visualize energy consumption patterns
plt.figure(figsize=(10, 6))
for cluster_id, data in clusters.items():
    plt.hist(data, bins=15, alpha=0.6, label=f'Cluster {cluster_id}')

# Add anomalies to the plot
plt.scatter(anomalies, [5] * len(anomalies), color='red', label='Anomalies', zorder=5)

plt.title('Energy Consumption Clustering Visualization')
plt.xlabel('Energy Consumption (kWh)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Simulate real-time recommendations as a bar graph
recommendations = ['Shift usage to off-peak hours', 'Investigate anomalies', 'Optimize load balance']
impact = [40, 30, 50]  # Simulated impact percentages

plt.figure(figsize=(8, 5))
plt.bar(recommendations, impact, color=['blue', 'orange', 'green'])
plt.title('Impact of Recommendations on Grid Efficiency')
plt.xlabel('Recommendations')
plt.ylabel('Impact (%)')
plt.ylim(0, 100)
plt.grid(axis='y')
plt.show()
