import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic GATK Variant Quality (QUAL) and Read Depth (DP) metrics
sample_qual = np.random.uniform(30, 110, 50)
sample_dp = np.random.uniform(10, 70, 50)

# Plotting the GATK QC metrics
plt.figure(figsize=(6, 4), dpi=300)
sns.scatterplot(x=sample_dp, y=sample_qual, color='purple', s=70)

# Add a quality control threshold line at QUAL = 40
plt.axhline(40, color='red', linestyle='--', label='QC Threshold (QUAL=40)')

# Add labels and formatting
plt.title("GATK Variant Quality & Read Depth QC")
plt.xlabel("Read Depth (DP)")
plt.ylabel("Variant Quality (QUAL)")
plt.legend(loc='lower right')
plt.tight_layout()

# Save the figure
plt.savefig("gatk_qc.png")
plt.close()
