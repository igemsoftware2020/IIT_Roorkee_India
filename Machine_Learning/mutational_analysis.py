#!/usr/bin/env python
# coding: utf-8

#importing necessary libraries
import numpy as np
import pandas as pd


list_antibiotics = ["ciprofloxacin","levofloxacin","gentamicin","tobramycin","amikacin","ceftriaxone","imipenem","ceftazidime",
                   "trimethoprim+sulfamethoxazole","ampicillin+sulbactam"]

antibiotic_name = "ciprofloxacin" #choose the antibiotic from above options

x = np.load("./dataset_antibiotic/"+antibiotic_name+"/features.npy")
y = np.load("./dataset_antibiotic/"+antibiotic_name+"/labels.npy")
keys = np.load("./list_strains/unique_genes.npy")
mutations = pd.read_excel("./results/"+antibiotic_name+"/mutation.xlsx")

mutations = np.array(mutations)
mutations = mutations[:,:2]

pairs = [] #to store the pairs which have already been analysed for mutations
count = 0
for pair in mutations:
    count = count + 1
    gene1, gene2 = pair[0], pair[1]
    pair1 = gene1 + "&" + gene2
    pair2 = gene2 + "&" + gene1
    if not (pair1 in pairs or pair2 in pairs): #if gene-gene pair is already analysed, then skip it
        pairs.append(pair1)
        pairs.append(pair2)
        first = []
        first.append(gene1)
        i = 1
        b = True
        while(b):
            c = gene1 + '_' + str(i)
            if c in keys:
                first.append(c)
                i = i + 1
            else:
                b = False

        second = [] 
        second.append(gene2)
        i = 1
        b = True
        while(b):
            c = gene2 + '_' + str(i)
            if c in keys:
                second.append(c)
                i = i + 1
            else:
                b = False
        first.append('Total')
        second.append('Total')
        scores = np.empty_like('                              ',shape=(len(first),len(second)))
    
        for f in first[:-1]:
            index = np.where(keys==f)[0]
            x_index = x[:,index].reshape(-1)
            total = x_index.sum()
            total_re = y[np.where(x_index==1)[0]].sum()
            if total == 0:
                scores[first.index(f),-1] = ''
            else:
                scores[first.index(f),-1] = str(total_re)+'/'+str(total) + '(' + str(round(total_re/total,4)) + ')'
        
        for s in second[:-1]:
            index = np.where(keys==s)[0]
            x_index = x[:,index].reshape(-1)
            total = x_index.sum()
            total_re = y[np.where(x_index==1)[0]].sum()
            if total == 0:
                scores[-1,second.index(s)] = ''
            else:
                scores[-1,second.index(s)] = str(total_re)+'/'+str(total) + '(' + str(round(total_re/total,4)) + ')'
        
        for f in first[:-1]:
            for s in second[:-1]:
                f_index = np.where(keys==f)[0]
                s_index = np.where(keys==s)[0]
                xf = x[:,f_index]
                xs = x[:,s_index]

                xf_indexes = np.where(xf==1)[0]
                xs_indexes = np.where(xs==1)[0]

                intersect_indexes = []
                for i in xf_indexes:
                    if i in xs_indexes:
                        intersect_indexes.append(i)

                total = len(intersect_indexes)
                total_re = y[intersect_indexes].sum()
                if total == 0:
                    scores[first.index(f),second.index(s)] = ''
                else:
                    scores[first.index(f),second.index(s)] = str(total_re)+'/'+str(total) + '(' + str(round(total_re/total,4)) + ')'
            
    
        mutation_scores = []
        mutation = []
        mutation.append('')
        for s in second:
            mutation.append(s)
        mutation_scores.append(mutation)
        for f in first:
            mutation_scores.append([f,*scores[first.index(f)]])
        columns = mutation_scores[0]
        mutation_scores = mutation_scores[1:]
        mutation_scores = pd.DataFrame(mutation_scores)
        mutation_scores.columns = columns
        mutation_scores.to_excel("./results/"+antibiotic_name+"/"+str(count)+"_"+pair[0]+" - "+pair[1]+'.xlsx',index=None)