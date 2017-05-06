#!/usr/bin/python
"""
Find no. of ppi for RBPs.
"""
# my edit - aarthi
import csv

rbps_from_list_of_rbps=[]
dictionary={}

with open("list_of_all_RBPs.txt","r") as csvfile:
    reader=csv.reader(csvfile, delimiter="\t")
    for lines in reader:
        rbps_from_list_of_rbps.append(lines[0])

# ppi file from biogrid
with open("prtn_prtn.txt","rU") as csvfile:
    reader=csv.reader(csvfile, delimiter="\t")
    reader.next()
    for lines in reader:
        if lines[0] in rbps:
            dictionary[lines[0]]=[]

with open("output.txt","w") as f:
    with open("prtn_prtn.txt","rU") as csvfile:
        reader=csv.reader(csvfile, delimiter="\t")
        for lines in reader:
            for keys in dictionary:
                if keys in lines[0]:
                    if lines[1] in rbps_from_list_of_rbps:
                        dictionary[keys].append(lines[1])

dictionary_1=sorted(dictionary)

with open("output.txt","w") as f:
    for key in sorted(dictionary.iterkeys()):
        print>>f, "%s    %s" % (key, len(dictionary[key]))
