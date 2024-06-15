import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step  1: Read the CSV file
df = pd.read_csv('angleData.csv')

# Step  2: Normalize the color values
colors = df['color'].values /  100.0  # Assuming 'color' is the name of the fourth column

# Step  3: Create the  3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = df['x'].values  # Assuming 'x' is the name of the first column
y = df['y'].values  # Assuming 'y' is the name of the second column
z = df['z'].values  # Assuming 'z' is the name of the third column

ax.scatter(x, y, z, c=colors, cmap='viridis')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot with Color')

# Show the plot
plt.show()
