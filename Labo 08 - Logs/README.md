# Logs

## Objectifs

- Estimer son travail
- Déployer un monitoring EFK sur Docker Compose
- Parser les logs
- Créer un tableau de bord dans Kibana
- Déployer un monitoring EFK sur Kubernetes

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/qi6NRlh2
  - Nom du fichier : `report.md` à la racine du répertoire
  - Code directement sur GitHub Classroom
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

### EFK sur Docker Compose

Déployer un Docker Compose avec EFK (Elasticsearch, Fluentd, Kibana) et un serveur web.

- Tutoriel (plus à jour) sur https://docs.fluentd.org/container-deployment/docker-compose
- Mettre à jour le tutoriel et le rendre fonctionnel.
- Endpoints :
  - Serveur web : http://localhost:80
  - Kibana : http://localhost:5601
  - Elasticsearch : http://localhost:9200
    - Affiche des informations sur le cluster.

<details>
  <summary>
    Indices
  </summary>
  - https://github.com/fluent/fluentd-docs-gitbook/issues/391
  - https://stackoverflow.com/questions/71933584/my-web-server-tries-to-connect-to-fluentd-before-listening-port-on-docker + https://docs.docker.com/config/containers/logging/fluentd/#fluentd-async
  - https://www.elastic.co/guide/en/elasticsearch/reference/8.11/security-settings.html#general-security-settings
</details>

:::tip Exemple

https://github.com/blueur/efk

:::

### Parser les logs

Parser les logs du serveur web avec Fluentd :

- Apache : https://docs.fluentd.org/parser/apache2
- Nginx : https://docs.fluentd.org/parser/nginx

Vérifier que les logs sont bien parsés dans Kibana.

<details>
  <summary>
    Solution
  </summary>
```
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>

<filter web.log>
  @type parser
  key_name log

  <parse>
    @type apache2
  </parse>
</filter>

<match web.log>
  @type copy

  <store>
    @type elasticsearch
    host elasticsearch
    port 9200
    logstash_format true
    logstash_prefix fluentd
    logstash_dateformat %Y%m%d
    include_tag_key true
    type_name access_log
    tag_key @log_name
    flush_interval 1s
  </store>

  <store>
    @type stdout
  </store>
</match>
```

https://github.com/blueur/efk/tree/feature/parser-web

</details>

Créer un tableau de bord dans Kibana :

- https://www.elastic.co/guide/en/kibana/current/create-a-dashboard-of-panels-with-web-server-data.html
- Affiche la proportion des chemins (`path`) et des codes HTTP (`code`) dans les logs

### Bonus : EFK sur Kubernetes

Déployer EFK sur Kubernetes : https://docs.fluentd.org/container-deployment/kubernetes

### Bonus : Ajouter Metricbeat sur Docker Compose

https://www.elastic.co/guide/en/beats/metricbeat/current/running-on-docker.html
