# Imports
import sys
import warnings
import art
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from collections import Counter

# print(art.text2art('PHISHING WEBSITE DETECTION', font="cybermedium"))
warnings.filterwarnings('ignore')
data = pd.read_csv('mydataset.csv')
# print(data.shape)
print(data.head(5))
# print(data.columns)

classes = Counter(data['class'].values)
# print(classes.most_common())
class_dist = pd.DataFrame(classes.most_common(), columns=[
                          'Class', 'Num_Records'])
# print(class_dist.T)

# plt.style.use('ggplot')
# subplot = class_dist.groupby('Class')['Num_Records'].sum().plot(kind='barh', width=0.2, figsize=(10, 8))
# subplot.set_title('Class distribution of websites', fontsize=15)
# subplot.set_xlabel('Number of Observations', fontsize=14)
# subplot.set_ylabel('Class', fontsize=14)
#
# for i in subplot.patches:
#     subplot.text(i.get_width() + 0.1, i.get_y() + 0.1, str(i.get_width()), fontsize=11)
# plt.show()

# print(data.describe().T)

data['class'] = data['class'].map({-1: 0, 1: 1})
print(data['class'].unique())

# print(data.isna().sum())
X = data.iloc[:, 1:31].values.astype(int)
y = data.iloc[:, 31].values.astype(int)
print('X: ', X)
print('Y: ', y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=np.random.seed(7))

logreg = LogisticRegression()
print(logreg.fit(X_train, y_train))

printer = 'Accuracy score of the Logistic regression classifier with default hyperparameter value'
print(printer + 's: {0:.2f}%'.format(accuracy_score(y_test,
      logreg.predict(X_test)) * 100))
