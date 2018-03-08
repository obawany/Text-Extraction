import numpy as np
import pandas as pd
import csv
import logging
import os
import io
import sys
#import mygene

path = '/Users/obawany/Desktop/GItHub Repositories/Text-Extraction/'

# with open('PTEN_ceRNAs.txt') as infile:
# 	mg = mygene.MyGeneInfo()

# 	genes = []
# 	for line in infile:
# 	    genes.append(line.strip())

# 	for gene in genes:
# 	    result = mg.query(gene, scopes="symbol", fields=["ensembl"], species="human", verbose=False)
# 	    hgnc_name = gene
# 	    for hit in result["hits"]:
# 	        if "ensembl" in hit and "gene" in hit["ensembl"]:
# 	            sys.stdout.write("%s\t%s\n" % (hgnc_name, hit["ensembl"]["gene"]))



d = {}
with open("mart_export_Gene_Name_Id.txt") as f:
    for line in f:
       (val, key) = line.split()
       d[string(key)] = val



