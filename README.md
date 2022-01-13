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

KNN sans suppression des caractéristiques

```
~ KNN Algorithm ~
KNN Train score:  0.31343283582089554
KNN Test Score:  0.38235294117647056
Matrice de confusion de KNN 
 [[13  0  0  1  0  0  1]
 [ 5  0  1  1  0  0  0]
 [ 0  0  0  0  0  0  0]
 [ 2  0  0  0  0  0  0]
 [ 2  0  0  0  0  0  0]
 [ 3  1  0  0  0  0  0]
 [ 4  0  0  0  0  0  0]]
```
KNN avec suppression des caractéristiques
```
~ KNN Algorithm ~
KNN Train score:  0.8955223880597015
KNN Test Score:  0.9411764705882353
Matrice de confusion de KNN 
 [[15  0  0  0  0  0  0]
 [ 0  6  0  0  0  0  0]
 [ 0  1  0  1  0  0  0]
 [ 0  0  0  4  0  0  0]
 [ 0  0  0  0  1  0  0]
 [ 0  0  0  0  0  3  0]
 [ 0  0  0  0  0  0  3]]
```
*Note : Après expérimentation, il convient d'utiliser pour k (la valeur des k plus proches voisins) la valeur 8. Cette valeur a permit d'obtenir le meilleur apprentissage*

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
*Note: on remarque que l'arbre de décision n'est pas influencé par les caractéristiques non corrélées. En effet, l'arbre se base sur l'entropie qui permet de s'abstraire d'une certaine correlation entre les caractéristiques.*
### Neuronal Network Algorithm
KNN sans suppression des caractéristiques
```
~ Neural Network Algorithm ~
NN Train score:  0.9552238805970149
NN Test Score:  0.23529411764705882
Matrice de confusion de NN 
 [[6 1 4 2 0 2]
 [4 1 2 0 0 0]
 [2 0 0 0 0 0]
 [0 1 1 0 0 0]
 [0 1 1 1 0 1]
 [2 1 0 0 0 1]]
```
KNN avec suppression des caractéristiques
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
*Note: après suppression des caractéristiques non utiles on remarque que le score sur la base de tests sont nettement meilleur !*