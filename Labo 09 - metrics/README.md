# Métriques

## Objectifs

- Estimer son travail
- Déployer Prometheus et Grafana sur Docker Compose
- Instrumenter une application Python (FastAPI)

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/uuvyWOwh
  - Nom du fichier : `report.md` à la racine du répertoire
  - Première partie : Code directement sur GitHub Classroom
  - Deuxième partie : MR sur votre projet DOP-Python (ajouter le lien dans le rapport)
- Délai: 1 semaine

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

### Prometheus et Grafana sur Docker Compose

Créer un Docker Compose avec Prometheus et Grafana qui collecte les métriques de notre machine :

- Utiliser [Node exporter](https://github.com/prometheus/node_exporter) pour collecter les métriques de la machine.
- Suivre le tutoriel sur https://mxulises.medium.com/simple-prometheus-setup-on-docker-compose-f702d5f98579
- Ajouter Grafana : https://github.com/docker/awesome-compose/blob/master/prometheus-grafana/README.md

Les endpoints devraient être accessibles sur les ports suivants :

- Prometheus : http://localhost:9090
- Grafana : http://localhost:3000

Observer les endpoints `/metrics` de :

- Prometheus : http://localhost:9090/metrics
- Node exporter : http://localhost:9100/metrics

(Changer de navigateur ou essayez en ligne de commande avec `curl`/`wget` en cas d'erreur.)

Rafraîchir la page des métriques.

:::info[Question rapport]

Expliquer le fonctionnement de Prometheus :

- Comment Prometheus collecte les métriques ?
- Où sont stockées les métriques ?
- Comment sont définies les métriques ?
- Qui définit la fréquence de collecte des métriques ?
- Qu'est-ce qui diffère par rapport à un système de logs ?

:::

### Instrumenter une application Python

- Reprendre votre application [HEIG-VD DevOps](https://gitlab.com/blueur/heig-vd-devops) et ajoutez des métriques au backend
- Utiliser https://github.com/trallnag/prometheus-fastapi-instrumentator
- Vérifier vos métriques avec http://localhost/api/metrics
- Ajouter Prometheus à votre Docker Compose
- Vérifier que les métriques sont bien collectées par Prometheus

:::tip Astuce

Utiliser les profiles pour activer/désactiver les services liés à l'observabilité : https://docs.docker.com/compose/profiles/

:::

:::tip Exemples

https://github.com/blueur/prometheus  
https://gitlab.com/blueur/heig-vd-devops/-/tree/feature/instrumentation

:::

### Instrumenter Nginx

Chercher comment collecter les métriques du frontend (Nginx) avec Prometheus.

:::info[Question rapport]

Qu'est-ce qui serait nécessaire pour que cela fonctionne ?

:::

En bonus, ajoutez les métriques de Nginx à votre Docker Compose.

### Bonus : Prometheus sur Docker

Pour collecter les métriques de Docker avec Prometheus : https://docs.docker.com/config/daemon/prometheus/

## Références

- https://github.com/blueur/prometheus
- https://gitlab.com/blueur/heig-vd-devops/-/tree/feature/instrumentation
