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
"""
from csv_management import string_to_csv, csv_to_string
from json_management import string_to_json, json_to_string
from xml_management import string_to_xml, xml_to_string

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