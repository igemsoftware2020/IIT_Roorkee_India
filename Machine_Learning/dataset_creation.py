#!/usr/bin/env python
# coding: utf-8

import numpy as np #import necessary libraries
import os

list_antibiotics = ["ciprofloxacin","levofloxacin","gentamicin","tobramycin","amikacin","ceftriaxone","imipenem","ceftazidime",
                   "trimethoprim+sulfamethoxazole","ampicillin+sulbactam"]

os.mkdir("./dataset_antibiotic") #if it is not created, then run this command
for antibiotic in list_antibiotics:
    os.mkdir("./dataset_antibiotic/"+antibiotic)
    x = []
    y = []
    res_strains = np.load("./list_strains/"+antibiotic+"/res_strains.npy")
    for res_strain in res_strains:
        arr = np.load("./strain_genome/"+res_strain+".npy")
        x.append(arr)
        y.append(1)
    sus_strains = np.load("./list_strains/"+antibiotic+"/sus_strains.npy")
    for sus_strain in sus_strains:
        arr = np.load("./strain_genome/"+sus_strain+".npy")
        x.append(arr)
        y.append(0)
    
    x = np.array(x)
    y = np.array(y)
    np.save("./dataset_antibiotic/"+antibiotic+"/features.npy",x)
    np.save("./dataset_antibiotic/"+antibiotic+"/labels.npy",y)