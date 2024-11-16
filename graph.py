import matplotlib.pyplot as plt

# Define the parameters
voter_clusters = [0.3, 0.4, 0.5, 0.6, 0.7]  # Voter distribution
candidate_positions = {"Macron": 0.4, "Le Pen": 0.2} 
median_voter_position = 0.5

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_yticks([])  

# Plot voter clusters as black dots
for i, voter in enumerate(voter_clusters):
    if i == 0:
        ax.plot(voter, 0.5, 'ko', markersize=8, label="Voter") 
    else:
        ax.plot(voter, 0.5, 'ko', markersize=8)

# Plot candidates
ax.plot(candidate_positions["Macron"], 0.6, 'bo', markersize=10, label="Macron (Right-wing)")
ax.plot(candidate_positions["Le Pen"], 0.6, 'ro', markersize=10, label="Le Pen (Left-wing)")

# Highlight the median voter
ax.plot(median_voter_position, 0.5, 'go', markersize=12, label="Median Voter")

# Add vertical lines
ax.axvline(x=median_voter_position, color='green', linestyle='--', label="Median Voter Line")
ax.axvline(x=candidate_positions["Macron"], color='blue', linestyle=':', label="Macron's Position")
ax.axvline(x=candidate_positions["Le Pen"], color='red', linestyle='-.', label="Le Pen's Position")

# Annotate points
ax.text(median_voter_position, 0.55, "Median Voter", color='green', fontsize=10, ha='center')
ax.text(candidate_positions["Macron"], 0.65, "Macron", color='blue', fontsize=10, ha='center')
ax.text(candidate_positions["Le Pen"], 0.65, "Le Pen", color='red', fontsize=10, ha='center')

# Titles and labels
ax.set_xlabel("Economic Policy Spectrum (0: Left-Wing, 1: Right-Wing)", fontsize=12)
ax.set_title("Spatial Voting Model Representation: 2022 French Presidential Election", fontsize=14)
ax.legend(loc="upper right")

# Display plot
plt.show()
