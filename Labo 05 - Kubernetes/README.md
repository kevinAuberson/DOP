# Kubernetes

## Objectifs

- Estimer son travail
- Utiliser minikube
- Déployer une application sur Kubernetes
- Créer un fichier `deployment.yaml` pour déployer l'application

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/G5aiIcSU
  - Nom du fichier : `report.md` à la racine du répertoire
  - Avec le lien vers la Merge Request GitLab
- Délai: 2 semaines

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

### Utiliser minikube

- Suivre les instructions sur [minikube](https://minikube.sigs.k8s.io/docs/start/) pour déployer des applications sur votre machine.
  - Suivre les points suivants:
    - 2. Start your cluster
    - 3. Interact with your cluster
    - 4. Deploy applications
      - Service
      - LoadBalancer
        - Scale le Deployment à 2 replicas et vérifier que les requêtes soient bien réparties entre les deux pods (en y accédant en navigation privée).
      - Ingress
- Regarder les logs (au niveau du pod).
  - Sur le dashboard, sélectionner un pod.
    - En haut à droite, il y a plusieurs icônes, dont `View logs` et `Exec into pod`.
  - En ligne de commande, utiliser `kubectl logs` et `kubectl exec` (`kubectl get pods` pour lister les pods).

### Déployer une application

Déployer une application sur Kubernetes. Les instructions suivantes utilise https://gitlab.com/blueur/heig-vd-devops mais c'est mieux d'utiliser sa propre version de l'application.

#### GUI

Déployer l'application sur Kubernetes en utilisant le dashboard.

- Déployer le frontend
  - Cliquer sur le `+` en haut à droite
    - `Create from form`
      - App name : `frontend`
      - Container image : `registry.gitlab.com/blueur/heig-vd-devops/frontend:latest`
      - Service : `Internal`
      - Port : `80`
      - Target port : `80`
    - Cliquer sur `Deploy`
  - Accéder à l'application avec `minikube service frontend`
- Déployer une base de donnée
  - App name : `database`
  - Container image : `postgres:16-alpine`
  - Service : `Internal`
  - Port : `5432`
  - Target port : `5432`
  - Cliquer sur `Show advanced options`
    - Environment variables
      - `POSTGRES_PASSWORD` : `postgres`
  - Cliquer sur `Deploy`
- Déployer le backend
  - App name : `backend`
  - Container image : `registry.gitlab.com/blueur/heig-vd-devops/backend:latest`
  - Service : `Internal`
  - Port : `80`
  - Target port : `80`
  - Cliquer sur `Show advanced options`
    - Environment variables
      - `POSTGRES_HOST` : `database`
      - `POSTGRES_PASSWORD` : `postgres`
      - `ROOT_PATH`: `/api`
- Créer un ingress
  - `Create from input`
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: heig-vd-devops-ingress
      annotations:
        nginx.ingress.kubernetes.io/use-regex: "true"
        nginx.ingress.kubernetes.io/rewrite-target: /$1
    spec:
      ingressClassName: nginx
      rules:
        - http:
            paths:
              - path: /?(.*)
                pathType: ImplementationSpecific
                backend:
                  service:
                    name: frontend
                    port:
                      number: 80
              - path: /api/?(.*)
                pathType: ImplementationSpecific
                backend:
                  service:
                    name: backend
                    port:
                      number: 80
    ```
- Accéder à l'application sur http://127.0.0.1/

#### CLI

- Suivre les instructions pour créer une application stateless : https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
- Suivre les instructions pour créer une application stateful : https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
- Créer un fichier `deployment.yaml` à la racine de votre repository qui permet de déployer votre application sur Kubernetes.
  - Il doit être possible de déployer ou mettre à jour toute l'application avec `kubectl apply -f deployment.yaml`
- Déployer votre application sur un nouveau [namespace](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)

### Cluster du cours

Déployer son application sur le [cluster Kubernetes du cours](/docs/tools/kubernetes) dans le namespace `<votre-nom>`.
