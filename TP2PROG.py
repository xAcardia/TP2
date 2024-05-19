#Ethan L.P
#Hakim Azizi

#Exercise 1

import json
import csv


# Les donnés JSON
data = [[2, 3], [3, 2], [1.0, -5.3]]

# Créer un fichier JSON 
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Lire le fichier JSON
try:
    with open('data.json', 'r') as json_file:
        complex_numbers = json.load(json_file)

    # Écrire dans un fichier CSV
    with open('complex_numbers.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Écrire l'en-tête
        csv_writer.writerow(['reel', 'imaginaire'])
        # Écrire les données
        for number in complex_numbers:
            csv_writer.writerow(number)

    print("Les nombres ont été écrits dans le fichier 'complex_numbers.csv'")

except FileNotFoundError:
    print("Le fichier 'data.json' n'a pas été trouvé.")



#Exercise 2

# Données pokemon
pokemons = [
    ["Pikachu", 35, 55, 30, 50, 40, 90],
    ["Charizard", 78, 84, 78, 109, 85, 100],
    ["Magikarp", 20, 10, 55, 15, 20, 80]
]

# Création du fichier CSV
with open('pokemon.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(pokemons)

print("Fichier 'pokemon.csv' créé avec succès.")


def charger_pokemons_csv(fichier_csv):
    pokemons = {}
    with open(fichier_csv, newline='') as csv_file:
        lecteur_csv = csv.reader(csv_file)
        for ligne in lecteur_csv:
            nom = ligne[0]
            stats = list(map(int, ligne[1:]))
            pokemons[nom] = stats
    return pokemons


# Spécifiez le chemin du fichier CSV
fichier_csv = 'pokemon.csv'

# Tests
try:
    pkmn = charger_pokemons_csv(fichier_csv)
    for nom, stats in pkmn.items():
        print(f"{nom}: {stats}")

    # Vérification des types
    print(isinstance(pkmn, dict))  # Va afficher True
    print(isinstance(pkmn["Pikachu"], list))  # Va afficher True
    print(isinstance(pkmn["Pikachu"][0], int))  # Va afficher True

except FileNotFoundError:
    print(f"Le fichier '{fichier_csv}' n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")

