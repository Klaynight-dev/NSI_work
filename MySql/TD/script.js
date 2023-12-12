// script.js
document.addEventListener('DOMContentLoaded', () => {
    const outputSection = document.getElementById('output');
    const createDBLink = document.getElementById('createDB');
    const deleteDBLink = document.getElementById('deleteDB');
    const createTableLink = document.getElementById('createTable');
    const deleteTableLink = document.getElementById('deleteTable');
    const insertDataLink = document.getElementById('insertData');
    const queryDataLink = document.getElementById('queryData');
    const insertMultipleLink = document.getElementById('insertMultiple');

function clearOutput() {
    outputSection.innerHTML = '';
}

createDBLink.addEventListener('click', (e) => {
    e.preventDefault();
    createBaseDonnee();
    clearOutput();
});

deleteDBLink.addEventListener('click', (e) => {
    e.preventDefault();
    delBaseDonnee();
    clearOutput();
});

createTableLink.addEventListener('click', (e) => {
    e.preventDefault();
    createTable();
    clearOutput();
});

deleteTableLink.addEventListener('click', (e) => {
    e.preventDefault();
    deleteTable();
    clearOutput();
});

insertDataLink.addEventListener('click', (e) => {
    e.preventDefault();
    insertIntoTable();
    clearOutput();
});

queryDataLink.addEventListener('click', (e) => {
    e.preventDefault();
    queryTable();
    clearOutput();
});

insertMultipleLink.addEventListener('click', (e) => {
    e.preventDefault();
    const nbr_element = prompt("Veuillez entrer le nombre d'élément que vous voulez ajouter :");
    if (nbr_element !== null) {
        if (isNaN(nbr_element) || nbr_element <= 0) {
            alert("Veuillez entrer un nombre valide supérieur à zéro.");
        } else {
            insertDataIntoDatabase(dicocreator(parseInt(nbr_element)));
            clearOutput();
        }
    }
});

const mysql = require('mysql');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: ''
});

connection.connect((err) => {
    if (err) {
        console.error('Erreur MySQL : ' + err.message);
    } else {
        console.log('Connecté à MySQL');
        main();
    }
});

function dicocreator(nbr_element) {
    const noms = ["dupont", "martin", "bernard", "dubois", "thomas", "richard", "petit", "robert", "moreau", "leclerc", "durand", "laurent", "simon", "leroy", "roux", "garcia", "lambert", "fontaine", "tremblay", "gauthier", "clark", "smith", "johnson", "williams", "jones", "brown", "davis", "miller", "wilson", "moore", "anderson", "jackson", "white", "harris", "martinez", "robinson", "clark", "lewis", "walker", "hall", "young", "lee", "lopez", "king", "adams", "hill", "scott", "green", "evans", "baker", "hall", "wright", "turner", "campbell", "parker", "collins", "stewart", "rogers", "cooper", "bennett", "wood", "hughes", "roberts", "james", "phillips", "watson", "brook", "murphy", "gray", "barnes", "harrison", "edwards", "price", "bryant", "powell", "kelly", "barker", "elliott", "howard", "gomez", "diaz", "davis", "fernandez", "gonzalez", "hernandez", "jimenez", "mendez", "nunez", "perez", "ramirez", "reyes", "rivera", "rodriguez", "sanchez", "torres", "velasquez", "alvarez", "gonzales", "pacheco", "cruz"];
    const prenoms = ["alice", "bob", "charlie", "david", "emma", "felix", "grace", "harry", "isabelle", "jacob", "lily", "mason", "noah", "olivia", "peter", "quinn", "rachel", "samuel", "thomas", "ursula", "victor", "william", "xander", "yasmine", "zachary", "adam", "benjamin", "catherine", "daniel", "emily", "frank", "gabrielle", "hannah", "ian", "jessica", "kevin", "laura", "matthew", "nora", "oliver", "pamela", "quincy", "riley", "sophia", "tristan", "uma", "violet", "wesley", "ximena", "yannick", "zara", "aiden", "beth", "caleb", "delilah", "ethan", "fiona", "gavin", "haley", "isaac", "julia", "kaden", "lucy", "michael", "nathan", "olivia", "parker", "quinn", "riley", "sarah", "tristan", "una", "victoria", "willow", "xavier", "yara", "zara"];
    const data_dict = {};

    for (let i = 0; i < nbr_element; i++) {
        const nom = noms[Math.floor(Math.random() * noms.length)];
        const prenom = prenoms[Math.floor(Math.random() * prenoms.length)];
        const age = Math.floor(Math.random() * 63) + 18; // Âge aléatoire entre 18 et 80 ans
        const nom_complet = `${prenom} ${nom}`;
        data_dict[nom_complet] = { nom: nom, prenom: prenom, age: age };
    }

    return data_dict;
}

