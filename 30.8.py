# TODO: Import NumPy
import numpy as np

# Read two sets of exam scores from user input
exam1 = np.array(input().split(), dtype=float)
exam2 = np.array(input().split(), dtype=float)

# Compute the average scores for each student
average_scores = (exam1 + exam2) / 2

# Output the average scores
print("Average scores:", average_scores)

# Count the number of scores that are 80 or above
count = np.count_nonzero(average_scores >= 80)

# Output the count
print("Number of students who received 80 and above:", count)