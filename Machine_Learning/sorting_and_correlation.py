#!/usr/bin/env python
# coding: utf-8

#necessary libraries
import numpy as np
import pickle
import pandas as pd

list_antibiotics = ["ciprofloxacin","levofloxacin","gentamicin","tobramycin","amikacin","ceftriaxone","imipenem","ceftazidime",
                   "trimethoprim+sulfamethoxazole","ampicillin+sulbactam"]

antibiotic_name = "ciprofloxacin" #choose the antibiotic from above options

weights = np.load("./results/"+antibiotic_name+"/weights_direct.npy") #loading absolute weights
keys = np.load("./results/"+antibiotic_name+"/keys.npy") #loading selected features for that antibiotic using variance threshold
dict_weights = pickle.load(open("./results/"+antibiotic_name+"/dict_weights_direct.pkl",'rb')) #loading weights for every particular iteration

sort = np.argsort(weights)[::-1] #sorting the alleles in the order of decreasing absolute weights

top = [] #storing top alleles 
top_alleles = [] #for converting alleles and weights to external file
top_alleles.append(['Allele','Weights'])
for s in sort:
    top.append(keys[s])
    top_alleles.append([keys[s],weights[s]])

columns = top_alleles[0]
top_alleles = top_alleles[1:]
top_alleles = pd.DataFrame(top_alleles)
top_alleles.columns = columns
top_alleles.to_excel("./results/"+antibiotic_name+"/top_alleles.xlsx",index=None)

top = top[:40] #finding top 40 alleles 
correlation = np.zeros((40,40))
pairs = []
scores = []
for i in range(40):
   for j in range(40):
       if i < j:   #to avoid correlation matrix from being symmetric   
           correlation[i,j] = np.corrcoef(dict_weights[keys[sort[i]]],dict_weights[keys[sort[j]]])[0,1]
           pair = keys[sort[i]] + "&" + keys[sort[j]] 
           pairs.append(pair) #storing pair
           scores.append(correlation[i,j]) #storing the correlation
      
pairs = np.array(pairs) #list of pairs of alleles
scores = np.array(scores) #list of their corresponding correlation scores
abs_scores = np.abs(scores) #conversion of correlation scores to absolute scores

#code for plotting correlation plot
#in case you want to plot complete correlation plot, follow the code below.
# correlation = np.zeros((40,40))
# for i in range(40):
#     for j in range(40):
#         correlation[i,j] = np.corrcoef(dict_weights[keys[sort[i]]],dict_weights[keys[sort[j]]])[0,1]
#plt.imsave("./results/"+antibiotic_name+"/correlation.png",correlation)
#plt.colorbar() #to generate colorbar of correlation values


sort_indexes = abs_scores.argsort()[::-1] #sorting the pairs as per their correlation scores

epistatic_analysis = [] #storing genes and their corresponding alleles with higher correlation score
epistatic_analysis.append(['Gene 1','Gene 2','Allele 1','Allele 2','Score']) 
count = 0
for st in sort_indexes:
   if count >= 20: #limit is set to find top 20 correlations 
       break
   pair = pairs[st]
   allele1, allele2 = pair.split('&')
   if allele1 in top and allele2 in top:
       gene1 = allele1.split('_')[0]
       gene2 = allele2.split('_')[0]
       if gene1 != gene2: #to ensure that there are two different genes in the pair
           print(gene1,' ',gene2,scores[st])
           epistatic_analysis.append([gene1,gene2,allele1,allele2,scores[st]])
           count = count + 1

columns = epistatic_analysis[0]
epistatic_analysis = epistatic_analysis[1:]

epistatic_analysis = pd.DataFrame(epistatic_analysis)
epistatic_analysis.columns = columns
epistatic_analysis.to_excel("./results/"+antibiotic_name+"/epistatic.xlsx",index=None) #storing the list of pair correlations