function createBaseDonnee() {
    rl.question('Veuillez entrer le nom de la base de données à créer : ', (databaseName) => {
        connection.query('CREATE DATABASE IF NOT EXISTS ??', [databaseName], (err) => {
            if (err) {
                console.error('Erreur MySQL : ' + err.message);
            } else {
                console.log(`La base de données '${databaseName}' a été créée avec succès.`);
                main();
            }
        });
    });
}

function delBaseDonnee() {
    rl.question('Veuillez entrer le nom de la base de données à supprimer : ', (databaseName) => {
        connection.query('DROP DATABASE IF EXISTS ??', [databaseName], (err) => {
            if (err) {
                console.error('Erreur MySQL : ' + err.message);
            } else {
                console.log(`La base de données '${databaseName}' a été supprimée avec succès.`);
                main();
            }
        });
    });
}

function createTable() {
    rl.question('Veuillez entrer le nom de la base de données : ', (databaseName) => {
        rl.question('Veuillez entrer le nom de la table à créer : ', (tableName) => {
            rl.question('Veuillez entrer les colonnes de la table sous forme de paires nom-colonne: type-colonne (séparées par des virgules) : ', (columnsInput) => {
                const columnsList = columnsInput.split(',').map(columnInfo => columnInfo.trim());
                const createTableQuery = `CREATE TABLE IF NOT EXISTS ${tableName} (${columnsList.join(', ')})`;
                connection.query(`USE ??`, [databaseName], (err) => {
                    if (err) {
                        console.error('Erreur MySQL : ' + err.message);
                    } else {
                        connection.query(createTableQuery, (err) => {
                            if (err) {
                                console.error('Erreur MySQL : ' + err.message);
                            } else {
                                console.log(`La table '${tableName}' a été créée avec succès dans la base de données '${databaseName}'.`);
                            }
                            main();
                        });
                    }
                });
            });
        });
    });
}

function deleteTable() {
    rl.question('Veuillez entrer le nom de la base de données : ', (databaseName) => {
        rl.question('Veuillez entrer le nom de la table à supprimer : ', (tableName) => {
            const deleteTableQuery = `DROP TABLE IF EXISTS ${tableName}`;
            connection.query(`USE ??`, [databaseName], (err) => {
                if (err) {
                    console.error('Erreur MySQL : ' + err.message);
                } else {
                    connection.query(deleteTableQuery, (err) => {
                        if (err) {
                            console.error('Erreur MySQL : ' + err.message);
                        } else {
                            console.log(`La table '${tableName}' a été supprimée avec succès de la base de données '${databaseName}'.`);
                        }
                        main();
                    });
                }
            });
        });
    });
}

function insertIntoTable() {
    rl.question('Veuillez entrer le nom de la base de données : ', (databaseName) => {
        rl.question('Veuillez entrer le nom de la table : ', (tableName) => {
            rl.question('Veuillez entrer les valeurs à insérer sous forme de paires nom-colonne: valeur-colonne (séparées par des virgules) : ', (valuesInput) => {
                const valuesList = valuesInput.split(',').map(valueInfo => valueInfo.trim());
                const columns = [];
                const values = [];
                valuesList.forEach((valueInfo) => {
                    const [columnName, columnValue] = valueInfo.split(':').map(value => value.trim());
                    columns.push(columnName);
                    values.push(columnValue);
                });
                const insertQuery = `INSERT INTO ${tableName} (${columns.join(', ')}) VALUES ?`;
                connection.query(`USE ??`, [databaseName], (err) => {
                    if (err) {
                        console.error('Erreur MySQL : ' + err.message);
                    } else {
                        connection.query(insertQuery, [[values]], (err) => {
                            if (err) {
                                console.error('Erreur MySQL : ' + err.message);
                            } else {
                                console.log(`Les valeurs ont été insérées avec succès dans la table '${tableName}' de la base de données '${databaseName}'.`);
                            }
                            main();
                        });
                    }
                });
            });
        });
    });
}

