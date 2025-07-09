import json
import os
from datetime import datetime

def string_to_json(data: str) -> str:
    """
    Prend une chaîne de caractères représentant un objet ou une liste JSON,
    la transforme en fichier .json et retourne le nom du fichier créé.
    Le fichier est créé dans le même dossier que ce script.

    Args:
        data (str): La chaîne JSON à écrire dans le fichier.

    Returns:
        str: Le nom du fichier JSON créé.
    """
    filename = f"data/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    # Charger pour valider le JSON
    obj = json.loads(data)
    with open(filepath, mode='w', encoding='utf-8') as jsonfile:
        json.dump(obj, jsonfile, ensure_ascii=False, indent=2)
    return filename

def json_to_string(filename: str) -> str:
    """
    Prend un fichier JSON en paramètre et retourne son contenu sous forme de chaîne de caractères.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        str: Le contenu du fichier sous forme de chaîne de caractères.
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, mode='r', encoding='utf-8') as jsonfile:
        obj = json.load(jsonfile)
    return json.dumps(obj, ensure_ascii=False, indent=2)
