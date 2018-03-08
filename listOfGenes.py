import numpy as np
import pandas as pd
import csv
import logging
import os
import io
import sys
#import mygene

path = '/Users/obawany/Desktop/GItHub Repositories/Text-Extraction/'

# my_dict = {}

with open('mart_export_Gene_Name_Id.txt', 'r') as dictonary, open('GeneNameByScoreOrdered.txt', 'r') as namestoLookup, open('GeneNameByScoreOrdered.ensembl_id.txt', 'w') as out:
		geneNamesComingFromNeeded = []
		for line in namestoLookup:
			#print (line)
			geneName = line.split()
			# print(geneName)
			geneNameStr = geneName[0]
			geneNamesComingFromNeeded.append(geneNameStr)
			# print(geneNameStr)
		# print(geneNamesComingFromNeeded)
		# for element in geneNamesComingFromNeeded:
		dict_my_own = {}
		# for element in geneNamesComingFromNeeded:
		for lineofdict in dictonary:
			gene_name_from_mart = lineofdict.split('\t')
			gene_name_dcit = gene_name_from_mart[1].strip('\n')
			ensembl_id_dict = gene_name_from_mart[0]
				# print(gene_name_dcit + ' ' + ensembl_id_dict)

			dict_my_own[gene_name_dcit] = ensembl_id_dict

		# print(geneNamesComingFromNeeded)
		#print(dict_my_own)	

		for elem in geneNamesComingFromNeeded:
			for gene, ensembl in dict_my_own.items():
				if (gene==elem):
					out.write(elem + '\t' + ensembl + '\n')
				# if (element in gene_name_dcit):
				# 	print(element)
				# print(gene_name_dcit)
				# print(geneNameStr)
				# print(gene_name_dcit)
				# print(gene_name_dcit)

				#print(gene_name_from_mart[1])
				# print(geneName)
				# if (geneNameStr in gene_name_dcit ):
			# 	if (lineofdict[1] == geneName):
			# 		ensembl_id = lineofdict[0]
			# 	line = line + '\t' + lineofdict[0]
			# 	out.write(line + '\n')

namestoLookup.close()
dictonary.close()
out.close()


# infile = open(".txt")
# for line in infile:
#     #line = line.strip() 
#     #parts = [p.strip() for p in line.split("\t")]
#     parts = [p for p in line.split("\t")]
#     my_dict[parts[0]] = parts[1]
#     print line

# for key in my_dict:
#     print "key: " + key + "\t" + "value " + my_dict[key]


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



# d = {}
# with open("mart_export_Gene_Name_Id.txt") as f:
#     for line in f:
#        (val, key) = line.split()
#        d[string(key)] = val



