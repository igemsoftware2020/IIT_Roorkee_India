#!/usr/bin/env python
# coding: utf-8

#importing necessary libraries
import numpy as np
from sklearn.feature_selection import VarianceThreshold, SelectFromModel
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
import os
import pickle

list_antibiotics = ["ciprofloxacin","levofloxacin","gentamicin","tobramycin","amikacin","ceftriaxone","imipenem","ceftazidime",
                   "trimethoprim+sulfamethoxazole","ampicillin+sulbactam"]

antibiotic_name = "ciprofloxacin" #choose the antibiotic from above options

#creating directory to store the results
os.mkdir("./results") #need to create results directory using this command before executing the next command in case it is not present already
os.mkdir("./results/"+antibiotic_name)  
#loading the dataset
x = np.load("./dataset_antibiotic/"+antibiotic_name+"/features.npy")
y = np.load("./dataset_antibiotic/"+antibiotic_name+"/labels.npy")
keys = np.load("./list_strains/unique_genes.npy")

#removal of features with very low variance i.e. below 0.01

selector = VarianceThreshold(threshold=.01) #creation of selector function
selector.fit_transform(x) #selection of important features as per criteria
x = x[:,selector.get_support()] #transformation of dataset 
keys = keys[selector.get_support()]
#saving names selected features
np.save("./results/"+antibiotic_name+"/keys.npy",keys)

#training machine learnig algorithm for various iterations
weights = np.zeros(keys.shape) #to store absolute weights of each feature

dict_weights = {} #to store the weights of features for every iteration
for k in keys:
    dict_weights[k] = [] 
    
for i in range(250):
    
    clf = SGDClassifier(loss="hinge", penalty="l1", shuffle=True, class_weight="balanced" , alpha=0.0001) #SGD Classifier i.e. linear SVM trained using SGD algorithm

    xtrain, xtest, ytrain, ytest = train_test_split(x,y,train_size = 0.8,stratify=None) #random splitting of dataset to train and validate the model

    clf.fit(xtrain,ytrain) #training the model

    weight = clf.coef_[0] #accessing the weight given to each feature for a particular iteration
    for k in range(keys.shape[0]):
        weights[k] += abs(weight[k]) #adding up the absolute weight
        dict_weights[keys[k]].append(weight[k]) #storing weight of particular iteration 
    print(i+1) #printing iteration number

np.save("./results/"+antibiotic_name+"/weights_direct.npy",weights) #saving absolute weights
pickle.dump(dict_weights,open("./results/"+antibiotic_name+"/dict_weights_direct.pkl",'wb'))