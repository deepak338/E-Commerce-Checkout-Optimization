import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# 1. Define traffic volume (Let's make it a solid sample size)
n_users = 100000 

# 2. Simulate User IDs and Device Types (80% Desktop, 20% Mobile)
user_ids = np.arange(1, n_users + 1)
devices = np.random.choice(['Desktop', 'Mobile'], size=n_users, p=[0.8, 0.2])

# 3. Simulate A/B Test Groups (50/50 split)
groups = np.random.choice(['Control', 'Treatment'], size=n_users, p=[0.5, 0.5])

df = pd.DataFrame({'user_id': user_ids, 'device': devices, 'group': groups})

# 4. Define Conversion Probabilities (The Simpson's Paradox setup)
# Control: Steady 10% across the board
# Treatment: Desktop surges to 15%, Mobile crashes to 4% due to a "UI bug"
def assign_conversion(row):
    if row['group'] == 'Control':
        return np.random.choice([0, 1], p=[0.90, 0.10])
    elif row['group'] == 'Treatment' and row['device'] == 'Desktop':
        return np.random.choice([0, 1], p=[0.85, 0.15])
    elif row['group'] == 'Treatment' and row['device'] == 'Mobile':
        return np.random.choice([0, 1], p=[0.96, 0.04])

df['converted'] = df.apply(assign_conversion, axis=1)

# 5. Inject some "messiness" (duplicate users) to show off data cleaning skills
duplicates = df.sample(500)
df = pd.concat([df, duplicates])

# Save to CSV for Tableau later
df.to_csv('checkout_ab_test_data.csv', index=False)
print("Dataset generated and saved!")