# Imports
import os
import sys
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
from collections import Counter
import predictor
from flask import Flask
import shap

logreg = LogisticRegression()
mysvm = svm.SVC()
mlc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)

app = Flask(__name__)


@app.route('/rerun')
def rerun_lregression():
    data = pd.read_csv('mydataset.csv')
    data['class'] = data['class'].map({-1: 0, 1: 1})
    X = data.iloc[:, 1:31].values.astype(int)
    y = data.iloc[:, 31].values.astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=np.random.seed(7))
    logreg.fit(X_train, y_train)
    mysvm.fit(X_train, y_train)
    mlc.fit(X_train, y_train)
    printer = 'Accuracy score of the Logistic regression '
    print(printer + ': {0:.2f}%'.format(accuracy_score(y_test,
                                                       logreg.predict(X_test)) * 100))
    printer = 'Accuracy score of the SVM '
    print(printer + ': {0:.2f}%'.format(accuracy_score(y_test,
                                                       mysvm.predict(X_test)) * 100))
    printer = 'Accuracy score of the ANN '
    print(printer + ': {0:.2f}%'.format(accuracy_score(y_test,
                                                       mlc.predict(X_test)) * 100))
    print('Regression Models updated!')
    return "Regression Models Updated!!"

# @app.route('/feedback/')
# def feedback():
    

@app.route('/predict/')
def predict():
    # get body of the data from the request
    # data = request.get_json()
    # url = data.url
    # favicon = data.favicon
    pass
    # predictor.send(url, favicon, reqURL, anchorURL, linkURL, SFH, mailTO, webFWD, sbc, disRC, popup, iFrame)
