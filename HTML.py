<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Site Web</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Bienvenue sur mon site web !</h1>
        <nav>
            <ul>
                <li><a href="#about">À propos</a></li>
                <li><a href="#projects">Projets</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>À propos de moi</h2>
        <p>Je suis un développeur passionné par la création de sites web modernes et interactifs.</p>
    </section>

    <section id="projects">
        <h2>Mes Projets</h2>
        <ul>
            <li>Projet 1</li>
            <li>Projet 2</li>
            <li>Projet 3</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Me contacter</h2>
        <form>
            <label for="name">Nom :</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email :</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message :</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Envoyer</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 Mon Site Web. Tous droits réservés.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
