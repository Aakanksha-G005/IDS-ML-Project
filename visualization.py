import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("final_dataset.csv")

# -----------------------------
# 1. PACKET LENGTH DISTRIBUTION
# -----------------------------
plt.figure()
plt.hist(df['Length'], bins=50)
plt.title("Packet Length Distribution")
plt.xlabel("Packet Length")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 2. PROTOCOL COUNT GRAPH
# -----------------------------
plt.figure()
df['Protocol'].value_counts().plot(kind='bar')
plt.title("Protocol Count")
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 3. PACKET RATE VS TIME
# -----------------------------
plt.figure()
plt.scatter(df['Time'], df['Packet_rate'])
plt.title("Packet Rate vs Time")
plt.xlabel("Time")
plt.ylabel("Packet Rate")
plt.show()

# -----------------------------
# 4. HISTOGRAM OF TIME_DIFF
# -----------------------------
plt.figure()
plt.hist(df['Time_diff'], bins=50)
plt.title("Time Difference Distribution")
plt.xlabel("Time Difference")
plt.ylabel("Frequency")
plt.show()