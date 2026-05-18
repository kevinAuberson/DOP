# Docker

## Objectifs

- Estimer son travail
- Dockeriser une application
- Créer un Docker Compose
- Appliquer les bonnes pratiques

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/TuhrFmh4
  - Nom du fichier : `report.md` à la racine du répertoire
  - Avec le lien vers la Merge Request GitLab
- Délai: 1 semaine
- **Laboratoire noté**

## Tâches

### Estimer son travail

- Estimer le temps nécessaire pour réaliser ce travail.
  - Découper le travail en tâches pour faciliter l'estimation.
- Une fois terminé, comparer le temps estimé avec le temps réellement passé.

| Tâche      | Temps estimé | Temps passé | Commentaire |
| ---------- | ------------ | ----------- | ----------- |
| Estimation | 10m          | 15m         | ...         |
| ...        | ...          | ...         | ...         |
| Total      | 2h           | 1h30        | ...         |

### Git

- Reprendre son projet GitLab du laboratoire précédent (DOP Python).
- Travailler sur une nouvelle branche `feature/02-docker` (à partir de `feature/01-tools` en attendant qu'elle soit merge sur `main`).
  - Faire une merge request (MR) sur `main` une fois terminé et demander une revue.
  - Une fois qu'une MR est acceptée, la merge sur `main`.
- Séparer son travail en commits cohérents avec des messages de commit clairs et concis.

:::info[Question rapport]

Indiquer le lien vers la MR dans le rapport.

:::

### Docker

:::info[Pour débuter avec Docker]

- [Containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/)
- [Update the application](https://docs.docker.com/get-started/workshop/03_updating_app/)

:::

- Dockeriser les deux applications `frontend` et `backend` du précédent laboratoire.
  - On doit pouvoir construire et démarrer les deux applications depuis leur dossier respectif.
  - Regarder dans les documentations officielles des frameworks pour trouver des exemples de Dockerfile.
  - Suivre les bonnes pratiques pour les Dockerfiles.
    - Frontend
      - Utiliser [nginx](https://nginx.org/) comme serveur web
      - `docker build -t frontend . && docker run -p 80:80 frontend`
    - Backend
      - `docker build -t backend . && docker run -p 8080:80 backend`
  - Ne pas oublier les [`.dockerignore`](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

:::info[Question rapport]

Justifier ses choix pour les Dockerfiles.

:::

### Docker Compose

- Créer un `compose.yml` pour démarrer les deux applications.
  - Depuis la racine du projet, on doit pouvoir :
    - construire les deux applications avec `docker compose build`.
    - démarrer les deux applications avec `docker compose up`.
    - accéder à l'application frontend sur le port 80.
    - accéder à l'application backend sur le port 8080.
    - arrêter les deux applications avec `docker compose down`.
  - Le Docker Compose doit fonctionner sur un nouvel ordinateur juste en clonant le projet.
- Ajouter un service `database`.
  - Utiliser une base de données PostgreSQL.
  - Utiliser les credentials suivants :
    - user : `postgres`
    - password : `postgres`
    - database : `postgres`
  - Exposer le port `5432`
  - Ajouter un volume pour persister les données (on doit pouvoir supprimer les conteneurs `docker compose rm` et les recréer sans perdre les données).
  - Possibilité d'utiliser [DBeaver](https://dbeaver.io/) pour visualiser les données.
- Indiquer les dépendances entre les services

:::info[Question rapport]

Justifier ses choix pour le Docker Compose et la base de données.

:::

## Evaluation

L'évaluation se porte sur les critères suivants :

- Rapport
  - [ ] **Le rapport est complet.**
  - [ ] _Le rapport est bien structuré et synthétique._
  - [ ] _Les choix techniques sont bien justifiés._
- Fonctionnalités
  - [ ] **Le Docker Compose est fonctionnel.**
  - [ ] **Toutes les fonctionnalités sont présentes (persistance, dockerignore, dépendances, &hellip;).**
  - [ ] _Les bonnes pratiques sont appliquées pour Docker._
  - [ ] _Les bonnes pratiques sont appliquées pour Docker Compose._
- Organisation
  - [ ] **La Merge Request est correctement créée et dans les temps.**
  - [ ] _Les commits sont cohérents et bien organisés._

|            Note            | &nbsp;1&nbsp; | &nbsp;2&nbsp; | 2.5 | &nbsp;3&nbsp; | 3.5 | &nbsp;4&nbsp; | 4.5 | &nbsp;5&nbsp; | 5.5 | &nbsp;6&nbsp; |
| :------------------------: | :-----------: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: |
| Nombre de critères validés |       0       |       1       |  2  |       3       |  4  |       5       |  6  |       7       |  8  |       9       |

- **En gras** : critères principaux.
- _En italique_ : critères secondaires.
