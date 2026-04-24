import pandas as pd
# Load dataset
df = pd.read_csv("raw_dataset.csv")

print("Original Dataset:")
print(df.head())
# -----------------------------
# STEP 1: REMOVE UNNECESSARY COLUMNS
# -----------------------------
columns_to_drop = ['No', 'Source', 'Destination', 'Info']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
# -----------------------------
# STEP 2: ENCODE PROTOCOL
# -----------------------------
df['Protocol'] = df['Protocol'].astype('category').cat.codes
# -----------------------------
# STEP 3: HANDLE TIME COLUMN
# -----------------------------
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df = df.dropna()
# ----------------------------
# STEP 4: CREATE NEW FEATURES
# -----------------------------
# Time difference
df['Time_diff'] = df['Time'].diff().fillna(0)
# Packet rate (avoid division by zero)
df['Packet_rate'] = 1 / (df['Time_diff'] + 0.0001)
# -----------------------------
# STEP 5: FINAL DATASET
# -----------------------------
final_df = df[['Time', 'Protocol', 'Length', 'Time_diff', 'Packet_rate', 'Label']]
# Save processed dataset
final_df.to_csv("final_dataset.csv", index=False)
print("\nProcessed Dataset:")
print(final_df.head())
print("\n✅ Preprocessing Completed. File saved as final_dataset.csv")