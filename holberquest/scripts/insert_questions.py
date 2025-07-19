from app import app, db
from app.models.quest import Quest

questions = questions = [
    {
        "question": "Quel est le résultat de print(3 * 2) en Python ?",
        "reponses": ["6", "32", "5"],
        "bonne_reponse": "6",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "Que fait la fonction printf(\"%d\", 10); en C ?",
        "reponses": ["Affiche 10", "Affiche %d", "Erreur"],
        "bonne_reponse": "Affiche 10",
        "difficulte": "facile",
        "langage": "c",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "Quel est le résultat de console.log(2 + '2') en JavaScript ?",
        "reponses": ["22", "4", "NaN"],
        "bonne_reponse": "22",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, que retourne len([1,2,3]) ?",
        "reponses": ["3", "2", "1"],
        "bonne_reponse": "3",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, quel type de variable pour stocker un caractère ?",
        "reponses": ["char", "int", "float"],
        "bonne_reponse": "char",
        "difficulte": "facile",
        "langage": "c",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "Quel est le résultat de typeof null en JavaScript ?",
        "reponses": ["object", "null", "undefined"],
        "bonne_reponse": "object",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, que fait la méthode .append() sur une liste ?",
        "reponses": ["Ajoute un élément", "Supprime un élément", "Trie la liste"],
        "bonne_reponse": "Ajoute un élément",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, quelle est la valeur initiale d'une variable non initialisée ?",
        "reponses": ["Indéfinie", "0", "NULL"],
        "bonne_reponse": "Indéfinie",
        "difficulte": "facile",
        "langage": "c",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "Quel est le résultat de 1 == '1' en JavaScript ?",
        "reponses": ["false", "true", "undefined"],
        "bonne_reponse": "false",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, que fait range(5) ?",
        "reponses": ["Crée un itérable de 0 à 4", "Crée une liste de 1 à 5", "Crée un tuple"],
        "bonne_reponse": "Crée un itérable de 0 à 4",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, que fait la fonction malloc ?",
        "reponses": ["Alloue de la mémoire", "Libère de la mémoire", "Copie une chaîne"],
        "bonne_reponse": "Alloue de la mémoire",
        "difficulte": "moyen",
        "langage": "c",
        "xp_gagne": 15,
        "xp_perdu": 5
    },
    {
        "question": "Quel est le résultat de [1,2,3].length en JavaScript ?",
        "reponses": ["3", "2", "undefined"],
        "bonne_reponse": "3",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, comment convertir une chaîne en entier ?",
        "reponses": ["int('123')", "str(123)", "float('123')"],
        "bonne_reponse": "int('123')",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, que fait la fonction free ?",
        "reponses": ["Libère de la mémoire", "Alloue de la mémoire", "Affiche une chaîne"],
        "bonne_reponse": "Libère de la mémoire",
        "difficulte": "moyen",
        "langage": "c",
        "xp_gagne": 15,
        "xp_perdu": 5
    },
    {
        "question": "Quel est le résultat de 'Hello'.toUpperCase() en JavaScript ?",
        "reponses": ["HELLO", "hello", "Hello"],
        "bonne_reponse": "HELLO",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, que fait la méthode .split() sur une chaîne ?",
        "reponses": ["Découpe la chaîne", "Concatène la chaîne", "Inverse la chaîne"],
        "bonne_reponse": "Découpe la chaîne",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, quel opérateur permet d'accéder à la valeur pointée ?",
        "reponses": ["*", "&", "%"],
        "bonne_reponse": "*",
        "difficulte": "moyen",
        "langage": "c",
        "xp_gagne": 15,
        "xp_perdu": 5
    },
    {
        "question": "Quel est le résultat de typeof undefined en JavaScript ?",
        "reponses": ["undefined", "object", "null"],
        "bonne_reponse": "undefined",
        "difficulte": "facile",
        "langage": "javascript",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En Python, que fait la méthode .pop() sur une liste ?",
        "reponses": ["Retire le dernier élément", "Ajoute un élément", "Trie la liste"],
        "bonne_reponse": "Retire le dernier élément",
        "difficulte": "facile",
        "langage": "python",
        "xp_gagne": 10,
        "xp_perdu": 2
    },
    {
        "question": "En C, que fait la fonction strcpy ?",
        "reponses": ["Copie une chaîne", "Compare deux chaînes", "Affiche une chaîne"],
        "bonne_reponse": "Copie une chaîne",
        "difficulte": "moyen",
        "langage": "c",
        "xp_gagne": 15,
        "xp_perdu": 5
    }
]

with app.app_context():
    for q in questions:
        quest = Quest(
            question=q["question"],
            reponses=q["reponses"],
            bonne_reponse=q["bonne_reponse"],
            difficulte=q["difficulte"],
            xp_gagne=q["xp_gagne"],
            xp_perdu=q["xp_perdu"]
        )
        db.session.add(quest)
    db.session.commit()
    print("Questions ajoutées !")