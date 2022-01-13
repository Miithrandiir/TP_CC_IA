# Evaluation finale
## Simon HEBAN

# Analyse des données

Après analyse des données il y a:
 - 101 entrées
 - 26 colonnes
 
Les colonnes A et B sont très stable donc ne servira pas à apprendre, on peut donc les retirer.

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

## Type de problème

Après analyse on se rend compte que le problème est un problème de **classification**

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