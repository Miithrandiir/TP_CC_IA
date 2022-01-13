# Evaluation finale
## Simon HEBAN

# Analyse des données

Après analyse des données il y a:
 - 101 entrées
 - 26 colonnes
 
Les colonnes A et B sont des nombres qui ne varie pas donc ne servira pas à apprendre, on peut donc les retirer.

On constate aussi que les exemples ne sont pas homogènes et que certaines classes seront difficiles à apprendre. 
Les classes 6 (8 exemples), 3(5 exemples) et 5(4 exemples)

## Matrice de corrélation

Positivement corrélé avec la classe Z:
 - Le descripteur F qui semble être le plus corrélé
 - Le descripteur I
 - Le descripteur N

Négativement corrélé avec la classe Z:
 - Le descripteur L qui semble le plus influer négativement notre classe
 - Le descripteur G
 
## Type de problème (Classification)

Après analyse on se rend compte que le problème est un problème de **classification**. Nous avons déjà des exemples étiquetés nous sommes donc face à un apprentissage supervisé.

## Suppressions de caractéristiques

Pendant le premier test on se rend compte que les performances des algorithmes KNN et Neuronal Network ne sont pas du tout bonne. (< 20%)
Il y a un tri à faire dans les caractéristiques ! 

En effet, après analyses de la matrice de corrélation on peut constater que certaines caractéristiques ne discrimine pas notre classe Z. On va pouvoir enlever certaines caractéristiques telles que :
 - A
 - B
 - C
 - E
 - H
 - J
 - O
 - P
 - R
 - T
 - U
 - V
 - W
 - X
 - Y

### Résultat lié à cette suppression

On remarque tout de suite une nette amélioration des algorithmes KNN et Neuronal Network. 
En effet, il n'était pas utile d'apprendre des caractéristiques qui ne discriminait pas notre classe !

# Résultat (Partie Apprentissage & Conseils)

### KNN Algorithm
```
~ KNN Algorithm ~
KNN Train score:  0.8656716417910447
KNN Test Score:  0.9117647058823529
Matrice de confusion de KNN 
 [[15  0  0  0  0  0  0]
 [ 0  7  0  0  0  0  0]
 [ 0  1  0  0  0  0  0]
 [ 0  0  0  4  0  0  0]
 [ 0  0  0  2  0  0  0]
 [ 0  0  0  0  0  2  0]
 [ 0  0  0  0  0  0  3]]
```
*note : Après expérimentation, il convient d'utiliser pour k (la valeur des k plus proches voisins) la valeur 8. Cette valeur a permit d'obtenir le meilleur apprentissage*

### Tree Algorithm
```
Tree Train score:  0.9552238805970149
Tree Test Score:  0.9705882352941176
Matrice de confusion de Tree 
 [[15  0  0  0  0  0  0]
 [ 0  7  0  0  0  0  0]
 [ 0  0  1  0  0  0  0]
 [ 0  0  0  4  0  0  0]
 [ 0  0  1  0  1  0  0]
 [ 0  0  0  0  0  2  0]
 [ 0  0  0  0  0  0  3]]
```

### Neuronal Network Algorithm
```
~ Neural Network Algorithm ~
NN Train score:  0.9552238805970149
NN Test Score:  0.9705882352941176
Matrice de confusion de NN 
 [[15  0  0  0  0  0  0]
 [ 0  7  0  0  0  0  0]
 [ 0  0  1  0  0  0  0]
 [ 0  0  0  4  0  0  0]
 [ 0  0  0  1  1  0  0]
 [ 0  0  0  0  0  2  0]
 [ 0  0  0  0  0  0  3]]
```