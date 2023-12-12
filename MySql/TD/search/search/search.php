<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "exercice"; // Nom de la base de données
$table = $_POST['table']; // Table sélectionnée depuis le menu déroulant
$columns = isset($_POST['columns']) ? $_POST['columns'] : array(); // Colonnes sélectionnées depuis les cases à cocher
$searchTerm = $_POST['searchTerm']; // Terme de recherche

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Créez la partie SELECT de la requête SQL en fonction des colonnes sélectionnées
    $selectColumns = empty($columns) ? "*" : implode(", ", $columns);

    // Effectuez la recherche dans la base de données en utilisant la requête SQL
    $stmt = $conn->prepare("SELECT $selectColumns FROM $table WHERE");
    $searchTerms = explode(" ", $searchTerm); // Divisez le terme de recherche en mots
    $conditions = array();
    foreach ($searchTerms as $term) {
        $term = "%" . $term . "%"; // Ajoutez des caractères de joker pour la recherche partielle
        $conditions[] = "(" . implode(" OR ", array_map(function ($col) use ($term) {
            return "$col LIKE ?";
        }, $columns)) . ")";
    }
    $stmt->bindValue(1, implode(" AND ", $conditions), PDO::PARAM_STR);
    foreach ($searchTerms as $term) {
        foreach ($columns as $colIdx => $col) {
            $stmt->bindValue(($colIdx + 2), $term, PDO::PARAM_STR);
        }
    }

    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (count($result) > 0) {
        // Affichez les résultats de la recherche sous forme de tableau Excel
        echo "<table border='1'>";
        echo "<thead>";
        echo "<tr>";
        foreach ($columns as $col) {
            echo "<th>$col</th>";
        }
        echo "</tr>";
        echo "</thead>";
        echo "<tbody>";
        foreach ($result as $row) {
            echo "<tr>";
            foreach ($columns as $col) {
                echo "<td>" . $row[$col] . "</td>";
            }
            echo "</tr>";
        }
        echo "</tbody>";
        echo "</table>";
    } else {
        echo "<p>Aucun résultat trouvé pour la recherche dans la table '$table'.</p>";
    }
} catch (PDOException $e) {
    echo "Erreur MySQL : " . $e->getMessage();
}
?>
