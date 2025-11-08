import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/water_quality.csv')

# Bar chart
plt.figure()
df.plot(x='State', y='pH', kind='bar')
plt.title('pH Levels by State')
plt.xlabel('State')
plt.ylabel('pH')
plt.tight_layout()
plt.savefig('ph_levels.png')
