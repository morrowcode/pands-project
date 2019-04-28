Originally published at UCI Machine Learning Repository, the 'Iris Data Set', is a small dataset from 1936 often used for testing out machine learning algorithms and visualizations. In the data set, each row of the table represents an iris flower, including its species and dimensions of its botanical parts, sepal and petal, in centimeters. There are 150 samples taken broken into 5 columns, sepal-length, sepal-width, petal-length, petal-width and class. An example of this is shown below indicating the first 5 samples taken with associated titles. This is taken from the python output.

sepal-length  sepal-width  petal-length  petal-width        class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa

To break this data down and understand it a little, we can run a 'description' which will indicate the number of samples for each value (sepal-length, width etc.), shown below. Furthermore, it will indicate the mean, standard deviation, min and max, upper and lower quartiles and median of the data set.
From reviewing this we can see the highest standard deviation value is in the petal length indicating the highest spread of values. This appears to be true, as we can see from the minimum and maximum values petal length has a spread of 5.9 cm across the samples. Sepal Width has the lowest spread of values with a standard deviation of 0.43 

       sepal-length  sepal-width  petal-length  petal-width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
We can see that in the 150 samples of the irises, there are 50 samples attributed to each class: Iris-setosa, Iris-Veriscolor and Iris-virginica.
class
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
dtype: int64

As we can see from the Box and Whisker Plot in the first graph showing the spread of lengths in centimetres for each attribute the sepal-width has the least spread and petal-length has the greatest spread of measured lengths.

To break this down further, using the next graph: The Scatter Plot Matrix, we can see a number o graphs that illustrate the various attributes broken down by their Iris class. What is immediately apparent is the dissimilarity of the Iris-setosa’s petal dimensions (length and width) to the other 2 irises. The iris-setosa sample population is for both the length and width of the petal is significantly different with almost no overlap in population between the setosa and the versicolor and virginica. Even between the versicolor and virginica in petal length and width there is distinction in population. This would explain the significant spread in values in the aforementioned boxplot. The sepal dimensions do show much more over lap in dimensions, but, as illustrated still indicated distinct populations.
In the next graph we can wee the sepal length vs width broken down by Iris class. Here we can see the distinction of the setosa to the other two Irises. We can also see the trend the versicolor appears to have a smaller length and width by comparison to the virginica. 

In the Petal Length vs Width graph, we and see the setosa again being significantly different and there being an obvious difference between the versicolor and virginica.

In the following 4 Violin plots we see each dimension broken down by class. In the first we see the sepal length. This again indicates a high concentration of setosa and a large virginica spread.
Secondly, we see sepal length, showing a much higher correlation in values across all classes, with setosa showing definite distinction in size.
Next, we see petal length where the setosa population is highly concentrated with definite spread of the other two irises.
Finally, we see the petal width indicating setosa again being highly similar and the other 2 irises showing significant spread.

References
1. Iris flower data set - Wikipedia https://en.wikipedia.org/wiki/Iris_flower_data_set
2. UCI Machine Learning Repository: Iris Data Set https://archive.ics.uci.edu/ml/datasets/iris
3. Watson Analytics Use Case: The Iris Data Set – IBM Analytics ... https://www.ibm.com/communities/.../watson-analytics-use-case-the-iris-data-set/
4. Official seaborn tutorial: https://seaborn.pydata.org/tutorial.html
5. Visualization with Seaborn: https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
6. A Beginner's Guide to Unsupervised learning: https://www.kaggle.com/bbhatt001/a-beginner-s-guide-to-unsupervised-learning