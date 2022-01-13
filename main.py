from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import seaborn as sn


def analyzeData():
    data = read_csv("./data/dataCCfinal.csv") # data devient un DataFrame
    print("~ Analyse de données ~")
    print("nombre d'exemples : " + str(len(data)))
    print("nombre de caractéristiques : " + str(len(data.columns)))
    print("nombre d'exemples de chaques classes :")
    for classe in data.columns:
        print("Nombre d'exemples de " + str(classe) + " : " + str(len(data[classe])))
    data.shape #Dimension du dataframe
    data.info() #résumé rapide des données
    print(data.describe()) #statistiques sur différentes tendances sur les données.
    sn.heatmap(data.corr(), cmap="PiYG", vmax=0.5)
    print("Nombre d'exemples de chaques classes : ")
    print(data.value_counts("Z"))
    plt.show()

    x = data
    y = data["Z"]
    del x["A"]
    del x["B"]
    x_train, x_test, y_train, y_test = train_test_split(x,y)

    return x_train, x_test, y_train, y_test


def knn(x_train, x_test, y_train, y_test):
    print("~ KNN Algorithm ~")
    regressor = KNeighborsRegressor(n_neighbors=3)
    regressor.fit(x_train, y_train)




analyzeData()