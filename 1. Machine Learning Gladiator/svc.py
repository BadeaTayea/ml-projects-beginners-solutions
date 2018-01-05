import pandas as pd
import numpy as np
import sklearn as sk

data_raw = pd.read_csv('data/adult.data.txt')

from numpy import unique

def category_to_numerical(column):
    categories = unique(column).tolist() # finding out all categorical features
    features = []
    for category in column:
        numercial_value =  categories.index(category) # use the index as a new numerical value
        features.append(numercial_value)
    return features

for column in data_raw.columns:
    if not np.issubdtype(data_raw[column].dtype, np.number):
        data_raw[column] = pd.DataFrame({column: category_to_numerical(data_raw[column])})

def split_features_labels(data):
    labels = data['income']
    features = data.drop('income',axis=1)
    return features, labels

def split_train_test(features, labels, test_size):
    total_test_size = int(len(features) * test_size)
    train_features = features[total_test_size:]
    train_labels = labels[total_test_size:]
    test_features = features[:total_test_size]
    test_labels = labels[:total_test_size]
    return train_features, train_labels, test_features, test_labels

features, labels = split_features_labels(data_raw)
train_features, train_labels, test_features, test_labels = split_train_test(features, labels, 0.15)

print('Train set length:',len(train_features))
print('Test set length:',len(test_features))

from sklearn.metrics import accuracy_score

from sklearn import svm

from time import time

svm_classifier = svm.SVC()

t_start = time()
svm_classifier.fit(train_features, train_labels)
print('Finished building machine learning model. Training time:', round(time()-t_start, 3), 's')

print("Accuracy: ", accuracy_score(svm_classifier.predict(test_features), test_labels))
