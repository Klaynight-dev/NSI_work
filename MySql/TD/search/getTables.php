<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "exercice"; // Nom de la base de données

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Obtenez la liste des tables dans la base de données
    $stmt = $conn->query("SHOW TABLES");
    $tables = $stmt->fetchAll(PDO::FETCH_COLUMN);

    // Générez les options pour les tables
    $options = "";
    foreach ($tables as $table) {
        $options .= "<option value=\"$table\">$table</option>";
    }

    echo $options;
} catch (PDOException $e) {
    echo "Erreur MySQL : " . $e->getMessage();
}
?>
