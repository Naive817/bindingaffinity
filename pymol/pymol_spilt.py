#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymol
from pymol import cmd
import os
import time
import pandas as pd
def spilt(i):
    cmd.extract("ligand","sele")
    cmd.h_add("ligand")
    if not os.path.exists(r"D:\mystuff\test\{}\{}_pocket.pdb".format(i,i)):
        dir = r"D:/mystuff/test/{}/{}_pocket.pdb".format(i, i)
        para = '{} within 10 to ligand'.format(i)
        cmd.select('new', para)
        cmd.save(dir, "new")
        print("saving {}'s pocket".format(i))
    if not os.path.exists(r"D:\mystuff\test\{}\{}_protein.pdb".format(i,i)):
        cmd.select ('protein' and 'polymer') and not 'solvent'
        dir = r"D:\mystuff\test\{}\{}_protein.pdb".format(i, i)
        cmd.save(dir, "sele")
    if not os.path.exists(r"D:\mystuff\test\{}\{}_ligand.sdf".format(i,i)):
        dir = r"D:\mystuff\test\{}\{}_ligand.sdf".format(i,i)
        cmd.save(dir, "ligand")
    if not os.path.exists(r"D:\mystuff\test\{}\{}_ligand.mol2".format(i,i)):
        dir = r"D:\mystuff\test\{}\{}_ligand.mol2".format(i, i)
        cmd.save(dir, "ligand")

#d=r"D:\mystuff\binding affinity data all.csv"
#df = pd.read_csv(d)
#l=df.loc[:,'PDB']
#for i in l:
    #spilt(i)

cmd.extend("spilt", spilt)