function queryTable() {
    rl.question('Veuillez entrer le nom de la base de données : ', (databaseName) => {
        rl.question('Veuillez entrer le nom de la table : ', (tableName) => {
            rl.question('Veuillez entrer le nom de la colonne (ou laisser vide pour toutes les colonnes) : ', (columnName) => {
                rl.question('Veuillez entrer la valeur de la ligne (ou laisser vide pour toutes les lignes) : ', (rowValue) => {
                    const selectQuery = `SELECT ${columnName || '*'} FROM ${tableName} ${rowValue ? `WHERE ${rowValue}` : ''}`;
                    connection.query(`USE ??`, [databaseName], (err) => {
                        if (err) {
                            console.error('Erreur MySQL : ' + err.message);
                        } else {
                            connection.query(selectQuery, (err, result) => {
                                if (err) {
                                    console.error('Erreur MySQL : ' + err.message);
                                } else {
                                    if (result.length > 0) {
                                        console.log('Résultat de la requête :');
                                        result.forEach((row) => {
                                            console.log(row);
                                        });
                                    } else {
                                        console.log('Aucun résultat trouvé.');
                                    }
                                }
                                main();
                            });
                        }
                    });
                });
            });
        });
    });
}

function insertDataIntoDatabase(data_dict) {
    rl.question('Veuillez entrer le nom de la base de données : ', (databaseName) => {
        rl.question('Veuillez entrer le nom de la table : ', (tableName) => {
            connection.query(`USE ??`, [databaseName], (err) => {
                if (err) {
                    console.error('Erreur MySQL : ' + err.message);
                    main();
                } else {
                    const keys = Object.keys(data_dict);
                    const insertQueries = keys.map((key) => {
                        const { nom, prenom, age } = data_dict[key];
                        return `INSERT INTO ${tableName} (nom, prenom, age) VALUES ('${nom}', '${prenom}', ${age})`;
                    });
                    connection.query(insertQueries.join('; '), (err) => {
                        if (err) {
                            console.error('Erreur MySQL : ' + err.message);
                        } else {
                            console.log('Les données ont été insérées avec succès dans la table.');
                        }
                        main();
                    });
                }
            });
        });
    });
}

function main() {
    const choix = {
        1: "Créer une Base de donnée.",
        2: "Supprimer une Base de donnée.",
        3: "Créer une Table dans une Base de donnée demandée.",
        4: "Supprimer une Table dans une Base de donnée demandée.",
        5: "Incrémenter une valeur à une table déjà existante.",
        6: "Vérifier si une valeur est dans la table.",
        7: "Incrémenter X éléments dans la base de donnée"
    };

    console.log("Voici vos choix :");

    for (const key in choix) {
        console.log(`${key}: ${choix[key]}`);
    }

    rl.question('Veuillez entrer un choix d\'application : ', (choice) => {
        choice = parseInt(choice);
        if (choice === 1) {
            createBaseDonnee();
        } else if (choice === 2) {
            delBaseDonnee();
        } else if (choice === 3) {
            createTable();
        } else if (choice === 4) {
            deleteTable();
        } else if (choice === 5) {
            insertIntoTable();
        } else if (choice === 6) {
            queryTable();
        } else if (choice === 7) {
            rl.question('Veuillez entrer le nombre d\'éléments que vous voulez ajouter : ', (nbr_element) => {
                nbr_element = parseInt(nbr_element);
                if (nbr_element <= 100000) {
                    insertDataIntoDatabase(dicocreator(nbr_element));
                } else {
                    console.log('Vous ne pouvez pas ajouter plus de 100 000 éléments.');
                    main();
                }
            });
        } else {
            console.log("Veuillez spécifier un choix de fonction qui existe.");
            main();
        }
    });
}