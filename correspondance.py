import pandas as pd
import random

# Chemins des fichiers sources
rome_metiers_path = "RefRomeCsv/unix_referentiel_code_rome_v460_utf8.csv"
centres_interet_path = "RefRomeCsv/unix_centre_interet_v460_utf8.csv"

# Lire les fichiers CSV
metiers_df = pd.read_csv(rome_metiers_path)
centres_df = pd.read_csv(centres_interet_path)

# Extraire les codes de centres d'intérêt
centres_codes = centres_df['code_centre_interet'].dropna().unique().tolist()

# Nettoyer les codes ROME (valides à 5 caractères)
metiers_df = metiers_df[metiers_df['code_rome'].apply(lambda x: isinstance(x, str) and len(x) == 5)]
metiers_codes = metiers_df['code_rome'].tolist()

# Regrouper les métiers par famille (première lettre)
familles_metiers = {}
for code in metiers_codes:
    prefix = code[0]
    familles_metiers.setdefault(prefix, []).append(code)

# Créer le mapping CI ↔ métiers
mapping = []
familles = list(familles_metiers.keys())

for ci in centres_codes:
    nb_familles = random.choice([1, 2])
    selected_familles = random.sample(familles, nb_familles)
    for fam in selected_familles:
        sample_metiers = random.sample(familles_metiers[fam], min(5, len(familles_metiers[fam])))
        for rome_code in sample_metiers:
            mapping.append({"code_centre_interet": ci, "code_rome": rome_code})

# Sauvegarder dans un fichier CSV
mapping_df = pd.DataFrame(mapping)
mapping_df.to_csv("RefRomeCsv/unix_lien_centre_metier.csv", index=False)

print("✅ Fichier unix_lien_centre_metier.csv généré avec succès.")
