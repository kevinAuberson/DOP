# Traces

## Objectifs

- Estimer son travail
- Explorer les traces avec Jaeger
- Instrumenter une application Python (FastAPI) avec OpenTelemetry
- Configurer un Collector pour exporter les traces vers Jaeger
- Instrumenter une base de données PostgreSQL avec OpenTelemetry

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/rVquW_MY
  - Nom du fichier : `report.md` à la racine du répertoire
  - MR sur votre projet DOP-Python (ajouter le lien dans le rapport)
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

### Démonstration sur Docker Compose

Déployer la démonstration suivante sur votre machine : https://opentelemetry.io/docs/demo/docker-deployment/

:::tip Astuce

Une version de la démonstration est déployée sur notre cluster Kubernetes :

- Web store: http://otel-demo.k8s.heig-vd.blueur.com/
- Grafana: http://otel-demo.k8s.heig-vd.blueur.com/grafana
- Load Generator UI: http://otel-demo.k8s.heig-vd.blueur.com/loadgen/
- Jaeger UI: http://otel-demo.k8s.heig-vd.blueur.com/jaeger/ui

https://opentelemetry.io/docs/demo/kubernetes-deployment/

:::

Suivre le scénario suivant : https://opentelemetry.io/docs/demo/scenarios/recommendation-cache/

### Instrumenter FastAPI (+ PostgreSQL)

Reprendre votre projet [DOP Python](https://gitlab.com/blueur/heig-vd-devops) et instrumenter le backend avec OpenTelemetry

- Ajouter les dépendances suivantes : `poetry add opentelemetry-instrumentation-fastapi opentelemetry-exporter-otlp`
  - [opentelemetry-instrumentation-fastapi](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html) pour automatiquement instrumenter FastAPI
  - [opentelemetry-exporter-otlp](https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html) pour exporter les traces au format OTLP
- Instrumenter l'application en ajoutant ces lignes :

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

...

tracerProvider = TracerProvider()
tracerProvider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace.set_tracer_provider(tracerProvider)
FastAPIInstrumentor.instrument_app(app)
```

- Pour afficher les spans dans la console (debug), vous pouvez ajouter le [ConsoleSpanExporter](https://opentelemetry-python.readthedocs.io/en/latest/sdk/trace.export.html#opentelemetry.sdk.trace.export.ConsoleSpanExporter) :

```python
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

...

trace.get_tracer_provider().add_span_processor(ConsoleSpanExporter())
```

- Ajouter les variables d'environnement suivantes :
  - `OTEL_RESOURCE_ATTRIBUTES`: `service.name=backend-service` pour le nom de notre service dans les traces
  - `OTEL_EXPORTER_OTLP_ENDPOINT`: `http://jaeger:4317` pour la destination des traces (Jaeger ou OpenTelemetry Collector)

Ajouter [Jaeger](https://www.jaegertracing.io/docs/1.52/deployment/#all-in-one) au Docker Compose

- On a besoin d'activer OpenTelemetry en ajoutant la variable d'environnement `COLLECTOR_OTLP_ENABLED=true`
- Jaeger UI: http://localhost:16686

Ajouter un [Collector](https://opentelemetry.io/docs/collector/) au Docker Compose

- https://opentelemetry.io/docs/collector/installation/#docker-compose
- Configurez le Collector pour exporter les traces vers Jaeger ([Troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/)) :

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:

exporters:
  otlp/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/jaeger]
```

- Le Collector est un adaptateur qui permet de recevoir des traces de différents formats et de les exporter vers différents formats. Dirigez les traces du backend vers le Collector pour vérifier que Jaeger les reçoit bien aussi.

En bonus, instrumenter la database PostgreSQL avec le [Collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/postgresqlreceiver/README.md)

- Configurer l'exportation des metrics vers [Prometheus](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusexporter)
- Vous pourrez observer les metrics `postgresql_*` dans Prometheus (et Grafana), par exemple `postgresql_commits_total` ou `postgresql_rows`

:::info[Question rapport]

Dans quels cas le collector est en mode [pull ou push](https://www.alibabacloud.com/blog/pull-or-push-how-to-select-monitoring-systems_599007) ?

:::

:::tip Exemple

https://gitlab.com/blueur/heig-vd-devops/-/tree/feature/instrumentation

:::

## Références

- https://gitlab.com/blueur/heig-vd-devops/-/tree/feature/instrumentation
- https://medium.com/@rickymondal/distributed-tracing-with-opentelemetry-91b76b22abf9
- https://www.baeldung.com/spring-boot-opentelemetry-setup
- https://tillepille.io/posts/otel-fastapi/
- https://opentelemetry.io/docs/collector/configuration/#exporters
- https://www.alibabacloud.com/blog/pull-or-push-how-to-select-monitoring-systems_599007
