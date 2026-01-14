# 🇩🇿 Nouveau Système d’Immatriculation Algérien  
### Proposition Technique + Générateur Automatique

##  Objectif
Ce dépôt propose un nouveau système d'immatriculation algérien **neutre, moderne et non régionaliste**, basé sur trois parties :

```
[Type] - [Année] - [Numéro Base26]
```

💡 Le but est d'éliminer les codes de wilayas, source de régionalisme, et de proposer un système plus compact, plus élégant et compatible informatiquement.

---

## 🧩 Structure du Matricule

### 1. Type de véhicule (1 chiffre)
| Type | Code |
|------|------|
| Véhicule léger | 0 |
| Camion | 1 |
| Moto | 2 |
| Bus | 3 |
| … jusqu'à 9 | - |

### 2. Année de fabrication
Format 4 chiffres (ex : 1998, 2024, 2084).

### 3. Numéro de série en base 26
Conversion du numéro en alphabet :

```
0 = A
1 = B
...
25 = Z
```

On remplace la conversion hexadécimale par une conversion **base 26 alphabétique**.

---

## 📘 Exemple

Numéro de série : 152347  
→ Conversion base 26 : **AFBXQD**

Matricule final :

```
0-2024-AFBXQD
```

---

## 🐍 Générateur Python

Le script `generator.py` permet d’automatiser la génération des matricules.



##  Exemples générés

Voir `examples/sample_plates.txt`.

---
##  Bénéfices du Nouveau Système d’Immatriculation

Ce système d’immatriculation modernisé apporte plusieurs avantages majeurs par rapport au format actuel en Algérie :

###  1. Suppression totale du régionalisme
Le nouveau format ne contient **aucun code de wilaya**, supprimant ainsi :
- les stéréotypes liés aux immatriculations,
- les jugements sociaux basés sur l’origine,
- les discriminations implicites dans la circulation.

C’est un système **national unifié**, sans référence géographique.

---

###  2. Format compact, lisible et élégant
L’utilisation d’un numéro de série **en Base-26 alphabétique** permet :
- de réduire la longueur des chaînes numériques,
- d’obtenir des identifiants esthétiques et homogènes,
- de faciliter la lecture visuelle.

Un matricule comme `5-2030-AZRTYU` est court, propre et facilement mémorisable.

---

###  3. Standard moderne compatible avec les systèmes informatiques
Le format 0–9 / AAAA / Base-26 :
- est facile à encoder,
- évite les collisions,
- est compatible avec les schémas de bases de données,
- facilite la génération automatique (scripts, API, systèmes nationaux).

Cela en fait un système parfaitement adapté à la **numérisation administrative**.

---

###  4. Grande capacité d’identifiants
La conversion Base-26 assure une **capacité énorme**, beaucoup plus grande qu’un simple numéro décimal :
- 6 lettres → 26⁶ ≈ 308 millions de combinaisons  
- 5 lettres → 26⁵ ≈ 11 millions de combinaisons  

Cela couvre largement les immatriculations nationales pour plusieurs décennies.

---

###  5. Neutralité et anonymisation
Le nouveau système :
- ne révèle **ni la région**,  
- ni le centre d'immatriculation,  
- ni des informations personnelles indirectes.

Cela renforce la **protection de la vie privée** des citoyens.

---

###  6. Transition possible depuis l’ancien système
Le numéro de série peut être converti à partir de l’ancien, ce qui permet :
- une migration progressive et ordonnée,
- une compatibilité avec les bases de données existantes,
- l’utilisation d’outils de mapping (ancien → nouveau).

---

###  7. Cohérence nationale et modernisation de l’image du pays
L’utilisation d’un système moderne et neutre :
- uniformise les plaques,
- améliore l’esthétique globale du parc automobile,
- aligne l’Algérie avec les bonnes pratiques internationales.

---

Ce système peut donc constituer une base solide pour une **réforme nationale**, une **expérimentation académique**, ou un **projet administratif pilote**.


##  Licence

Ce projet est sous licence MIT. Voir `LICENSE`.

---

##  Contribution

Toute amélioration ou optimisation du système est bienvenue.  
Merci de contribuer via des *pull requests* !

