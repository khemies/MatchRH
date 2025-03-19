import pandas as pd

# Charger les deux datasets
df1 = pd.read_csv('C:/Users/khmai/OneDrive/Bureau/PFE/MatchRH/Data_cleaned/Profil-version2.csv')
df2 = pd.read_csv('C:/Users/khmai/OneDrive/Bureau/PFE/MatchRH/Data_cleaned/Profil-version3.csv')

# Combiner les deux datasets
combined_df = pd.concat([df1, df2], ignore_index=True)

# Supprimer les doublons
combined_df = combined_df.drop_duplicates()

# Sauvegarder le nouveau dataset sans doublons
combined_df.to_csv('combined_no_duplicates_cv.csv', index=False)
