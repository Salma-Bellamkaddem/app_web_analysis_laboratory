# Gestion et Analyse des Laboratoires - Application OCP

**Description**  
Ce projet est une application web développée dans le cadre d’un stage de fin d’études réalisé à l’Office Chérifien des Phosphates (OCP). L'objectif est d'optimiser la gestion des analyses de laboratoire pour les engrais produits par l'OCP.

---

## Fonctionnalités principales
- **Gestion des échantillons** : Suivi des échantillons avec traçabilité complète.
- **Analyse des produits** : Suivi des analyses réalisées par les laboratoires internes et externes.
- **Gestion des utilisateurs** : Administration des rôles et permissions pour les laborantins, chefs de laboratoire, etc.
- **Rapports et tableaux de bord** : Génération de rapports et visualisation des statistiques.

---

## Technologies utilisées

### Backend
- **Python** avec le framework **Django**
- **MySQL** pour la base de données

### Frontend
- **HTML/CSS** : Structuration et mise en forme des pages
- **Bootstrap** : Interface utilisateur réactive
- **JavaScript** : Interaction utilisateur dynamique

---

## Captures d'écran

### Fenêtre d'authentification
![Fenêtre d'authentification](images/fenetre_authentification.png)

### Tableau de bord du chef de laboratoire
![Tableau de bord](images/tableau_bord_chef.png)

### Gestion des échantillons
![Gestion des échantillons](images/gestion_echantillons.png)

### Rapport d'analyse
![Rapport d'analyse](images/rapport_analyse.png)

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/username/ocp-laboratoire.git
   ```

2. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez la base de données dans `settings.py`.

4. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

6. Accédez à l'application via `http://127.0.0.1:8000/`.

---

## Auteur
**Salma Bellamkaddem**  
Projet réalisé dans le cadre d’un stage de fin d’année à l’OCP (2022/2023).

---

## Contributions
Les contributions sont les bienvenues ! N'hésitez pas à soumettre une issue ou une pull request pour améliorer le projet.

---

## Licence
Ce projet est sous licence [MIT](LICENSE).
