import csv
import os
from datetime import datetime

# Utilisation du chemin absolu du dossier parent du projet pour le dossier data
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')


def string_to_csv(data: str) -> str:
    """
    Prend une chaîne de caractères, la transforme en fichier CSV et retourne le nom du fichier créé.
    Chaque ligne de la chaîne correspond à une ligne du CSV, les valeurs sont séparées par des virgules.
    Le fichier est créé dans le même dossier que ce script.

    Args:
        data (str): La chaîne à transformer (lignes séparées par '\n', colonnes par ',').

    Returns:
        str: Le nom du fichier CSV créé.
    """
    # Générer un nom de fichier unique
    filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(DATA_DIR, filename)

    # Séparer les lignes et colonnes
    lines = data.strip().split('\n')
    rows = [line.split(',') for line in lines]

    # Écrire dans le fichier CSV
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    return filename


def csv_to_string(filename: str) -> str:
    """
    Prend un fichier CSV en paramètre et retourne son contenu sous forme de chaîne de caractères.
    Chaque ligne du CSV devient une ligne de la chaîne, les valeurs sont séparées par des virgules.

    Args:
        filename (str): Le nom du fichier CSV à lire.

    Returns:
        str: Le contenu du fichier sous forme de chaîne de caractères.
    """
    filepath = os.path.join(DATA_DIR, filename)
    lines = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(','.join(row))
    return '\n'.join(lines)


def string_to_csv_dict(data: str) -> str:
    """
    Prend une chaîne de caractères CSV avec en-tête, la transforme en fichier CSV via DictWriter et retourne le nom du fichier créé.
    """
    filename = f"output_dict_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(DATA_DIR, filename)
    lines = data.strip().split('\n')
    reader = csv.DictReader(lines)
    fieldnames = reader.fieldnames
    rows = list(reader)
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return filename


def csv_to_string_dict(filename: str) -> str:
    """
    Prend un fichier CSV en paramètre et retourne son contenu sous forme de liste de dictionnaires (via DictReader).
    """
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return str([row for row in reader])
