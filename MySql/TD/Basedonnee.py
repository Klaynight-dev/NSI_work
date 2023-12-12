import mysql.connector
import random

def dicocreator(nbr_element):
    # liste de noms de famille et de prenoms fictifs
    noms = ["dupont", "martin", "bernard", "dubois", "thomas", "richard", "petit", "robert", "moreau", "leclerc",
    "durand", "laurent", "simon", "leroy", "roux", "garcia", "lambert", "fontaine", "tremblay", "gauthier",
    "clark", "smith", "johnson", "williams", "jones", "brown", "davis", "miller", "wilson", "moore",
    "anderson", "jackson", "white", "harris", "martinez", "robinson", "clark", "lewis", "walker", "hall",
    "young", "lee", "lopez", "king", "adams", "hill", "scott", "green", "evans", "baker",
    "hall", "wright", "turner", "campbell", "parker", "collins", "stewart", "rogers", "cooper", "bennett",
    "wood", "hughes", "roberts", "james", "phillips", "watson", "brook", "murphy", "gray", "barnes",
    "harrison", "edwards", "price", "bryant", "powell", "kelly", "barker", "elliott", "howard", "gomez",
    "diaz", "davis", "fernandez", "gonzalez", "hernandez", "jimenez", "mendez", "nunez", "perez", "ramirez",
    "reyes", "rivera", "rodriguez", "sanchez", "torres", "velasquez", "alvarez", "gonzales", "pacheco", "cruz",]
    prenoms = ["alice", "bob", "charlie", "david", "emma", "felix", "grace", "harry", "isabelle", "jacob",
    "lily", "mason", "noah", "olivia", "peter", "quinn", "rachel", "samuel", "thomas", "ursula",
    "victor", "william", "xander", "yasmine", "zachary", "adam", "benjamin", "catherine", "daniel",
    "emily", "frank", "gabrielle", "hannah", "ian", "jessica", "kevin", "laura", "matthew", "nora",
    "oliver", "pamela", "quincy", "riley", "sophia", "tristan", "uma", "violet", "wesley", "ximena",
    "yannick", "zara", "aiden", "beth", "caleb", "delilah", "ethan", "fiona", "gavin", "haley",
    "isaac", "julia", "kaden", "lucy", "michael", "nathan", "olivia", "parker", "quinn", "riley",
    "sarah", "tristan", "una", "victoria", "william", "xander", "yasmine", "zane", "amelia",
    "bryce", "chloe", "dylan", "ella", "finley", "gabriel", "hannah", "isaiah", "juliet", "kayla",
    "liam", "maya", "nolan", "olivia", "piper", "quincy", "ryan", "sophia", "tyler", "una",
    "vivian", "willow", "xavier", "yara", "zara"]
    # initialisation du dictionnaire de donnees
    data_dict = {}

    # generer une liste de 150 lignes avec des donnees aleatoires
    for i in range(nbr_element):
        nom = random.choice(noms)
        prenom = random.choice(prenoms)
        age = random.randint(18, 80)  # Âge aleatoire entre 18 et 80 ans
        nom_complet = f"{prenom} {nom}"  # nom complet sous forme de cle
        data_dict[nom_complet] = {"nom": nom, "prenom": prenom, "age": age}  # details de la personne comme valeur

    # maintenant, la variable "data_dict" contient les 150 lignes de donnees sous forme de dictionnaire
    return data_dict

