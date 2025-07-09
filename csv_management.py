import csv
import os
from datetime import datetime


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
    filename = f"data/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(os.path.dirname(__file__), filename)

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
    filepath = os.path.join(os.path.dirname(__file__), filename)
    lines = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(','.join(row))
    return '\n'.join(lines)
