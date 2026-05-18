# CI/CD Java

## Objectifs

- Estimer son travail
- Dockeriser une application Java
- Configurer une pipeline CI/CD pour une application Java
- Configurer un déploiement sur Kubernetes pour une application Java

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/5QPDBsHu
  - Nom du fichier : `report.md` à la racine du répertoire
  - Avec le lien vers la Merge Request GitLab
- Délai: 2 semaines
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

### Prérequis

- [Maven](https://maven.apache.org/)
- [Java 17](https://adoptium.net/fr/temurin/releases/?version=17) (ou supérieur)

### Préparation

- Fork le repository suivant : https://gitlab.com/blueur/heig-vd-devops-java
  - Renommer le projet en `dop-java`.
- Cloner votre repository sur votre machine.
- Empaqueter l'application avec Maven : `mvn package`
- Lancer l'application : `mvn spring-boot:run`
  - L'application est accessible sur http://127.0.0.1:8080/

### Application des principes DevOps

- Conteneuriser l'application avec Docker.
  - Quelle image de base ? Pourquoi ?
  - Utiliser la version 17 de Java.
- Configurer Docker Compose de sorte que `docker compose up` lance l'application sur une nouvelle machine.
- Configurer la CI/CD sur GitLab.
  - Pour chaque commit sur n'importe quelle branche :
    - Vérifier que le projet compile.
    - Vérifier que les tests passent.
      - Avec les [Unit Test Reports](https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html)
  - Pour chaque merge request :
    - Vérifier que l'image Docker se construit.
  - Pour chaque commit sur `main` :
    - Mettre à jour l'image Docker sur le registry GitLab avec le tag `latest`.
- Configurer un déploiement sur Kubernetes : `kubectl apply -f deployment.yaml` doit lancer l'application sur un cluster Kubernetes.

### Rapport

- Indiquer dans votre rapport votre démarche ainsi que les difficultés rencontrées.
- Expliquer tous les choix techniques que vous avez fait (sauf ceux indiqués).
  -Expliquer comment utiliser les outils de CI/CD dans GitLab (unit test report, code coverage, SAST, ...).

## Evaluation

L'évaluation se porte sur les critères suivants :

- Organisation
  - [ ] **La Merge Request est correctement créée et dans les temps.**
  - [ ] **Le rapport est complet et synthétique.**
- Docker
  - [ ] **Le Docker Compose est fonctionnel.**
  - [ ] _Les bonnes pratiques sont appliquées pour Docker & Docker Compose._
- CI/CD
  - [ ] **La pipeline CI/CD est fonctionnelle.**
  - [ ] _Fonctionnalités supplémentaires pour la CI/CD (code coverage, SAST, ...)._
  - [ ] _Les bonnes pratiques sont appliquées pour la CI/CD._
- Kubernetes
  - [ ] **Le déploiement Kubernetes est fonctionnel.**
  - [ ] _Les bonnes pratiques sont appliquées pour Kubernetes._

|            Note            | &nbsp;1&nbsp; | &nbsp;2&nbsp; | 2.5 | &nbsp;3&nbsp; | 3.5 | &nbsp;4&nbsp; | 4.5 | &nbsp;5&nbsp; | 5.5 | &nbsp;6&nbsp; |
| :------------------------: | :-----------: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: |
| Nombre de critères validés |       0       |       1       |  2  |       3       |  4  |       5       |  6  |       7       |  8  |       9       |

- **En gras** : critères principaux.
- _En italique_ : critères secondaires.
