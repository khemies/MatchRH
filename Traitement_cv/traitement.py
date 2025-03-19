import pandas as pd
# Charger le fichier CSV
file_path = "C:/Users/khmai/OneDrive/Bureau/PFE/MatchRH/Data/CV_csv/cv_thèque_france_travail_data.csv"
df = pd.read_csv(file_path)

# Renommer les colonnes principales avec des noms plus clairs
new_column_names = {
    "Titre": "Poste_recherche",
    "subtext": "Disponibilite",
    "subtext1": "Date_mise_a_jour",
    "date": "Date_actualisation",
    "description": "Presentation",
    "information": "Points_forts",
    "motclé": "Competences",
    "textlink": "Accroche_candidat",
    "btn_lien": "Lien_profil"
}
df.rename(columns=new_column_names, inplace=True)

# Fusionner les colonnes similaires (cvresult, cvresult1...) en une seule colonne
cv_columns = [col for col in df.columns if "cvresult" in col]
df["CV_Complet"] = df[cv_columns].apply(lambda row: " ".join(row.dropna().astype(str)), axis=1)
df.drop(columns=cv_columns, inplace=True)

# Fusionner les colonnes de mots-clés en une seule
keywords_columns = [col for col in df.columns if "motclé" in col]
df["Mots_clés_complets"] = df[keywords_columns].apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)
df.drop(columns=keywords_columns, inplace=True)

# Exporter le fichier modifié
df.to_csv("C:/Users/khmai/OneDrive/Bureau/PFE/MatchRH/Data/Data_cleaned/cv_theque_france_travail_cleaned.csv", index=False)
print("Fichier modifié enregistré sous 'cv_theque_france_travail_cleaned.csv'")
