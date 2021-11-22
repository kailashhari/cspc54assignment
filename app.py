# Imports
# import os
# import sys
# import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
# from collections import Counter
from pymongo import MongoClient
import predictor
from flask import Flask, request
import shap
from csv import writer
import json

logreg = LogisticRegression()
mysvm = svm.SVC()
mlc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.aiml
collection = db.globals
# print(db.list_collection_names())

@app.route('/globals', methods=['GET'])
def get_globals():
    collection.drop()
    collection.insert_one({"name": "REQUESTURL_MIN", "value": "22"})
    collection.insert_one({"name": "REQUESTURL_MAX", "value": "66"})
    collection.insert_one({"name": "ANCHOR_MIN", "value": "31"})
    collection.insert_one({"name": "ANCHOR_MAX", "value": "67"})
    collection.insert_one({"name": "LINKS_MIN", "value": "32"})
    collection.insert_one({"name": "LINKS_MAX", "value": "81"})
    collection.insert_one({"name": "DOMAIN_AGE", "value": "4320"})
    collection.insert_one({"name": "WORLD_RANK", "value": "100000"})
    globals = list(collection.find())

    # bson to json
    json_globals = {}
    for global_ in globals:
        json_globals[global_['name']] = global_['value']

    return json_globals

@app.route('/rerun')
def rerun_lregression():
    data = pd.read_csv('mydataset.csv')
    data.drop_duplicates(keep=False,inplace=True)
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

@app.route('/feedback', methods=['GET'])
def feedback():
    url = request.args.get('url')
    print(url)
    favicon = request.args.get('favicon')
    requestURL = request.args.get('requestURL')
    AnchorURL = request.args.get('AnchorURL')
    LinksInScript = request.args.get('LinksInScript')
    ServerFormHandler = request.args.get('ServerFormHandler')
    InfoEmail = request.args.get('InfoEmail')
    StatusBarCust = request.args.get('StatusBarCust')
    DisableRightClick = request.args.get('DisableRightClick')
    UsingPopupWindow = request.args.get('UsingPopupWindow')
    IframeRedirectio = request.args.get('IframeRedirectio')
    phishing = request.args.get('phishing')
    if phishing == "Yes":
        phishing = 1
    else:
        phishing = 0
    print(phishing)
    fulldata = predictor.predictor(url,favicon,requestURL,AnchorURL,LinksInScript,ServerFormHandler,InfoEmail,StatusBarCust,DisableRightClick,UsingPopupWindow,IframeRedirectio)
    print(fulldata)
    fulldata += [phishing]
    with open('mydataset.csv', "r+") as csvfile:
        nrecords = len(csvfile.readlines()) - 1
        mywriter = writer(csvfile)
        mywriter.writerow([nrecords] + fulldata)
        csvfile.close()
    return "!"
    

@app.route('/predict',methods=['GET'])
def predict():
    url = request.args.get('url')
    favicon = request.args.get('favicon')
    requestURL = request.args.get('requestURL')
    AnchorURL = request.args.get('AnchorURL')
    LinksInScript = request.args.get('LinksInScript')
    ServerFormHandler = request.args.get('ServerFormHandler')
    InfoEmail = request.args.get('InfoEmail')
    StatusBarCust = request.args.get('StatusBarCust')
    DisableRightClick = request.args.get('DisableRightClick')
    UsingPopupWindow = request.args.get('UsingPopupWindow')
    IframeRedirectio = request.args.get('IframeRedirectio')
    rerun_lregression()
    fulldata = predictor.predictor(url,favicon,requestURL,AnchorURL,LinksInScript,ServerFormHandler,InfoEmail,StatusBarCust,DisableRightClick,UsingPopupWindow,IframeRedirectio)
    result = mlc.predict([fulldata])
    print(result[0])
    return str(result[0])
