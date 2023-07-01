import pandas as pd

file_name = input()

# Read in file_name as a dataframe
df = pd.read_csv(file_name, sep='\t')

# Output rows by descending Final scores
df_sorted = df.sort_values(by='Final', ascending=False)

print(df_sorted.to_string(index=False))

# Output the max scores of each assignment
print("\nMax Scores:")
max_scores = df[['Midterm1', 'Midterm2', 'Final']].max()
print(max_scores)

# Output the median scores of each assignment
print("\nMedian Scores:")
median_scores = df[['Midterm1', 'Midterm2', 'Final']].median()
print(median_scores)

# Output the average scores of each assignment
print("\nAverage Scores:")
avg_scores = df[['Midterm1', 'Midterm2', 'Final']].mean()
print(avg_scores)

# Output the standard deviation of each assignment
print("\nStandard Deviation:")
std_scores = df[['Midterm1', 'Midterm2', 'Final']].std()
print(std_scores)