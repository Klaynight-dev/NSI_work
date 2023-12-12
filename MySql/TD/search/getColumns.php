<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "exercice"; // Nom de la base de données
$table = $_POST['table'];

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Obtenez la liste des colonnes de la table sélectionnée
    $stmt = $conn->query("DESCRIBE $table");
    $columns = $stmt->fetchAll(PDO::FETCH_COLUMN);

    // Générez les options pour les colonnes
    $options = "";
    foreach ($columns as $column) {
        $options .= "<option value=\"$column\">$column</option>";
    }

    echo $options;
} catch (PDOException $e) {
    echo "Erreur MySQL : " . $e->getMessage();
}
?>
