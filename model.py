import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import os
import xlrd
import cv2
import HandDataCollecter
import mediapipe as mp
import numpy as np

local_path = (os.path.dirname(os.path.realpath('__file__')))
file_name = ('a data.csv')
data_path = os.path.join(local_path, file_name)
print(data_path)
df = pd.read_csv(r'' + data_path)

print(df)

units_in_data = 28

titles = []
for i in range(units_in_data):
    titles.append("unit-" + str(i))
X = df[titles]
y = df['letter']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)
from sklearn.metrics import accuracy_score, classification_report

# Random Forest
clf = RandomForestClassifier(n_estimators=30)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('Random Forest Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print("Random Forest classification_report")
print(classification_report(y_pred, y_test, labels=None))

# KNN
clf1 = KNeighborsClassifier()
clf1.fit(X_train, y_train)
y_pred = clf1.predict(X_test)
print('KNN Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print("KNN classification_report")
print(classification_report(y_pred, y_test, labels=None))

# SVM
from sklearn.svm import SVC
clf2 = SVC()
clf2.fit(X_train, y_train)
y_pred = clf2.predict(X_test)
print('SVM Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print("SVM classification_report")
print(classification_report(y_pred, y_test, labels=None))
