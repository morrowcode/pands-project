###


import csv
import scipy
import numpy
import matplotlib
import pandas
import seaborn as sns

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names = names)

# shape
print(dataset.shape)

# head
print(dataset.head())

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# box and whisker plots 
sns.boxplot(data=dataset, orient="h", palette="husl").set_title('Box and Whisker Plot')
plt.show()

# scatter plot matrix
g = sns.pairplot(dataset, hue='class', palette="husl")
g.add_legend()
g.fig.suptitle('Scatter Plot Matrix')
plt.show()

# sfacet - epal length vs width
a = sns.FacetGrid(dataset,hue='class', palette='husl')
a.map(plt.scatter,'sepal-length','sepal-width')
a.add_legend()
a.fig.suptitle('Sepal Length vs Width')
plt.show()

# facet - petal length vs width
b = sns.FacetGrid(dataset,hue='class', palette='husl')
b.map(plt.scatter,'petal-length','petal-width')
b.add_legend()
b.fig.suptitle('Petal Length vs Width')
plt.show()

# violin plots - class vs attribute
sns.violinplot(x='sepal-length', y='class', data=dataset, inner='stick', palette='husl')
plt.show()
sns.violinplot(x='sepal-width', y='class', data=dataset, inner='stick', palette='husl')
plt.show()
sns.violinplot(x='petal-length', y='class', data=dataset, inner='stick', palette='husl')
plt.show()
sns.violinplot(x='petal-width', y='class', data=dataset, inner='stick', palette='husl')
plt.show()