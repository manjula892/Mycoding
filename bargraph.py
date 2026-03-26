import numpy as np
import matplotlib.pyplot as plt

overs = np.arange(1, 10)  # match scores length
scores = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])

plt.bar(overs, scores, color='blue')
plt.xlabel('Overs')
plt.ylabel('Scores')
plt.title('Cricket Scores')
plt.xticks(overs)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()