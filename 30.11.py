import matplotlib.pyplot as plt
import pandas as pd

file = input()

df = pd.read_csv(file)

# Calculate the average of flight delays and flight cancellations
avg_delays = round(df["Delayed"].mean(), 2)
avg_cancellations = round(df["Cancelled"].mean(), 2)
print(f"Average delays: {avg_delays}\nAverage cancellations: {avg_cancellations:.2f}")

# Create a lineplot of flight delays vs months and flight cancellations vs months
df.plot(x="Month", y=["Delayed", "Cancelled"])
plt.title("Flight status at LAX", fontsize=14)
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.legend(["Delays", "Cancellations"])
# TODO: Read in the CSV file as a dataframe


# TODO: Print the average of flight delays and flight cancellations


# TODO: Create a lineplot of flight delays vs months


# TODO: In the same figure, create a lineplot of flight cancellations vs months


# TODO: Add axis labels, title, and legend


# Save figure as output_fig.png
plt.savefig('output_fig.png')