# Leçon 7.3 — Environnements virtuels et `pip`

⏱ 45 min · 🎯 Débutant+ · 📦 Prérequis : leçon 7.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Un environnement par projet, une liste de dépendances : tu vas travailler comme dans une vraie équipe de développement.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Installer des paquets externes avec `pip`
- Créer et activer un **environnement virtuel** (`venv`)
- Sauvegarder et recréer la liste de tes dépendances (`requirements.txt`)
- Expliquer pourquoi on isole chaque projet

---

## 1. Le problème

Le projet A a besoin de `pandas 2.0`, le projet B de `pandas 3.0`. Si on installe tout au même endroit, l'un des
deux casse. Et si tu envoies ton projet à un collègue, comment sait-il quoi installer ? La réponse : un
**environnement virtuel** par projet, et un fichier qui liste les dépendances.

## 2. L'idée en images

Un environnement virtuel est une **boîte à outils privée** pour un projet :

```
 Python du système
   ├── projet_A/venv  → pandas 2.0, requests
   └── projet_B/venv  → pandas 3.0, fastapi
```

Chaque boîte a ses propres versions, sans conflit.

## 3. Pas à pas

### 3.1 `pip` : le gestionnaire de paquets

```powershell
python -m pip --version
python -m pip install requests          # installer
python -m pip install "requests>=2.30"  # avec contrainte de version
python -m pip install --upgrade requests
python -m pip uninstall requests
python -m pip list                      # paquets installés
python -m pip show requests             # détails d'un paquet
```

On écrit `python -m pip` (plutôt que `pip` seul) pour être sûr d'utiliser **le pip du bon Python**.
Les paquets viennent de **PyPI** (<https://pypi.org>), le catalogue public.

### 3.2 Créer un environnement virtuel

À la racine de ton projet :

```powershell
python -m venv venv
```

Cela crée un dossier `venv` contenant une copie isolée de Python.

### 3.3 L'activer

| Système | Commande |
|---|---|
| Windows (PowerShell) | `.\venv\Scripts\Activate.ps1` |
| Windows (cmd) | `venv\Scripts\activate.bat` |
| Linux / macOS | `source venv/bin/activate` |

Le terminal affiche alors `(venv)` au début de la ligne. Désactivation : `deactivate`.

> 💡 Sous PowerShell, si l'activation est bloquée : `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

### 3.4 Installer dans l'environnement

Une fois activé, `python -m pip install ...` installe **uniquement** dans `venv`.

### 3.5 Figer et recréer les dépendances

```powershell
python -m pip freeze > requirements.txt          # sauvegarde les versions exactes
python -m pip install -r requirements.txt        # recrée l'environnement ailleurs
```

Bonne pratique : tenir **deux fichiers** :
- `requirements.in` : tes dépendances **directes** (`requests`, `pandas`) ;
- `requirements.txt` : toutes les versions exactes résolues.

### 3.6 Ne jamais envoyer `venv` sur Git

Le dossier `venv` est lourd et propre à ta machine. Ajoute-le au fichier **`.gitignore`** :

```
venv/
__pycache__/
*.pyc
```

### 3.7 Outils modernes (pour plus tard)

`uv` (très rapide), `poetry`, `pipx` (outils en ligne de commande). Le principe reste identique : isoler et figer.

### 3.8 Mise à jour et sécurité

```powershell
python -m pip list --outdated
python -m pip install --upgrade requests
```

Des paquets obsolètes peuvent contenir des **failles de sécurité** : mets-les à jour régulièrement et, en
entreprise, utilise un scanner comme `pip-audit`.

## 4. ⚠️ Pièges courants

**Installer sans activer l'environnement** : le paquet va dans le Python global.

**`pip` et `python` de deux installations différentes** → utilise toujours `python -m pip`.

**Mélanger des versions** : après avoir copié un projet, recrée un `venv` et réinstalle depuis `requirements.txt`.

**Installer un paquet inconnu** : vérifie le nom exact (risque d'attaque par fautes de frappe, *typosquatting*).

## 5. À retenir

- Un `venv` **par projet** : `python -m venv venv`, puis activation.
- `python -m pip install`, `freeze`, `install -r requirements.txt`.
- `venv/` dans `.gitignore`.
- Vérifie les noms de paquets et mets à jour régulièrement.

## 6. Exercices

Fichier : [`exercices/ex26_venv_et_pip.py`](../exercices/ex26_venv_et_pip.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex26_venv_et_pip.py -v
```

## 7. Quiz

1. Pourquoi un environnement virtuel par projet ?
2. Quelle commande crée un environnement nommé `venv` ?
3. Comment recréer l'environnement d'un collègue ?
4. Pourquoi ne pas versionner le dossier `venv` ?

<details>
<summary>Réponses</summary>

1. Pour isoler les versions des paquets et éviter les conflits entre projets.
2. `python -m venv venv`
3. Créer un `venv`, l'activer, puis `python -m pip install -r requirements.txt`.
4. Il est volumineux, dépend de la machine et peut être recréé à partir de `requirements.txt`.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais isoler tes projets et installer des bibliothèques proprement. C'est une habitude de professionnel.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 7.4 — Écrire ses propres modules et packages](l27_ecrire_ses_modules.md).
<!-- /cadre:fin -->