def createBaseDonnee():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Nom de la base de données à créer (changez-le selon vos besoins)
        database_name = str(input("Veuillez Entrer le nom de la base de données à créer : "))

        # Vérifier si la base de données existe déjà
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name not in existing_databases:
            # Créer la base de données si elle n'existe pas déjà
            admin_cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"La base de données '{database_name}' a été créée avec succès.")
        else:
            print(f"La base de données '{database_name}' existe déjà.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()
        
def delBaseDonnee():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Nom de la base de données à créer ou supprimer (changez-le selon vos besoins)
        database_name = str(input("Veuillez entrer le nom de la base de données : "))

        # Vérifier si la base de données existe déjà
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name not in existing_databases:
            # Vous pouvez également ajouter un message ici si vous le souhaitez
            print(f"La base de données '{database_name}' n'existe pas.")
        else:
            # Supprimer la base de données existante
            admin_cursor.execute(f"DROP DATABASE {database_name}")
            print(f"La base de données '{database_name}' a été supprimée avec succès.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()

def createTable():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Nom de la base de données à utiliser
        database_name = input("Veuillez entrer le nom de la base de données : ")

        # Vérifier si la base de données existe
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name in existing_databases:
            admin_cursor.execute(f"USE {database_name}")

            # Nom de la table à créer
            table_name = input("Veuillez entrer le nom de la table à créer : ")

            # Demander les colonnes de la table sous forme de paires nom-colonne: type-colonne
            print("Veuillez entrer les colonnes de la table sous forme de paires nom-colonne:")
            columns_input = input("type-colonne (séparées par des virgules) : ")
            columns_list = columns_input.split(',')

            # Construire la clause CREATE TABLE
            create_table_query = f"CREATE TABLE {table_name} ("
            for column_info in columns_list:
                column_info = column_info.strip()  # Supprimer les espaces inutiles
                create_table_query += f"{column_info}, "
            
            create_table_query = create_table_query.rstrip(', ') + ")"
            
            # Création de la table
            admin_cursor.execute(create_table_query)
            print(f"La table '{table_name}' a été créée avec succès dans la base de données '{database_name}'.")

        else:
            print(f"La base de données '{database_name}' n'existe pas.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()

def deleteTable():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Nom de la base de données à utiliser (changez-le selon vos besoins)
        database_name = input("Veuillez entrer le nom de la base de données : ")

        # Nom de la table à supprimer
        table_name = input("Veuillez entrer le nom de la table à supprimer : ")

        # Suppression de la table de la base de données
        admin_cursor.execute(f"USE {database_name}")
        admin_cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        print(f"Table '{table_name}' supprimée avec succès de la base de données '{database_name}'.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()

def insertIntoTable():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Nom de la base de données à utiliser
        database_name = input("Veuillez entrer le nom de la base de données : ")

        # Vérifier si la base de données existe
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name in existing_databases:
            admin_cursor.execute(f"USE {database_name}")

            # Nom de la table dans laquelle ajouter des valeurs
            table_name = input("Veuillez entrer le nom de la table : ")

            # Demander les valeurs à insérer sous forme de paires nom-colonne: valeur-colonne
            values_input = input("Veuillez entrer les valeurs à insérer sous forme de paires [nom-colonne: valeur-colonne , ...] : ")
            values_list = values_input.split(',')

            # Construire la clause INSERT INTO
            columns = []
            values = []
            for value_info in values_list:
                value_info = value_info.strip()  # Supprimer les espaces inutiles
                column_name, column_value = value_info.split(':')
                columns.append(column_name.strip())
                values.append(column_value.strip())
            
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
            
            # Insérer les valeurs dans la table
            admin_cursor.execute(insert_query, values)
            admin_connection.commit()
            print(f"Les valeurs ont été insérées avec succès dans la table '{table_name}' de la base de données '{database_name}'.")

        else:
            print(f"La base de données '{database_name}' n'existe pas.")

    except mysql.connector.Error as err:
        admin_connection.rollback()  # Annuler les modifications en cas d'erreur
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()

def queryTable():
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Demander le nom de la base de données
        database_name = input("Veuillez entrer le nom de la base de données : ")

        # Vérifier si la base de données existe
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name in existing_databases:
            admin_cursor.execute(f"USE {database_name}")

            # Demander le nom de la table
            table_name = input("Veuillez entrer le nom de la table : ")

            # Vérifier si la table existe
            admin_cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            table_exists = admin_cursor.fetchone()

            if table_exists:
                # Demander le nom de la colonne (ou laisser vide pour obtenir toutes les colonnes)
                column_name = input("Veuillez entrer le nom de la colonne (ou laisser vide pour toutes les colonnes) : ")

                # Demander la valeur de la ligne (ou laisser vide pour obtenir toutes les lignes)
                row_value = input("Veuillez entrer la valeur de la ligne (ou laisser vide pour toutes les lignes) : ")

                # Construire la requête SQL
                if column_name == "":
                    column_name = "*"
                if row_value == "":
                    query = f"SELECT {column_name} FROM {table_name}"
                else:
                    query = f"SELECT {column_name} FROM {table_name} WHERE {row_value}"

                # Exécuter la requête SQL
                admin_cursor.execute(query)
                result = admin_cursor.fetchall()

                if result:
                    # Afficher les résultats
                    for row in result:
                        print(row)
                else:
                    print("Aucun résultat trouvé.")
            else:
                print(f"La table '{table_name}' n'existe pas dans la base de données '{database_name}'.")

        else:
            print(f"La base de données '{database_name}' n'existe pas.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()
        
def insertDataIntoDatabase(data_dict):
    try:
        # Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
        admin_connection = mysql.connector.connect(host="localhost", user="root", password="")

        # Création d'un curseur pour exécuter des requêtes SQL
        admin_cursor = admin_connection.cursor()

        # Demander le nom de la base de données
        database_name = input("Veuillez entrer le nom de la base de données : ")

        # Vérifier si la base de données existe
        admin_cursor.execute("SHOW DATABASES")
        existing_databases = [database[0] for database in admin_cursor]

        if database_name in existing_databases:
            admin_cursor.execute(f"USE {database_name}")

            # Demander le nom de la table
            table_name = input("Veuillez entrer le nom de la table : ")

            # Vérifier si la table existe
            admin_cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            table_exists = admin_cursor.fetchone()

            if table_exists:
                # Insérer les données du dictionnaire dans la table
                for key, value in data_dict.items():
                    nom = value["nom"]
                    prenom = value["prenom"]
                    age = value["age"]
                    insert_query = f"INSERT INTO {table_name} (nom, prenom, age) VALUES ('{nom}', '{prenom}', {age})"
                    admin_cursor.execute(insert_query)
                
                admin_connection.commit()
                print("Les données ont été insérées avec succès dans la table.")

            else:
                print(f"La table '{table_name}' n'existe pas dans la base de données '{database_name}'.")

        else:
            print(f"La base de données '{database_name}' n'existe pas.")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        # Fermer la connexion à l'utilisateur administrateur
        admin_cursor.close()
        admin_connection.close()
        
        


def main():
    choix={1:"Créer une Base de donnée.",
           2:"Supprimer une Base de donnée.",
           3:"Créer une Table dans une Base de donnée demandé.",
           4:"Supprimer une Table dans une Base de donnée demandé.",
           5:"Incrémenter une valeur à une table déjà existante.",
           6:"Verifier si une valeur est dans la table.",
           7:"Incrémenter X élément dans la base de donnée"}
    
    print("Voici vos choix :")
    
    for clé in choix:
        print(f"{clé} : {choix[clé]}")
        
    choice = int(input("Veuillez entrer un choix d'application : "))
    assert choice >= 1, 'Veuillez entrer un nombre supérieur ou égal à 1'

    if choice == 1:
        createBaseDonnee()

    elif choice == 2:
        delBaseDonnee()
    
    elif choice == 3:
        createTable()
    
    elif choice == 4:
        deleteTable()
        
    elif choice == 5:
        insertIntoTable()
    
    elif choice==6:
        queryTable()
        
    elif choice==7:
        nbr_element=int(input("Veuillez entrer le nombre d'élément que vous voulez ajouter : "))
        assert nbr_element<=100000, "Vous ne pouvez pas mettre un nombre supérieur à 200 comme élément à ajouter"
        insertDataIntoDatabase(dicocreator(nbr_element))
        
    else:
        print("Veuillez spécifier un choix de fonction qui existe.")

if __name__ == "__main__":
    main()
