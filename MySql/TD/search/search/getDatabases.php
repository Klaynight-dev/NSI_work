<?php
// Connexion à MySQL en utilisant les informations de connexion de l'administrateur (root)
$connection = mysqli_connect("localhost", "root", "");

if (!$connection) {
    die("Erreur de connexion à MySQL : " . mysqli_connect_error());
}

// Requête pour obtenir la liste des bases de données
$query = "SHOW DATABASES";
$result = mysqli_query($connection, $query);

if (!$result) {
    die("Erreur lors de l'exécution de la requête : " . mysqli_error($connection));
}

// Créez une liste déroulante HTML avec les bases de données
echo '<option value="">Sélectionner une base de données</option>';
while ($row = mysqli_fetch_assoc($result)) {
    echo '<option value="' . $row['Database'] . '">' . $row['Database'] . '</option>';
}

// Fermez la connexion à MySQL
mysqli_close($connection);
?>
