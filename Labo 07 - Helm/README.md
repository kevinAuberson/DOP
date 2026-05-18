# Helm

## Objectifs

- Estimer son travail
- Utiliser les ConfigMaps et Secrets de Kubernetes
- Utiliser les volumes de Kubernetes
- Créer un Helm chart

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/BcWAPpYa
  - Nom du fichier : `report.md` à la racine du répertoire
  - Avec le lien vers la Merge Request GitLab
- Délai: 1 semaine

## Tâches

Reprendre son projet GitLab `DOP Python` des laboratoires précédents.

### Estimer son travail

- Estimer le temps nécessaire pour réaliser ce travail.
  - Découper le travail en tâches pour faciliter l'estimation.
- Une fois terminé, comparer le temps estimé avec le temps réellement passé.

| Tâche      | Temps estimé | Temps passé | Commentaire |
| ---------- | ------------ | ----------- | ----------- |
| Estimation | 10m          | 15m         | ...         |
| ...        | ...          | ...         | ...         |
| Total      | 2h           | 1h30        | ...         |

### Limiter les ressources

Définir les [limites de ressources](https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota) pour ses pods, par exemple :

- 0.25 core de CPU
- 512MiB de RAM

:::info[Question rapport]
Quelle est la différence entre les limites et les requêtes de ressources ?
:::

### Utiliser les ConfigMaps et Secrets

Utiliser une ConfigMap pour définir les variables d'environnement suivantes :

- POSTGRES_USER : `postgres`
- POSTGRES_DB : `postgres`

Utiliser un Secret pour définir les variables d'environnement suivantes :

- POSTGRES_PASSWORD : `postgres`

### Utiliser les volumes

Créer un volume pour le pod `postgres` et le monter dans le dossier `/var/lib/postgresql/data`.

- Utiliser un [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) de 128MiB.

:::info[Question rapport]
Est-ce une bonne idée de déployer une base de données avec Kubernetes ?
:::

### Configurer les stratégies de déploiement

Quelles stratégies de déploiement sont disponibles dans Kubernetes ?

Quelle stratégie de déploiement devriez-vous utiliser pour chacun de vos déploiements ?

<details>
  <summary>
    Solution
  </summary>
  Préférer le RollingUpdate pour les applications web et le Recreate pour les bases de données.
</details>

:::info[Question rapport]
Pourquoi ?
:::

### Créer un Helm chart

[Helm](https://helm.sh/) est un package manager pour Kubernetes, une façon de définir et de gérer les applications Kubernetes.

- Créer un Helm chart pour son application : `helm create helm-chart`.
- Suivre les instructions de la [documentation](https://helm.sh/docs/chart_template_guide/getting_started/).
- Modifier le Helm chart pour déployer son application.

### Créer un deuxième environnement

Utiliser son Helm chart pour déployer une deuxième instance de son application dans un autre namespace en utilisant des valeurs différentes pour :

- POSTGRES_USER
- POSTGRES_DB
- POSTGRES_PASSWORD

## Références

- https://gitlab.com/blueur/heig-vd-devops
