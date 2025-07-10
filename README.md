# Python Basics – Gestion de fichiers et base de données

Bienvenue dans ce projet pédagogique illustrant les bases de la manipulation de fichiers (CSV, JSON, XML), l'utilisation de fonctions Python courantes (`map`, `filter`) et l'accès à une base de données SQLite.

## 📁 Architecture du projet

```
python_basics/
│
├── app.py                  # Point d'entrée principal, tous les exemples
├── data/                   # Dossier pour les fichiers générés (CSV, JSON, XML, base SQLite)
└── modules/                # Tous les modules Python du projet
    ├── csv_management.py
    ├── json_management.py
    ├── xml_management.py
    ├── map_filter.py
    ├── database_management.py
    └── __init__.py
```

## 🚀 Fonctionnalités principales

- **CSV** : Création et lecture de fichiers CSV (avec `csv.writer`, `csv.DictWriter`, etc.)
- **JSON** : Création et lecture de fichiers JSON
- **XML** : Création et lecture de fichiers XML
- **map/filter** : Exemples simples d'utilisation de `map` et `filter`
- **SQLite** : Exemple de base de données simple avec insertion et lecture

## 📝 Exécution

Lancez simplement le fichier principal :

```bash
python app.py
```

Vous verrez s'afficher dans la console :
- La création et la lecture de fichiers CSV, JSON, XML
- L'utilisation de `map` et `filter` sur une liste
- L'insertion et la lecture de données dans une base SQLite

## ✨ Extrait de code (app.py)

```python
from modules.csv_management import string_to_csv, csv_to_string
from modules.json_management import string_to_json, json_to_string
from modules.xml_management import string_to_xml, xml_to_string
from modules.map_filter import double_liste, filtre_pairs
from modules.database_management import SimpleDatabase

if __name__ == "__main__":
    # ...
    db = SimpleDatabase()
    db.insert_personne("Alice", 30)
    db.insert_personne("Bob", 25)
    print("Toutes les personnes dans la base :", db.get_all_personnes())
    db.close()
```

## 📦 Prérequis
- Python 3.8+
- Aucun package externe requis (tout est basé sur la bibliothèque standard)

## 🤝 Contribuer
Ce projet est conçu pour l'apprentissage. N'hésitez pas à proposer des améliorations ou à l'utiliser comme base pour vos propres exercices !

---
**Auteur :** ByKeyrin
