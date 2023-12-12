<?php
if (isset($_POST['database'])) {
    $database = $_POST['database'];

    // Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
    $connection = mysqli_connect("localhost", "root", "");

    if (!$connection) {
        die("Erreur de connexion à MySQL : " . mysqli_connect_error());
    }

    // Sélection de la base de données spécifiée
    if (!mysqli_select_db($connection, $database)) {
        die("Erreur lors de la sélection de la base de données : " . mysqli_error($connection));
    }

    // Requête pour obtenir la liste des tables dans la base de données spécifiée
    $query = "SHOW TABLES";
    $result = mysqli_query($connection, $query);

    if (!$result) {
        die("Erreur lors de l'exécution de la requête : " . mysqli_error($connection));
    }

    // Créez une liste déroulante HTML avec les tables
    echo '<option value="">Sélectionner une table</option>';
    while ($row = mysqli_fetch_row($result)) {
        echo '<option value="' . $row[0] . '">' . $row[0] . '</option>';
    }

    // Fermez la connexion à MySQL
    mysqli_close($connection);
}
?>
