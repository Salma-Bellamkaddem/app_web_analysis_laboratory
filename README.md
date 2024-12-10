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
![2REgister](https://github.com/user-attachments/assets/e4aa2ec6-8364-422f-8b4d-cd3648b21aae)
![3forgetpass](https://github.com/user-attachments/assets/7170fb17-47ed-4ea0-a5fe-d288478d1263)

![create account](https://github.com/user-attachments/assets/5c6731f7-bbda-46e8-8cb8-aea67eb4b10d)

### Tableau de bord du chef de laboratoire
![Tableau de bord]![4dashbord](https://github.com/user-attachments/assets/72594901-d0c7-40ef-952b-5ecfb7062e7d)


### Gestion des échantillons
![Gestion des échantillons](images/gestion_echantillons.png)

### Rapport d'analyse
![Rapport d'analyse]![rapport dessai](https://github.com/user-attachments/assets/98045e66-6012-460c-85b6-4547b6f40e45)
nouveaux utilisateurs d'accéder à notre plateforme.
![image](https://github.com/user-attachments/assets/f7eaf651-dd7f-461a-8bc8-0ff92371f33e)

Figure 11Register Account


a.	Connexion :

Notre système de connexion sécurisé garantit que les utilisateurs enregistrés peuvent accéder rapidement à leur compte en saisissant leurs informations d'identification. Nous avons mis en œuvre des mécanismes de sécurité robustes pour protéger les données sensibles des utilisateurs.
 

 ![image](https://github.com/user-attachments/assets/054cbf6d-d907-4f18-a00c-c54c8ade252f)

Figure 12interface connecter

b.	Envoi d'E-mails :

L'envoi d'e-mails est intégré à plusieurs étapes de l'application, notamment pour la confirmation d'inscription, la réinitialisation de mot de passe et d'autres communications importantes avec les utilisateurs. Nous avons utilisé des protocoles sécurisés pour garantir que les e-mails sont livrés de manière fiable.
 

 
Figure 13interface envoyer email

![image](https://github.com/user-attachments/assets/365f999e-3443-4423-9a0d-10af17c48715)



Figure 14interface reset sent

4. initialisation de Mot de Passe :

En cas d'oubli de mot de passe, notre application propose une fonction de réinitialisation de mot de passe qui permet aux utilisateurs de créer un nouveau mot de passe en suivant un processus sécurisé. Cela garantit que les utilisateurs ne sont jamais bloqués hors de leur compte.

 

 
Figure 15:Interface new password



![image](https://github.com/user-attachments/assets/84a27271-533d-4647-b335-91f172b5b6a4)




2.	L’interface destinée aux laborantins :


![image](https://github.com/user-attachments/assets/1938fefc-36ca-4dd8-b383-9051889316b4)

L'interface réservée aux laborantins dans notre application représente un élément central de notre solution de gestion et d'analyse des produits au laboratoire de l'OCP. Conçue pour simplifier et optimiser les tâches quotidiennes des professionnels de laboratoire, cette interface offre un ensemble de fonctionnalités essentielles visant à améliorer l'efficacité, la précision et la traçabilité des analyses. Dans cette section, nous explorerons en détail deux aspects cruciaux de cette interface : l'ajout d'analyses et la modification de profils d'utilisateurs.
Ajout d'Analyses :
Le processus d'ajout d'analyses est au cœur de notre application. Il permet aux laborantins d'enregistrer, de suivre et de documenter chaque analyse effectuée sur les produits chimiques et agricoles. Cette fonctionnalité offre une approche simplifiée et structurée pour la création de bulletins d'analyse complets, garantissant une traçabilité totale depuis la réception des échantillons jusqu'à la génération de rapports détaillés. Nous explorerons les étapes du processus d'ajout d'analyses, les options de personnalisation disponibles et comment cette
 
fonctionnalité renforce la qualité et la précision de nos opérations de laboratoire

a.	Modification de Profils d'Utilisateurs :
Dans un environnement multi-utilisateur, la gestion des profils d'utilisateurs est cruciale. Notre interface permet aux laborantins de personnaliser leurs profils, d'ajuster leurs paramètres et d'accéder à des fonctionnalités spécifiques en fonction de leurs responsabilités. Nous discuterons de la manière dont cette fonctionnalité offre une flexibilité aux utilisateurs pour adapter l'application à leurs besoins, tout en maintenant des normes de sécurité strictes.






![image](https://github.com/user-attachments/assets/349e8fc6-2142-4d26-ac74-3c64b7f2c708)




















Figure 17settings laborantins


1.	L’interface Chef laboratoire :



 ![image](https://github.com/user-attachments/assets/8dcc4290-81cf-4f72-a872-a9ad77ccaf3b)




a.	Gestion des Échantillons :
Au cœur de toute opération de laboratoire réside la gestion rigoureuse des échantillons. Notre interface permet au chef de laboratoire de superviser et de coordonner l'ensemble du processus, de l'enregistrement initial des échantillons à leur suivi à travers chaque étape de l'analyse. Nous explorerons comment cette fonctionnalité assure la traçabilité complète des échantillons, permettant une gestion efficace des ressources et une réduction des erreurs potentielles.

Figure 19interface de gestion echantillon_produit




![image](https://github.com/user-attachments/assets/d1e80c4e-0838-4fb8-9263-6167fec79d63)

 

![image](https://github.com/user-attachments/assets/d3f4a3e6-ddf5-4653-a052-538e942bab97)



 
Figure 21interface recherche d analyse

![image](https://github.com/user-attachments/assets/14d953db-320f-4d89-8b78-96dfb941c396)


c.	Génération de Rapports :
Enfin, l'interface du chef de laboratoire offre la possibilité de générer des rapports détaillés sur les opérations du laboratoire. Ces rapports fournissent une vue d'ensemble complète des activités, des résultats d'analyse et des tendances. Nous mettrons en évidence comment ces rapports contribuent à la prise de décision éclairée et à la conformité aux normes de qualité.

 ![image](https://github.com/user-attachments/assets/4e4de367-a88e-4084-b99d-265c8ebf0a5b)



 




Figure 22rapport d essai



d.	Gestion des Produits d'Analyse :

La variété des analyses réalisées au laboratoire nécessite une gestion précise des produits d'analyse. Cette fonctionnalité permet au chef de laboratoire de superviser l'inventaire des produits, de s'assurer de leur disponibilité pour les analyses et de garantir leur conformité aux normes. Nous discuterons de la manière dont cette gestion proactive des produits contribue à des analyses précises et de haute qualité.
 

![image](https://github.com/user-attachments/assets/a335e095-8581-4873-ae28-d70bf3baa926)

 

![image](https://github.com/user-attachments/assets/c0e74d0a-62ba-48b6-83d1-c60624b89fe2)

Figure 23interface gestion d analyse

































3.	Code :








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
