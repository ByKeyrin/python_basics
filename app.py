"""
Point d'entrée du programme :

Ce script montre des exemples d'utilisation pour la gestion de fichiers CSV, JSON et XML.
Pour chaque format, il :
- Convertit une chaîne de caractères en fichier (CSV, JSON, XML)
- Relit le fichier créé et affiche son contenu

Exemples utilisés :
- Alice et Bob avec leurs âges

Fonctions importées :
- string_to_csv, csv_to_string (csv_management)
- string_to_json, json_to_string (json_management)
- string_to_xml, xml_to_string (xml_management)
- double_liste, filtre_pairs (map_filter)
"""
from modules.csv_management import string_to_csv, csv_to_string, string_to_csv_dict, csv_to_string_dict
from modules.json_management import string_to_json, json_to_string
from modules.xml_management import string_to_xml, xml_to_string
from modules.map_filter import double_liste, filtre_pairs
from modules.database_management import SimpleDatabase

if __name__ == "__main__":
    print("Bienvenue dans le main de l'application !")

    # Exemple d'utilisation : conversion d'une chaîne en CSV puis relecture du CSV
    csv_data = "nom,age\nAlice,30\nBob,25"
    print("\nCréation d'un fichier CSV à partir d'une chaîne :")
    filename = string_to_csv(csv_data)
    print(f"Fichier créé : {filename}")

    print("\nLecture du contenu du fichier CSV :")
    contenu = csv_to_string(filename)
    print(contenu)

    # Exemple d'utilisation : conversion d'une chaîne en CSV via DictWriter puis relecture avec DictReader
    print("\nCréation d'un fichier CSV (DictWriter) à partir d'une chaîne :")
    filename_dict = string_to_csv_dict(csv_data)
    print(f"Fichier créé (DictWriter) : {filename_dict}")

    print("\nLecture du contenu du fichier CSV (DictReader) :")
    contenu_dict = csv_to_string_dict(filename_dict)
    print(contenu_dict)

    # Exemple d'utilisation : conversion d'une chaîne JSON puis relecture du JSON
    json_data = '[{"nom": "Alice", "age": 30}, {"nom": "Bob", "age": 25}]'
    print("\nCréation d'un fichier JSON à partir d'une chaîne :")
    json_filename = string_to_json(json_data)
    print(f"Fichier JSON créé : {json_filename}")

    print("\nLecture du contenu du fichier JSON :")
    json_contenu = json_to_string(json_filename)
    print(json_contenu)

    # Exemple d'utilisation : conversion d'une chaîne XML puis relecture du XML
    xml_data = """<personnes>\n  <personne><nom>Alice</nom><age>30</age></personne>\n  <personne><nom>Bob</nom><age>25</age></personne>\n</personnes>"""
    print("\nCréation d'un fichier XML à partir d'une chaîne :")
    xml_filename = string_to_xml(xml_data)
    print(f"Fichier XML créé : {xml_filename}")

    print("\nLecture du contenu du fichier XML :")
    xml_contenu = xml_to_string(xml_filename)
    print(xml_contenu)

    # Exemple d'utilisation de map et filter
    nombres = [1, 2, 3, 4, 5]
    print("\nListe de départ :", nombres)

    doubles = double_liste(nombres)
    print("Après map (x2) :", doubles)

    pairs = filtre_pairs(nombres)
    print("Après filter (pairs) :", pairs)

    # Exemple d'utilisation de la base de données SQLite
    print("\n--- Exemple base de données SQLite ---")
    db = SimpleDatabase()
    db.insert_personne("Alice", 30)
    db.insert_personne("Bob", 25)
    personnes = db.get_all_personnes()
    print("Toutes les personnes dans la base :", personnes)
    db.close()