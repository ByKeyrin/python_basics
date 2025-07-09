import os
from datetime import datetime
import xml.etree.ElementTree as ET

def string_to_xml(data: str) -> str:
    """
    Prend une chaîne de caractères représentant un document XML,
    la transforme en fichier .xml et retourne le nom du fichier créé.
    Le fichier est créé dans le même dossier que ce script.

    Args:
        data (str): La chaîne XML à écrire dans le fichier.

    Returns:
        str: Le nom du fichier XML créé.
    """
    filename = f"data/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    # Valider le XML
    ET.fromstring(data)
    with open(filepath, mode='w', encoding='utf-8') as xmlfile:
        xmlfile.write(data)
    return filename

def xml_to_string(filename: str) -> str:
    """
    Prend un fichier XML en paramètre et retourne son contenu sous forme de chaîne de caractères.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        str: Le contenu du fichier sous forme de chaîne de caractères.
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, mode='r', encoding='utf-8') as xmlfile:
        return xmlfile.read()
