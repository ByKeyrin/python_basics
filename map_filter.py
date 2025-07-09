# Fonction utilisant map : multiplie chaque élément d'une liste par 2

def double_liste(liste):
    return list(map(lambda x: x * 2, liste))

# Fonction utilisant filter : garde les éléments pairs d'une liste

def filtre_pairs(liste):
    return list(filter(lambda x: x % 2 == 0, liste))
