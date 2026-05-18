# Outils

## Objectifs

- Estimer son travail
- Avoir un environnement de travail fonctionnel
- Utiliser GitLab et GitHub Classroom

## Rendu

- Rapport individuel en [Markdown](https://fr.wikipedia.org/wiki/Markdown) à rendre avant le prochain cours
  - GitHub Classroom : https://classroom.github.com/a/9GFgSJJf
  - Nom du fichier : `report.md` à la racine du répertoire
  - Avec le lien vers la Merge Request GitLab
- Présentation individuelle à rendre sur Cyberlearn
  - Nom du fichier : `presentation-prenom-nom.pdf`
- Délai: 1 semaine

## Tâches

### Comptes GitHub et GitLab

- Commencer par indiquer ses pseudo [GitHub](https://github.com/) et [GitLab](https://gitlab.com/) sur [Cyberlearn](https://cyberlearn.hes-so.ch/mod/questionnaire/view.php?id=2421655).
  - Créer les comptes si nécessaire et les lier à des adresses e-mail privées afin de ne pas perdre l'accès à la fin de la formation.

### Estimer son travail

- Estimer le temps nécessaire pour réaliser ce travail dans le rapport.
  - Découper le travail en tâches pour faciliter l'estimation.
- Une fois terminé, comparer le temps estimé avec le temps réellement passé.
- Le but n'est pas d'estimer correctement, mais de comprendre comment améliorer ses estimations.

| Tâche      | Temps estimé | Temps passé | Commentaire |
| ---------- | ------------ | ----------- | ----------- |
| Estimation | 10m          | 15m         | ...         |
| ...        | ...          | ...         | ...         |
| Total      | 2h           | 1h30        | ...         |

### Environnement de travail

:::tip[Conseils]

- Préférer les versions stables (LTS) aux versions de développement plus récentes.
  - Moins de bugs potentiels.
- Préférer les versions officielles aux versions tierces (p. ex. Python au lieu de Anaconda).
  - On n'installe que les outils nécessaires.
- Les gestionnaires de versions (nvm et pyenv) permettent d'avoir plusieurs versions installées sur la machine.
- Pour Windows
  - Installer [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=fr-ch).
  - Utiliser [Chocolatey](https://chocolatey.org/) pour installer les outils.
  - Utiliser [cmder](https://cmder.app/) comme terminal (disponible via [Chocolatey](https://community.chocolatey.org/packages/Cmder)).
    - Intégration avec [Windows Terminal](https://medium.com/talpor/windows-terminal-cmder-%EF%B8%8F-573e6890d143).
  - Possible problème d'[alias d'exécution de Python](https://www.thewindowsclub.com/manage-app-execution-aliases-on-windows-10) à désactiver.

:::

Installer et vérifier les outils suivants (mettre à jour si nécessaire):

- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
  - Vérifier avec `git --version`.
- [Docker](https://www.docker.com/)
  - Vérifier avec `docker --version`.
  - Vérifier avec `docker compose version`.
- [Node.js](https://nodejs.org/)
  - Au moins la dernière version LTS.
  - Vérifier avec `node --version`.
  - Possibilité d'utiliser [nvm](https://github.com/nvm-sh/nvm) pour gérer plusieurs versions de Node.js.
- [Python](https://www.python.org/)
  - Vérifier avec `python --version`.
  - Possibilité d'utiliser [pyenv](https://github.com/pyenv/pyenv) pour gérer plusieurs versions de Python.
- [Poetry](https://python-poetry.org/)
  - Vérifier avec `poetry --version`.
  - Utiliser les [virtualenvs en local](https://python-poetry.org/docs/configuration/#virtualenvsin-project) avec `poetry config virtualenvs.in-project true`.
- [MiniKube](https://minikube.sigs.k8s.io/docs/)
  - Vérifier avec `minikube version`.
- [Java](https://adoptium.net/fr/)
  - Au moins la dernière version LTS.
  - Vérifier avec `java --version`.
- [Maven](https://maven.apache.org/)
  - Vérifier avec `mvn --version`.

### GitLab

- Créer un projet privé sur GitLab dans votre groupe personnel.
  - Depuis le groupe, cliquer sur `New project` > `Create blank project`.
  - Nom du projet : `DOP Python`.
  - Identifiant du projet (laisser par défaut) : `dop-python`.
- Ajouter `blueur` et `GeraudSilvestri` comme membre du projet.
  - Trouvez le bon [rôle](https://docs.gitlab.com/ee/user/permissions.html) qui permet de mettre à jour les merge requests (MR) sans pouvoir changer les paramètres du projet.
- Protéger la branche `main`.
  - Personne ne doit pouvoir pousser directement sur la branche.
  - Seuls les mainteneurs peuvent fusionner des MR.
- Cloner le répertoire sur votre machine.
  - Vérifier que vous ne pouvez pas pousser directement sur la branche `main`.
- Créer une issue (ticket) dans le projet.
  - Titre : `Rendu labo 01`.
  - Assigner l'issue à soi-même.
- Sur son ordinateur, créer une nouvelle branche `feature/01-tools` et aller dessus.
  - Créer un projet Vue 3 dans le dossier `/frontend`.
    - https://vuejs.org/guide/quick-start.html#creating-a-vue-application
    - Depuis la racine du répertoire, exécutez `npm create vue@latest`.
      - Project name: `frontend`
      - Add TypeScript? `Yes`
      - Add JSX Support? `No`
      - Add Vue Router for Single Page Application development? `No`
      - Add Pinia for state management? `No`
      - Add Vitest for Unit testing? `No`
      - Add an End-to-End Testing Solution? `No`
      - Add ESLint for code quality? `Yes`
      - Add Prettier for code formatting? `Yes`
    - Installer les dépendances avec `npm install`
    - Tester le serveur de développement avec `npm run dev`
  - Créer un commit avec les changements et pousser la branche sur GitLab.
  - Créer un projet Poetry dans le dossier `/backend`.
    - https://python-poetry.org/docs/basic-usage/#project-setup
    - Depuis la racine du répertoire, exécuter `poetry new backend`.
    - Depuis le dossier `/backend`, installer [FastAPI](https://fastapi.tiangolo.com/).
      - https://fastapi.tiangolo.com/#installation
      - `poetry add fastapi uvicorn[standard]` ou `poetry add fastapi "uvicorn[standard]"` (pour zsh).
      - S'il y a le dossier `/backend/backend` :
        - Créer un fichier `main.py` dans `/backend/backend` avec le code ci-dessous.
        - Tester le serveur de développement avec `poetry run uvicorn backend.main:app --reload`.
      - S'il y a le dossier `/backend/src/backend` :
        - Créer un fichier `main.py` dans `/backend/src/backend` avec le code ci-dessous.
        - Tester le serveur de développement avec `poetry run uvicorn src.backend.main:app --reload`.
      - Voir la documentation de l'API à l'adresse http://127.0.0.1:8000/docs
    - Ajouter un fichier `.gitignore` adapté au projet.
- Créer un commit avec les changements et pousser la branche sur GitLab.
- Créer une MR pour fusionner la branche feature dans `main`.
  - Lier la MR à l'issue `Rendu labo 01` (plusieurs façons possibles).
  - Assigner la MR à soi-même (assignee).
  - Demander une revue de code à `GeraudSilvestri` (reviewer).
- Essayer l'outils de suivi du temps de GitLab pour ses estimations.
  - `/estimate 2h` pour estimer le temps nécessaire pour la MR.
  - `/spend 1h30m` pour indiquer le temps réellement passé.

```python title="/backend/backend/main.py" showLineNumbers
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

:::info[Question rapport]

- Indiquer le lien vers la MR dans le rapport.
- Quelles sont les bonnes pratiques pour les messages de commit?

:::

## Configuration

- Configurer son ordinateur pour qu'il affiche les extensions des fichiers.
  - macOS : Finder > Préférences > Avancé > Cocher "Afficher toutes les extensions de fichier".
  - Windows : Explorer > Affichage > Options > Modifier les options des dossiers et de recherche > Affichage > Décocher "Masquer les extensions des fichiers dont le type est connu".
- Configurer son ordinateur pour qu'il affiche les fichiers cachés.
  - macOS : Finder > <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>.</kbd>.
  - Windows : Explorer > Affichage > Options > Modifier les options des dossiers et de recherche > Affichage > Cocher "Afficher les fichiers, dossiers et lecteurs cachés".

## Présentation

- Écrire une brève présentation de soi avec notamment
  - Son parcours académique
  - Ses centres d'intérêt
  - Ses compétences en informatique et en DevOps
  - Pourquoi avoir choisi ce cours/cette formation
  - Ses attentes pour le cours
  - &hellip;
- Rendre la présentation au format PDF nommé `presentation-prenom-nom.pdf` (avec votre prénom et nom, tout en minuscule, sans accent, sans espace avec des tirets) sur [Cyberlearn](https://cyberlearn.hes-so.ch/mod/assign/view.php?id=2361540).

### Bonus : Réécriture de Git

- Cloner le répertoire [Git Exercise](https://github.com/blueur/git-exercises)
- Faire les exercices indiqués dans le README
