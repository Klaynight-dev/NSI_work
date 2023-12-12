<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "exercice"; // Remplacez par le nom de votre base de données

$action = $_POST['action'];

if ($action == 'createDatabase') {
    // Code pour créer la base de données
    try {
        $conn = new PDO("mysql:host=$servername", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "CREATE DATABASE IF NOT EXISTS $database";
        $conn->exec($sql);
        echo "La base de données a été créée avec succès.";
    } catch (PDOException $e) {
        echo "Erreur MySQL : " . $e->getMessage();
    }
} elseif ($action == 'insertData') {
    // Code pour insérer des données dans la table
    try {
        $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        // Remplacez cette partie par la logique d'insertion des données
        $stmt = $conn->prepare("INSERT INTO votre_table (nom, prenom, age) VALUES (:nom, :prenom, :age)");
        $stmt->bindParam(':nom', $nom);
        $stmt->bindParam(':prenom', $prenom);
        $stmt->bindParam(':age', $age);

        // Exemple d'insertion de données
        $nom = "Dupont";
        $prenom = "Alice";
        $age = 30;
        $stmt->execute();

        echo "Les données ont été insérées avec succès.";
    } catch (PDOException $e) {
        echo "Erreur MySQL : " . $e->getMessage();
    }
}

// Implémentez d'autres actions (comme la suppression de la base de données, la création de tables, etc.) de manière similaire.
?>