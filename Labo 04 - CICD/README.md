import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CI/CD

## Objectifs

- Estimer son travail
- Ajouter des tests unitaires en Python
- Créer une CI/CD pipeline sur GitLab

## Rendu

- Rapport individuel en Markdown à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/zuAA1JDu
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

### Git

- Reprendre son projet GitLab du laboratoire précédent (DOP Python).
- Travailler sur une nouvelle branche `feature/04-cicd`.
  - Faire une merge request (MR) sur `main` une fois terminé et demander une revue.
  - Une fois qu'une MR est acceptée, la merge sur `main`.
- Séparer son travail en commits cohérents avec des messages de commit clairs et concis.

### Tester le backend

- Ajouter les dépendances de développement `poetry add -G dev pytest pytest-cov httpx`.
  - Une dépendance de développement est une dépendance qui n'est pas nécessaire en production, par exemple uniquement pour les tests.
  - `pytest` est le framework de test.
  - `pytest-cov` permet de générer un rapport de couverture de code.
  - `httpx` permet de faire des requêtes HTTP dans les tests.
- Ajouter ou modifier les fichiers suivants (inspirés de cette [documentation](https://fastapi.tiangolo.com/advanced/testing-database/)) :

<Tabs>
  <TabItem value="main.py" default>

```python title="/backend/backend/main.py" showLineNumbers
from os import getenv
# highlight-next-line
from sys import modules

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

# highlight-next-line
if "pytest" not in modules:
# highlight-next-line
    models.Base.metadata.create_all(bind=engine)

app = FastAPI(root_path=getenv("ROOT_PATH"))

...
```

  </TabItem>
  <TabItem value="test_main.py">

```python title="/backend/backend/tests/test_main.py" showLineNumbers
from random import choices, uniform
from string import ascii_letters

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.database import Base
from backend.main import app, get_db

DATABASE_URL = "sqlite://"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def random_string(n=32):
    return "".join(choices(ascii_letters, k=n))


def random_double():
    return round(uniform(0.0, 100.0), 2)


product = {
    "name": random_string(),
    "description": random_string(512),
    "price": random_double(),
}


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_empty_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product():
    response = client.post(
        "/products/",
        json=product,
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}


def test_read_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}


def test_read_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, **product}]


def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}
    response = client.get("/products/1")
    assert response.status_code == 404


def test_read_deleted_empty_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []
```

  </TabItem>
</Tabs>

- Pour lancer les tests : `poetry run pytest --cov`

### GitLab CI/CD

Créer une pipeline sur GitLab CI/CD qui :

- a les 3 stages :
  - build : vérifie que le code compile.
  - test (autant que possible parmi les éléments suivants) :
    - vérifie que les tests (du backend) passent.
    - [Unit Test Reports](https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html)
    - [Code Coverage](https://docs.gitlab.com/ee/ci/testing/code_coverage.html)
    - [Code Quality](https://docs.gitlab.com/ee/ci/testing/code_quality.html)
    - [Dependency Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/)
    - [SAST](https://docs.gitlab.com/ee/user/application_security/sast/)
    - [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/)
  - deploy : met à jour les images Docker sur le registry.
- est déclenchée à chaque push sur n'importe quelle branche.
  - le stage `deploy` n'est exécuté que sur `main`.
- Le frontend et le backend doivent être dans des jobs séparés et en parallèle.
  - Chacun est exécuté uniquement lorsqu'il y a des changements dans son dossier.
    - [Parent-child pipelines](https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html#parent-child-pipelines)

#### Proposition

Beaucoup de changements sur la pipeline vont être testés, une manière d'éviter d'avoir plein de commit est d'en avoir qu'un seul au final (à éviter sur `main` ou `develop`) : `git commit --amend --all --no-edit && git push --force-with-lease`

Commencer par le frontend (commencer le script par `cd frontend/`) :

- Le job `build-frontend` utilise l'image `node:lts`, exécute `npm ci` et `npm run build`.
  - Le résultat du build est gardé dans un artefact pour être utilisé par le job `deploy-frontend`.
  - Ajouter le [cache](https://docs.gitlab.com/ee/ci/caching/#cache-nodejs-dependencies).
- Le job `deploy-frontend` utilise l'image `docker` avec le service `docker:dind`, exécute `docker build -t ${CI_REGISTRY_IMAGE}/frontend:latest .` et `docker push ${CI_REGISTRY_IMAGE}/frontend:latest`.
  - [Docker in Docker](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#docker-in-docker-with-tls-enabled-in-the-docker-executor)
  - [Docker login](https://docs.gitlab.com/ee/ci/docker/authenticate_registry.html#option-1-run-docker-login)
    - `echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY --username $CI_REGISTRY_USER --password-stdin`
  - [Docker Layer Caching](https://docs.gitlab.com/ee/ci/docker/docker_layer_caching.html)

<details>
  <summary>Solution `.gitlab-ci.yml`</summary>
  <div>

```yaml
build-frontend:
  stage: build
  image: node:lts
  cache:
    key:
      files:
        - frontend/package-lock.json
    paths:
      - frontend/.npm/
  before_script:
    - cd frontend/
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run build
  artifacts:
    paths:
      - frontend/dist/

deploy-frontend:
  stage: deploy
  image: docker
  services:
    - docker:dind
  dependencies:
    - build-frontend
  variables:
    REGISTRY_IMAGE: ${CI_REGISTRY_IMAGE}/frontend
  before_script:
    - cd frontend/
    - echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY --username $CI_REGISTRY_USER --password-stdin
  script:
    - docker pull $REGISTRY_IMAGE:latest || true
    - docker build --cache-from $REGISTRY_IMAGE:latest -t $REGISTRY_IMAGE:latest .
    - docker push $REGISTRY_IMAGE:latest
```

  </div>
</details>

Puis le backend (similairement au frontend) :

- Le job `build-backend` utilise l'image `python:3.11`, installe Poetry et les dépendances en les cachant pour les prochains jobs.
  - [Cache](https://docs.gitlab.com/ee/ci/caching/#cache-python-dependencies)

```yaml
build-backend:
  stage: build
  image: python:3.11
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  cache:
    paths:
      - .cache/pip
      - backend/.venv/
  before_script:
    - cd backend/
    - pip install poetry
    - poetry config virtualenvs.in-project true
  script:
    - poetry install
```

- Le job `test-backend` reprend le cache du job `build-backend` et exécute `poetry run pytest --cov`.

```yaml
test-backend:
  stage: test
  image: python:3.11
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  cache:
    paths:
      - .cache/pip
      - backend/.venv/
  before_script:
    - cd backend/
    - pip install poetry
    - poetry config virtualenvs.in-project true
  script:
    - poetry run pytest --cov
```

- Ajouter les éléments suivants :
  - [Unit test reports](https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html#how-to-set-it-up) avec [JUnitXML](https://docs.pytest.org/en/latest/how-to/output.html#creating-junitxml-format-files).
  - [Test coverage visualization](https://docs.gitlab.com/ee/ci/testing/test_coverage_visualization.html#python-example)
- Le job `deploy-backend` est très similaire au job `deploy-frontend`.

<details>
  <summary>Solution `.gitlab-ci.yml`</summary>
  <div>

```yaml
build-backend:
  stage: build
  image: python:3.11
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  cache:
    paths:
      - .cache/pip
      - backend/.venv/
  before_script:
    - cd backend/
    - pip install poetry
    - poetry config virtualenvs.in-project true
  script:
    - poetry install

test-backend:
  stage: test
  image: python:3.11
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  cache:
    paths:
      - .cache/pip
      - backend/.venv/
  before_script:
    - cd backend/
    - pip install poetry
    - poetry config virtualenvs.in-project true
  script:
    - poetry run pytest --cov --junitxml="rspec.xml" --cov-report term --cov-report xml:coverage.xml
  coverage: '/(?i)total.*? (100(?:\.0+)?\%|[1-9]?\d(?:\.\d+)?\%)$/'
  artifacts:
    paths:
      - backend/rspec.xml
    reports:
      junit: backend/rspec.xml
      coverage_report:
        coverage_format: cobertura
        path: backend/coverage.xml

deploy-backend:
  stage: deploy
  image: docker
  services:
    - docker:dind
  variables:
    REGISTRY_IMAGE: ${CI_REGISTRY_IMAGE}/backend
  before_script:
    - cd backend/
    - echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY --username $CI_REGISTRY_USER --password-stdin
  script:
    - docker pull $REGISTRY_IMAGE:latest || true
    - docker build --cache-from $REGISTRY_IMAGE:latest -t $REGISTRY_IMAGE:latest .
    - docker push $REGISTRY_IMAGE:latest
```

  </div>
</details>

- Effectuer le stage `deploy` uniquement sur la branche `main`.
  - [rules](https://docs.gitlab.com/ee/ci/yaml/#rules)
- Transformer votre pipeline en [Directed Acyclic Graph Pipelines](https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html#directed-acyclic-graph-pipelines).
- Transformer votre pipeline en [Parent-child pipelines](https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html#parent-child-pipelines).
- [Optimisez vos fichiers YAML](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html)
- Ajouter et configurer (autant que possible) les éléments suivants :
  - [Code Quality](https://docs.gitlab.com/ee/ci/testing/code_quality.html)
  - [Dependency Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/)
  - [SAST](https://docs.gitlab.com/ee/user/application_security/sast/)
  - [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/)

## Références

- https://gitlab.com/blueur/heig-vd-devops
