import pandas
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix


def label_encode(data, col: str):
    # Transforme un type catégorie en entier
    le = LabelEncoder()
    # On récupère tous les noms de catégories possibles
    unique_values = list(data[col].unique())
    le_fitted = le.fit(unique_values)
    # On liste l'ensemble des valeurs
    values = list(data[col].values)
    # On transforme les catégories en entier
    values_transformed = le.transform(values)
    # On fait le remplacement de la colonne dans le dataframe d'origine
    data[col] = values_transformed


def analyzeData():
    data = read_csv("./data/dataCCfinal.csv")  # data devient un DataFrame
    print("~ Analyse de données ~")
    print("nombre d'exemples : " + str(len(data)))
    print("nombre de caractéristiques : " + str(len(data.columns)))
    print("nombre d'exemples de chaques classes :")
    for classe in data.columns:
        print("Nombre d'exemples de " + str(classe) + " : " + str(len(data[classe])))
    data.shape  # Dimension du dataframe
    data.info()  # résumé rapide des données
    print(data.describe())  # statistiques sur différentes tendances sur les données.
    sn.heatmap(data.corr(), cmap="PiYG", vmax=0.5)
    print("Nombre d'exemples de chaques classes : ")
    print(data.value_counts("Z"))
    plt.show()
    label_encode(data, "C")
    x = data
    y = data["Z"]
    del x["A"]
    del x["B"]
    del x["C"]
    del x["E"]
    del x["H"]
    del x["J"]
    del x["O"]
    del x["P"]
    del x["R"]
    del x["T"]
    del x["U"]
    del x["V"]
    del x["W"]
    del x["X"]
    del x["Y"]
    del x["Z"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    return x_train, x_test, y_train, y_test


def knn(x_train, x_test, y_train, y_test):
    print("~ KNN Algorithm ~")
    classifier = KNeighborsClassifier(n_neighbors=8)
    classifier.fit(x_train, y_train)
    print("KNN Train score: ", classifier.score(x_train, y_train))
    print("KNN Test Score: ", classifier.score(x_test, y_test))
    print("Matrice de confusion de KNN \n", confusion_matrix(y_test, classifier.predict(x_test)))


def tree(x_train, x_test, y_train, y_test):
    print("~ Tree Algorithm ~")
    classifier = DecisionTreeClassifier(criterion='entropy')
    classifier.fit(x_train, y_train)
    print("Tree Train score: ", classifier.score(x_train, y_train))
    print("Tree Test Score: ", classifier.score(x_test, y_test))
    print("Matrice de confusion de Tree \n", confusion_matrix(y_test, classifier.predict(x_test)))


def neural_network(x_train, x_test, y_train, y_test):
    print("~ Neural Network Algorithm ~")
    classifier = MLPClassifier()
    classifier.fit(x_train, y_train)
    print("NN Train score: ", classifier.score(x_train, y_train))
    print("NN Test Score: ", classifier.score(x_test, y_test))
    print("Matrice de confusion de NN \n", confusion_matrix(y_test, classifier.predict(x_test)))


x_train_d, x_test_d, y_train_d, y_test_d = analyzeData()
knn(x_train_d, x_test_d, y_train_d, y_test_d)
tree(x_train_d, x_test_d, y_train_d, y_test_d)
neural_network(x_train_d, x_test_d, y_train_d, y_test_d)
