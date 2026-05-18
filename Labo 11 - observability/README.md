# Observabilité

## Objectifs

- Estimer son travail
- Dockeriser une application Spring Boot
- Instrumenter une application Spring Boot pour la visualisation des logs, métriques et traces
- Configurer un dashboard dans Kibana
- Configurer un dashboard dans Grafana

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/4MeZ9BEl
  - Nom du fichier : `report.md` à la racine du répertoire
  - Code directement sur GitHub Classroom
- Délai: 2 semaines
  - Rendu intermédiaire après 1 semaine pour avoir un retour sur le travail effectué

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

### Mise en place

Ce projet reprend [demotory](https://github.com/blueur/demotory) qui est le point de départ sur GitHub Classroom.

```bash
mvn spring-boot:run
```

http://localhost:8080

### Docker Compose

- Dockeriser l'application
- Créer un Docker Compose pour lancer l'application
  - `docker compose up`
- Utiliser les [profiles](https://docs.docker.com/compose/profiles/) pour activer/désactiver les outils APM

### Instrumentation

Instrumenter l'application en justifiant vos choix d'outils

- Le Docker Compose doit exposer les services suivants:
  - **Kibana** pour visualiser les logs sur http://localhost:5601
  - **Grafana** pour visualiser les métriques sur http://localhost:3000
    - **Prometheus** pour récupérer les métriques sur http://localhost:9090
  - **Jaeger** pour visualiser les traces sur http://localhost:16686
- Documenter les configurations manuelles à faire après avoir lancé `docker compose up` dans le `README.md`
  - Exemple: ajouter des dashboards dans Kibana et Grafana
  - Vous pouvez ajouter des screenshots dans la documentation

#### Logs avec Kibana

Visualiser les logs de tous les containers (application + outils APM) dans Kibana.

Bonus :

- Gérer les stacktraces qui sont sur plusieurs lignes (regrouper la stacktrace en un seul record)

#### Métriques avec Grafana

Visualiser les métriques de tous les containers (application + outils APM) dans Grafana.

Bonus :

- Ajouter des métriques personnalisées de l'application
  - Nombre d'entrées dans la map sous forme de [Gauge](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#gauge)
  - Nombre de changements de la map sous forme de [Sums](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#sums)

#### Traces avec Jaeger

Visualiser les traces de l'application dans Jaeger.

Bonus :

- Déployer aussi Zipkin et visualiser les traces dans Zipkin
- Comparer les deux outils

### Rapport

- Indiquer dans votre rapport votre démarche ainsi que les difficultés rencontrées
- Expliquer tous les choix techniques que vous avez fait (sauf ceux indiqués)

## Evaluation

L'évaluation se porte sur les critères suivants :

- Organisation
  - [ ] **Le rendu est correct et dans les temps.**
  - [ ] **Documentation (README.md) des configurations manuelles, de l'application et des APMs.**
  - [ ] _Le rapport (report.md) est complet (explication de la démarche et des choix techniques) et synthétique._
- Docker
  - [ ] **Bonne dockerisation & Utilisation des profiles**
- Logs
  - [ ] **Visualisation des logs de l'application dans Kibana.**
  - [ ] _Ajout des logs de tous les services & Stacktraces regroupées & Dashboard_
- Métriques
  - [ ] **Visualisation des métriques de l'application dans Grafana.**
  - [ ] _Ajout des métriques de tous les services & Gauge, Sums, &hellip;_
- Traces
  - [ ] **Visualisation des traces de l'application dans Jaeger.**
  - [ ] _Ajout des traces de tous les services & Visualisation des traces dans Zipkin & Comparaison avec Zipkin_
- Bonus
  - [ ] _Autre bonus_

|            Note            | &nbsp;1&nbsp; | 1.5 | &nbsp;2&nbsp; | 2.5 | &nbsp;3&nbsp; | 3.5 | &nbsp;4&nbsp; | 4.5 | &nbsp;5&nbsp; | 5.5 | &nbsp;6&nbsp; |
| :------------------------: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: | :-: | :-----------: |
| Nombre de critères validés |       0       |  1  |       2       |  3  |       4       |  5  |       6       |  7  |       8       |  9  |      10       |

- **En gras** : critères principaux.
- _En italique_ : critères secondaires.
