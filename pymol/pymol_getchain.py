#!/usr/bin/env python
# coding: utf-8

# In[1]:

#remove extra chains

import pymol
from pymol import cmd
import os
import time
import pandas as pd
def getchain():
    chains=cmd.get_chains()
    print (chains)
    #cmd.select("chain A")
    cmd.select ('chain {}'.format(chains[1]))


cmd.extend("getchain", getchain)