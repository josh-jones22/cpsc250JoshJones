import matplotlib.pyplot as plt
import pandas as pd

file_name = input()

df = pd.read_csv(file_name)

# 2. Insert a new column labelled "Size" at the end of the dataframe
df['Size'] = df['Gross Potential'] / 2

# 3. Output the dataframe using the print() function
print(df)

# 4. Create a scatter plot of "Gross Potential" vs "Capacity"
plt.scatter(df['Capacity'], df['Gross Potential'], marker='x', color='orange', s=df['Size'])

# 5. Add the x-label, y-label, and title to the figure
plt.xlabel('Capacity', fontsize=10)
plt.ylabel('Gross Potential', fontsize=10)
plt.title('Gross Potential vs Capacity', fontsize=16)

# 6. Add gridlines to the figure
plt.grid(linestyle='--')

# 7. Save the figure as output_fig.png
plt.savefig('output_fig.png')
plt.show()
