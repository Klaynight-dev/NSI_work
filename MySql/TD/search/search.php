<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "exercice"; // Nom de la base de données
$table = $_POST['table'];
$column = $_POST['column'];
$searchTerm = $_POST['searchTerm'];

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Effectuez la recherche dans la base de données en utilisant une requête SQL
    $stmt = $conn->prepare("SELECT * FROM $table WHERE $column LIKE :searchTerm");
    $searchTerm = "%" . $searchTerm . "%"; // Ajoutez des caractères de joker pour la recherche partielle
    $stmt->bindParam(':searchTerm', $searchTerm, PDO::PARAM_STR);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (count($result) > 0) {
        // Affichez les résultats de la recherche
        echo "<h2>Résultats de la recherche dans la table '$table' (colonne '$column') :</h2>";
        echo "<ul>";
        foreach ($result as $row) {
            echo "<li>Colonne $column : " . $row[$column] . "</li>";
            // Vous pouvez ajouter ici d'autres colonnes à afficher si nécessaire
        }
        echo "</ul>";
    } else {
        echo "<p>Aucun résultat trouvé pour la recherche dans la table '$table' (colonne '$column').</p>";
    }
} catch (PDOException $e) {
    echo "Erreur MySQL : " . $e->getMessage();
}
?>
