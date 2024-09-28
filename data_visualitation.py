import ssl
from statistics import correlation
from xml.etree.ElementInclude import include

import certifi
import seaborn as sns
import matplotlib.pyplot as plt
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
def generate_seaborn_plo():
    context = ssl.create_default_context()
    print(sns.__version__)
    df = sns.load_dataset('iris')
    print(df.head())
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
    plt.savefig('static/img/seaborn_plot.png')
    plt.close()

    df_numeric = df.select_dtypes(include="number")

    # mapa de calor

    plt.figure(figsize=(10, 6))
    correlation_matrix = df_numeric.corr()
    sns.heatmap(correlation_matrix, annot= True, cmap="coolwarm")
    plt.savefig('static/img/seaborn_heatmap.png')


#boxplot

    plt.figure(figsize=(10, 6))
    sns.boxplot(x="species", y="petal_length", data=df)
    plt.savefig('static/img/seaborn_boxplot.png')
    plt.close()


#pairplot

    sns.pairplot(df, hue= "species")
    plt.savefig('static/img/seaborn_pairplot.png')
    plt.close()


