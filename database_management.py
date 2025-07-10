import sqlite3

class SimpleDatabase:
    """
    Classe simple pour illustrer l'utilisation de sqlite3 en Python.
    Permet de créer une table, d'insérer et de lire des personnes (nom, âge).
    La base est stockée dans le dossier data/.
    """
    def __init__(self, db_name="data/simple.db"):
        """
        Initialise la connexion à la base et crée la table si besoin.
        Args:
            db_name (str): Chemin du fichier de base de données.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """
        Crée la table 'personnes' si elle n'existe pas.
        """
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS personnes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            ''')

    def insert_personne(self, nom, age):
        """
        Insère une personne dans la table.
        Args:
            nom (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        with self.conn:
            self.conn.execute(
                "INSERT INTO personnes (nom, age) VALUES (?, ?)", (nom, age)
            )

    def get_all_personnes(self):
        """
        Retourne toutes les personnes sous forme de liste de tuples (nom, age).
        Returns:
            list: Liste de tuples (nom, age)
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT nom, age FROM personnes")
        return cursor.fetchall()

    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

if __name__ == "__main__":
    db = SimpleDatabase()
    db.insert_personne("Alice", 30)
    db.insert_personne("Bob", 25)
    print("Toutes les personnes dans la base :", db.get_all_personnes())
    db.close()
